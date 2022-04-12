from threading import Thread, Lock
from vosk import Model, KaldiRecognizer, SetLogLevel
import pyaudio
import wave
import regex as re
import kivy
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.properties import StringProperty
from translator import Sentence
from dicter import speak
from database import DataBase


kivy.require('2.0.0')

class CreateAccountWindow(Screen):
    namee = ObjectProperty(None)
    email = ObjectProperty(None)
    password = ObjectProperty(None)

    def submit(self):
        if self.namee.text != "" and self.email.text != "" and self.email.text.count("@") == 1 and self.email.text.count(".") > 0:
            if self.password != "":
                db.add_user(self.email.text, self.password.text, self.namee.text)

                self.reset()

                sm.current = "login"
            else:
                invalidForm()
        else:
            invalidForm()

    def login(self):
        self.reset()
        sm.current = "login"

    def reset(self):
        self.email.text = ""
        self.password.text = ""
        self.namee.text = ""


class LoginWindow(Screen):
    email = ObjectProperty(None)
    password = ObjectProperty(None)

    def loginBtn(self):
        if db.validate(self.email.text, self.password.text):
            PropertiesWindow.current = self.email.text
            self.reset()
            sm.current = "trad"
        else:
            invalidLogin()

    def createBtn(self):
        self.reset()
        sm.current = "create"

    def reset(self):
        self.email.text = ""
        self.password.text = ""


class TradScreen(Screen):
    def __init__(self,**kwargs):
        super(TradScreen, self).__init__(**kwargs)
        global gameview
        gameview = GameView(Recorder("mic.wav"),Player("mic.wav"))
        self.add_widget(gameview)

    textecritrad=StringProperty("Translation")
    my_text = StringProperty("Press and hold to record your message")

    def propout(self):
        sm.current = "properties"

    def start_record(self):
        gameview.start_record()

    def stop_record(self):
        gameview.stop_record()
        self.my_text = string2

    def traduire(self):
        self.mytext=gameview.traduire(self.ids.buttonDepart.text,
                                      self.ids.buttonArrivee.text)

    def traduire2(self):
        self.textecritrad=gameview.traduire2(self.ids.buttonDepart.text,
                                             self.ids.buttonArrivee.text,
                                             self.ids.textecrit.text)

    def dicter(self):
        gameview.dicter()
    
    def dicter2(self):
        gameview.dicter2()


class PropertiesWindow(Screen):
    n = ObjectProperty(None)
    created = ObjectProperty(None)
    email = ObjectProperty(None)

    def goBack(self):
        sm.current = "trad"

    def logOut(self):
        sm.current = "login"

    def on_enter(self, *args):
        password, name, created = db.get_user(self.current)
        self.n.text = "Account Name: " + name
        self.email.text = "Email: " + self.current
        self.created.text = "Created On: " + created


class WindowManager(ScreenManager):
    pass


def invalidLogin():
    pop = Popup(title='Invalid Login',
                  content=Label(text='Invalid username or password.'),
                  size_hint=(None, None), size=(400, 400))
    pop.open()


def invalidForm():
    pop = Popup(title='Invalid Form',
                  content=Label(text='Please fill in all inputs with valid information.'),
                  size_hint=(None, None), size=(400, 400))

    pop.open()


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


class GameView(Widget):
    textToCode={
        "Source Language":"fr",
        "Target language":"en",
        "English":"en",
        "Spanish":"es",
        "French":"fr",
        "Italian":"it",
        "German":"de"}
    voice={
        "en":2,
        "es":6,
        "fr":7,
        "it":9,
        "de":11,}
    def __init__(self, recorder, player, **kwargs):
        super().__init__(**kwargs)
        self.recorder = recorder
        self.player = player
        self.sentence = Sentence
        self.langue1="fr"
        self.langue2="en"

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

        string = rec.PartialResult()
        global string2
        string2 = re.sub('\}|\{|\:|\"partial"|\"','', string)
        self.my_text = string2
        return string2

    def traduire(self,L1,L2):
        sentence = Sentence(string2,GameView.textToCode[L1])
        sentence.translate(GameView.textToCode[L2])
        t=sentence.write()
        self.my_text=t
        return t

    def traduire2(self,L1,L2,text):
        sentence=Sentence(str(text),GameView.textToCode[L1])
        sentence.translate(GameView.textToCode[L2])
        t=sentence.write()
        self.textecritrad=t
        return t


    def dicter(self):
        if self.my_text!=None:
            speak(self.my_text,GameView.voice[self.langue2])
        else :
            pass

    def dicter2(self):
        speak(self.textecritrad,GameView.voice[self.langue2])


db = DataBase("users.txt")

kv = Builder.load_file("trad.kv")

sm = WindowManager()

sm.add_widget(LoginWindow(name="login"))
sm.add_widget(CreateAccountWindow(name="create"))
sm.add_widget(PropertiesWindow(name="properties"))
sm.add_widget(TradScreen(name="trad"))
# sm.add_widget(GameView(Recorder("mic.wav"),Player("mic.wav"), name='game'))
sm.current = "login"


# Gv = GameView(Recorder("mic.wav"), Player("mic.wav"))

class TradApp(App):
    def build(self):
        return sm

if __name__ == '__main__':
    tradApp = TradApp()
    tradApp.run()
