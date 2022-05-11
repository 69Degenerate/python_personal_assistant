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
from calculator import cal


engine =pyttsx3.init('sapi5')
voices =engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)

class Assistant(Widget):
    def textt(self,call):
        self.leb.text=str(call)#
       # self.ids.mic1.source='mic2.png'

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
            k.pause_threshold ==0.7
            audio=k.listen(source)
        try:
            print("Recognizing......")
            self.speak("Recognizing......")
            query=k.recognize_google(audio, language='Eng-in')    
            print(f"user said: ",{query},"\n")
        except Exception as e:
            print("Say that again please....")
            self.speak("Say that again please....")
            return "None"
            
        self.ids.mic1.source='mic1.png'
        self.exe(query)



    def sendEmail(to,content):
        server=smtplib.SMTP('smtp.gmail.com',587)
        server.ehlo()
        server.starttls()
        server.login('amolbrand00@gmail.com','amol@1234#')
        server.sendmail('amolbrand00@gmail.com',to,content)
        server.close()

    def cal():
        return cal.calcApp.run()
            
    def exe(self,query): 
        query=query.lower()
        if 'wikipedia' and 'Wikipedia' in query:
                    try:
                        self.speak('searching Wikipedia....')
                        query= query.replace("wikipedia",'')
                        results = wikipedia.summary(query,sentences=1)
                        self.speak("Acording To Wikipedia")
                        self.speak(results)
                    except Exception as e:
                        print(e)
                        self.speak("There was problem, Check your internet connection  Or Check your query is correct?")
        elif 'time' and 'Time' and 'TIME' in query:
                    strtime= datetime.datetime.now().strftime("%H:%M:%S")
                    self.speak(f"The time is {strtime}")

#FOLLOWING CODE PUT IN ANOTHER WINDOW
        elif 'game' in query:
                self.speak("Welcome to  adventure game")
                print("THE ADVENTURE GAME")
                self.speak("Let's play the game...! ")
                self.speak("What is your name?")
                name = input("Type your name: ")
                self.speak("Welcome", name, "to this adventure!")
                print("Welcome", name, "to this adventure!")

                self.speak("You are on a dirt road, it has come to an end and you can go left or right. Which way would you like to go? ")
                answer = input( "You are on a dirt road, it has come to an end and you can go left or right. Which way would you like to go? \n")

                if answer == "left":
                    self.speak("You come to a river, you can walk around it or swim accross? Type walk to walk around and swim to swim accross: ")
                    answer = input("You come to a river, you can walk around it or swim accross? Type walk to walk around and swim to swim accross: ")

                    if answer == "swim":
                        self.speak("You swam acrross and were eaten by an alligator.")
                        print("You swam acrross and were eaten by an alligator.")
                    elif answer == "walk":
                        self.speak("You walked for many miles, ran out of water and you lost the game.")
                        print("You walked for many miles, ran out of water and you lost the game.")
                    else:
                        self.speak("Ohuh.., That's not correct answer")
                        print('Not a valid option. You lose.')

                elif answer == "right":
                    self.speak("You come to a bridge, it looks wobbly, do you want to cross it or head back (cross/back)? ")
                    answer = input("You come to a bridge, it looks wobbly, do you want to cross it or head back (cross/back)? ")

                    if answer == "back":
                        self.speak("You go back and lose.")
                        print("You go back and lose.")
                    elif answer == "cross":
                        self.speak("You cross the bridge and meet a stranger. Do you talk to them (yes/no)? ")
                        answer = input("You cross the bridge and meet a stranger. Do you talk to them (yes/no)? ")

                        if answer == "yes":
                            self.speak("You talk to the stanger and they give you gold. You WIN!")
                            print("You talk to the stanger and they give you gold. You WIN!")
                        elif answer == "no":
                            self.speak("You ignore the stranger and they are offended and you lose.")
                            print("You ignore the stranger and they are offended and you lose.")
                        else:
                            self.speak("Ohuh.., Chose correct answer")
                            print('Not a valid option. You lose.')
                    else:
                        self.speak("Ohuh.., Chose correct answer")
                        print('Not a valid option. You lose.')

                else:
                    self.speak("Ohuh.., Chose correct answer")
                    print('Not a valid option. You lose.')

                print("Thank you for trying", name)            
#===========================================================================================================================================
#FOLLOWING CODE PUT IN ANOTHER WINDOW

        elif 'i want to watch movies' in query:
            self.speak("Here list of movies.")
            j="1)Moonfall\n2)Gangubai\n3)Pawankhind"
            self.leb.text=j
            self.speak(' which movie you want to watch in this.')
            movie=query
            if 'moonfall' in movie:
             webbrowser.open('https://drive.google.com/file/d/1SEaKYjiQXVLbgJhtOiBSoY6OICwFct5o/view?usp=sharing')   
            elif 'gangubai' in movie:
                webbrowser.open('https://drive.google.com/file/d/1G676i4Vft5iD-pclUdek6x46vIqhRaoV/view?usp=sharing')
            elif 'pawankhind' in movie:
                webbrowser.open('https://drive.google.com/file/d/1ubVMz_I-r9wdWx1Ejcr-_8IzL82w2Vrn/view?usp=sharing')
        elif 'youtube' in query:
                    self.speak('starting')
                    time.sleep(3)
                    webbrowser.open('https://youtu.be/iik25wqIuFo')
#============================================================================================================================



        elif 'help' in query:
                self.speak('here are some query you can use')
                h="who are you : for the intoduction of AI \nyoutube : to start youtube in web browser \ntime : to check current time \nwikipedia : to search wikipedia \nquit : to terminate program"
                self.leb.text=h
        elif'who are you' in query:
                    self.speak('I am veronica, i am A.i system of created by self,with love of you, i m a ho,such a disspointment to this dammed world') 
       

        elif 'calculator' in query:
               Assistant.cal()

        elif 'exit' in query:
             quit()
        else:
                self.speak("please give appropriate query")


    def anim(self,widget,*args):
        animate=Animation(background_color=(0,0,0,0),d=1)
        animate.start(widget)
        


    def update(self,*args):
        self.ti.text= datetime.datetime.now().strftime("[b]%H:%M[/b]:%S")
    def __init__(self, **kwargs):
        super(Assistant,self).__init__(**kwargs)
        Clock.schedule_interval(self.update,1)



class app(a):
    def build(self):
        return Assistant()

app().run()

# if __name__=='__main__':
#     app().run()
