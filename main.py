from threading import Thread, Lock
from kivy.event import EventDispatcher
from pynput import keyboard
from vosk import Model, KaldiRecognizer, SetLogLevel
import pyaudio
import wave
import os
import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.properties import StringProperty

kivy.require('2.0.0')

class Player():
    def __init__(self, wavfile):
        self.wavfile = wavfile
        self.playing = 0  # flag so we don't try to record while the wav file is in use
        self.lock = Lock()  # muutex so incrementing and decrementing self.playing is safe

    def run(self):
        with self.lock:
            self.playing += 1
        with wave.open(self.wavfile, 'rb') as wf:
            p = pyaudio.PyAudio()
            stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
                            channels=wf.getnchannels(),
                            rate=wf.getframerate(),
                            output=True)
            data = wf.readframes(8192)
            while data != b'':
                stream.write(data)
                data = wf.readframes(8192)

            stream.stop_stream()
            stream.close()
            p.terminate()
            wf.close()
        with self.lock:
            self.playing -= 1

    def start(self):
        Thread(target=self.run).start()


class Recorder():
    def __init__(self,
                 wavfile,
                 chunksize=8192,
                 dataformat=pyaudio.paInt16,
                 channels=1,
                 rate=44100):
        self.filename = wavfile
        self.chunksize = chunksize
        self.dataformat = dataformat
        self.channels = channels
        self.rate = rate
        self.recording = False
        self.pa = pyaudio.PyAudio()

    def start(self):
        # we call start and stop from the keyboard listener, so we use the asynchronous
        # version of pyaudio streaming. The keyboard listener must regain control to
        # begin listening again for the key release.
        if not self.recording:
            self.wf = wave.open(self.filename, 'wb')
            self.wf.setnchannels(self.channels)
            self.wf.setsampwidth(self.pa.get_sample_size(self.dataformat))
            self.wf.setframerate(self.rate)

            def callback(in_data, frame_count, time_info, status):
                # file write should be able to keep up with audio data stream (about 1378 Kbps)
                self.wf.writeframes(in_data)
                return (in_data, pyaudio.paContinue)

            self.stream = self.pa.open(format=self.dataformat,
                                       channels=self.channels,
                                       rate=self.rate,
                                       input=True,
                                       stream_callback=callback)
            self.stream.start_stream()
            self.recording = True
            print('recording started')

    def stop(self):
        if self.recording:
            self.stream.stop_stream()
            self.stream.close()
            self.wf.close()

            self.recording = False
            print('recording finished')


class GameView(BoxLayout):
    def __init__(self,recorder,player, **kwargs):
        super().__init__(**kwargs)
        self.recorder = recorder
        self.player = player

    my_text = StringProperty("Maintenez appuyer pour enregistrer votre message")

    def start_record(self):
        if self.player.playing == 0:
            self.recorder.start()

    def stop_record(self):
        self.recorder.stop()
        
        SetLogLevel(0)
        wf = wave.open("mic.wav", "rb")
        model = Model("model_fr")
        rec = KaldiRecognizer(model, wf.getframerate())
        rec.SetWords(True)

        while True:
            data = wf.readframes(4000)
            if len(data) == 0:
                break
            if rec.AcceptWaveform(data):
                print(rec.Result())

        self.my_text = rec.PartialResult()     

class TradApp(App):
    def build(self):
        recorder = Recorder("mic.wav")
        player = Player("mic.wav")
        return GameView(recorder, player)

if __name__ == '__main__':
    tradApp = TradApp()
    tradApp.run()
