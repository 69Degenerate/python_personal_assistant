import time
import pyttsx3
import speech_recognition as sr
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
import datetime
# import pyaudio
import wikipedia
import webbrowser
from kivy.config import Config
import os
import smtplib
# import googletrans
from kivy.app import App as a
from kivy.uix.button import Button as b
from kivy.uix.widget import Widget
from kivy.uix.textinput import TextInput
from kivy.clock import Clock
from kivy.core.image import Image
from kivy.animation import Animation
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
# import game


class WindowManager(ScreenManager):
	pass

engine =pyttsx3.init()
voices =engine.getProperty('voices')
engine.setProperty('voice',voices[-1].id)

class FirstWindow(Screen):
    pass

class SecondWindow(Screen,Widget):
    def scr(self,screen):
        self.ids.f.current=screen
        self.ids.f.trigger_action(0.2)
    def textt(self,call):
        self.leb.text=str(call)
        self.ids.mic1.source='mic2.png'

    def off(self):
        self.ids.mic1.source='mic2.png'


    def speak(self,audio):
        self.leb.text=self.leb.text+"\n \n"+str(audio)
        print(audio)
        engine.say(audio)
        engine.runAndWait()


    def wishme(self):
        hour = int(datetime.datetime.now().hour)
        self.speak("hello sir ")    
        if hour>=0 and hour<12:
            self.speak("Good Morning!")
        elif hour>=12 and hour<18:
            self.speak("Good Afternoon!")
        else:
            self.speak("Good Evining!")         
        self.speak("i am friday, how may i help you?")        


    def listen(self):
        k = sr.Recognizer()
        with sr.Microphone() as source:
            self.speak("Listening....")
            k.pause_threshold == 1
            audio=k.listen(source)
        try:
            self.speak("Recognizing......")
            query=k.recognize_google(audio, language='eng-in')    
            print("user said: ",{query},"\n")
        except Exception as e:
            print("Say that again please....")
            self.speak("Say that again please....")
            return "None"
        self.ids.mic1.source='mic1.png'
        return query


    def sendEmail(to,content):
        server=smtplib.SMTP('smtp.gmail.com',587)
        server.ehlo()
        server.starttls()
        server.login('amolbrand00@gmail.com','amol@1234#')
        server.sendmail('amolbrand00@gmail.com',to,content)
        server.close()
    def Alarm(query):
        TimeHere=open('data.txt','a')
        TimeHere.write(query)
        TimeHere.close()
        os.startfile("C:\\Users\\Amol\\Desktop\\project\\project\\changes\\changes\\Database\\alarm.py")
     

            
    def exe(self,query):
        if 'wikipedia' in query:
                    try:
                        self.speak('searching Wikipedia....')
                        query= query.replace("wikipedia","")
                        results = wikipedia.summary(query,sentences=50)
                        self.speak("Acording To Wikipedia")
                        print(results)
                        self.speak(results)
                    except Exception as e:
                        print(e)
                        self.speak("sorry boss ,i am not able get any appropriate result from wikipedia")
        elif 'time' in query:
                    strtime= datetime.datetime.now().strftime("%H:%M:%S")
                    self.speak(f"The time is {strtime}")
        elif 'next' in query:
            self.ids.f.trigger_action(0.2)
            # self.scr("third")
        elif 'third' in query:
            self.ids.t.trigger_action(0.2)
        elif 'forth' in query:
            self.ids.fo.trigger_action(0.2)
            # self.scr('third')    
        elif " alarm" in query:
            self.speak("in which time")

            self.Alarm('set alarm for 5 and 07 ')

        elif 'youtube' in query:
                    self.speak('starting')
                    time.sleep(3)
                    webbrowser.open('https://youtu.be/iik25wqIuFo')
        elif 'help' in query:
                self.speak('here are some query you can use')
                h='''
who are you : for the intoduction of AI 
youtube : to start youtube in web browser
time : to check current time 
wikipedia : to search wikipedia 
next:goto the second screen 
quit : to terminate program
                '''
                self.leb.text=self.leb.text+h
        elif'who are you' in query:
                    self.speak('I am veronica, i am A.i system of created by self,with love of you, i m a ho,such a disspointment to this dammed world') 
        
        elif 'quit' in query:

            self.speak('have a great day')    

            quit()
        else:
                self.speak("please give appropriate query")

    def anim(self,widget,*args):
        animate=Animation(background_color=(0,0,0,0),d=1)
        animate.start(widget)
        


    def update(self,*args):
        self.ti.text= datetime.datetime.now().strftime("[b]%H:%M[/b]:%S")
    def __init__(self, **kwargs):
        super(SecondWindow,self).__init__(**kwargs)
        Clock.schedule_interval(self.update,1)

class ThirdWindow(Screen):
    # game.Game()
    pass

class FourthWindow(Screen,GridLayout):
    Config.set('graphics', 'resizable', 1)
    def calculate(self, calculation):
            if calculation:
                try:
                    self.display.text = str(eval(calculation))
                except Exception:
                    self.display.text = "Error"
    def delete(self, dele):
            if dele:
                try:
                    self.display.text = str(dele[:-1])
                except Exception:
                    self.display.text = "Error"
    def exit(self):
            quit()



kv = Builder.load_file('app.kv')
class app(App):
	def build(self):
		return kv

if __name__ == '__main__':
    app().run()