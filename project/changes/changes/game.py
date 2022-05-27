# from cv2 import logPolar
import pyttsx3
import speech_recognition as sr

engine =pyttsx3.init('sapi5')
voices =engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)


def speak(*audio):
        engine.say(audio)
        engine.runAndWait()


def listen():
        k = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening....")
            k.pause_threshold ==0.7
            audio=k.listen(source)
        try:
            print("Recognizing......")
            speak("Recognizing......")
            query=k.recognize_google(audio, language='Eng-in')    
            print(f"user said: ",{query},"\n")
        except Exception as e:
            print("Say that again please....")
            speak("Say that again please....")
            return "None"
        return query   
def Game():
    if __name__=="__main__":
        query=input()
        while True:
            if 'game'  in query:
                    speak("Welcome to game")
                    speak("Let's play the game...! ")
                    speak("What is your name?")
                    name =str(input("Type your name: "))
                    speak("Welcome",name,"to this adventure!")
                    print("Welcome", name, "to this adventure!")

                    speak("You are on a dirt road, it has come to an end and you can go left or right. Which way would you like to go? ")
                    answer = input( "You are on a dirt road, it has come to an end and you can go left or right. Which way would you like to go? \n")

                    if answer == "left":
                        speak("You come to a river, you can walk around it or swim accross? Type walk to walk around and swim to swim accross: ")
                        answer = input("You come to a river, you can walk around it or swim accross? Type walk to walk around and swim to swim accross: ")

                        if answer == "swim":
                            speak("You swam acrross and were eaten by an alligator.")
                            print("You swam acrross and were eaten by an alligator.")
                        elif answer == "walk":
                            speak("You walked for many miles, ran out of water and you lost the game.")
                            print("You walked for many miles, ran out of water and you lost the game.")
                        else:
                            speak("Ohuh.., That's not correct answer")
                            print('Not a valid option. You lose.')

                    elif answer == "right":
                        speak("You come to a bridge, it looks wobbly, do you want to cross it or head back (cross/back)? ")
                        answer = input("You come to a bridge, it looks wobbly, do you want to cross it or head back (cross/back)? ")

                        if answer == "back":
                            speak("You go back and lose.")
                            print("You go back and lose.")
                        elif answer == "cross":
                            speak("You cross the bridge and meet a stranger. Do you talk to them (yes/no)? ")
                            answer = input("You cross the bridge and meet a stranger. Do you talk to them (yes/no)? ")

                            if answer == "yes":
                                speak("You talk to the stanger and they give you gold. You WIN!")
                                print("You talk to the stanger and they give you gold. You WIN!")
                            elif answer == "no":
                                speak("You ignore the stranger and they are offended and you lose.")
                                print("You ignore the stranger and they are offended and you lose.")
                            else:
                                speak("Ohuh.., Chose correct answer")
                                print('Not a valid option. You lose.')
                        else:
                            speak("Ohuh.., Chose correct answer")
                            print('Not a valid option. You lose.')

                    else:
                        speak("Ohuh.., Chose correct answer")
                        print('Not a valid option. You lose.')

                    print("Thank you for trying", name) 


            elif 'quit game' in query:
                break                      
