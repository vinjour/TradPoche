from threading import Thread, Lock
from pynput import keyboard
from vosk import Model, KaldiRecognizer, SetLogLevel
import pyaudio
import wave
import os


class player:
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


class recorder:
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


class listener(keyboard.Listener):
    def __init__(self, recorder, player):
        super().__init__(on_press=self.on_press, on_release=self.on_release)
        self.recorder = recorder
        self.player = player

    def on_press(self, key):
        if key is None:  # unknown event
            pass
        elif isinstance(key, keyboard.Key):  # special key event
            if key.space and self.player.playing == 0:
                self.recorder.start()
        elif isinstance(key, keyboard.KeyCode):  # alphanumeric key event
            if key.char == 'q':  # press q to quit
                if self.recorder.recording:
                    self.recorder.stop()
                return False  # this is how you stop the listener thread
            if key.char == 'p' and not self.recorder.recording:
                self.player.start()
            if key.char == 't' and not self.recorder.recording:
                SetLogLevel(0)
                if not os.path.exists("model_fr"):
                    print(
                        "Please download the model from https://alphacephei.com/vosk/models and unpack as 'model' in the current folder.")
                    exit(1)

                wf = wave.open("mic.wav", "rb")
                if wf.getnchannels() != 1 or wf.getsampwidth() != 2 or wf.getcomptype() != "NONE":
                    print("Audio file must be WAV format mono PCM.")
                    exit(1)

                model = Model("model_fr")
                rec = KaldiRecognizer(model, wf.getframerate())
                rec.SetWords(True)

                while True:
                    data = wf.readframes(4000)
                    if len(data) == 0:
                        break
                    if rec.AcceptWaveform(data):
                        print(rec.Result())

                print(rec.FinalResult())



    def on_release(self, key):
        if key is None:  # unknown event
            pass
        elif isinstance(key, keyboard.Key):  # special key event
            if key.space:
                self.recorder.stop()
        elif isinstance(key, keyboard.KeyCode):  # alphanumeric key event
            pass


if __name__ == '__main__':
    r = recorder("mic.wav")
    p = player("mic.wav")
    l = listener(r, p)
    print('hold spacebar to record press p to playback, press q to quit, press t to translate')
    l.start()  # keyboard listener is a thread so we start it here
    l.join()  # wait for the tread to terminate so the program doesn't instantly close