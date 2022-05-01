import time
import pyttsx3
import speech_recognition as sr
import datetime
import pyaudio
import wikipedia
import webbrowser
import os
import smtplib
import googletrans
from kivy.app import App as a
from kivy.uix.button import Button as b
from kivy.uix.widget import Widget
from kivy.uix.textinput import TextInput
from kivy.clock import Clock
from kivy.core.image import Image
from kivy.animation import Animation


engine =pyttsx3.init()
voices =engine.getProperty('voices')
engine.setProperty('voice',voices[-1].id)

class game(Widget):
    def textt(self,call):
        self.leb.text=str(call)#
        self.ids.mic1.source='mic2.png'

    def off(self):
        self.ids.mic1.source='mic2.png'


    def speak(self,audio):
        self.leb.text=str(audio)
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
            print("Listening....")
            k.pause_threshold == 1
            audio=k.listen(source)
        try:
            print("Recognizing......")
            self.speak("Recognizing......")
            query=k.recognize_google(audio, language='mar-in')    
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

            
    def exe(self,query):
        if 'wikipedia' in query:
                    try:
                        self.speak('searching Wikipedia....')
                        query= query.replace("wikipedia","")
                        results = wikipedia.summary(query,sentences=1)
                        self.speak("Acording To Wikipedia")
                        self.speak(results)
                    except Exception as e:
                        print(e)
                        self.speak("sorry boss ,i am not able get any appropriate result from wikipedia")
        elif 'time' in query:
                    strtime= datetime.datetime.now().strftime("%H:%M:%S")
                    self.speak(f"The time is {strtime}")
        elif 'youtube' in query:
                    self.speak('starting')
                    time.sleep(3)
                    webbrowser.open('https://youtu.be/iik25wqIuFo')
        elif 'help' in query:
                self.speak('here are some query you can use')
                h="who are you : for the intoduction of AI \nyoutube : to start youtube in web browser \ntime : to check current time \nwikipedia : to search wikipedia \nquit : to terminate program"
                self.leb.text=h
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
        super(game,self).__init__(**kwargs)
        Clock.schedule_interval(self.update,1)



class app(a):
    def build(self):
        return game()

app().run()

# if __name__=='__main__':
#     app().run()