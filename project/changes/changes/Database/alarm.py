import os
from MySQLdb import Time
from playsound import playsound
import datetime

ext_time= open('data.txt','rt')
time=ext_time.read()
Time-str(time)

del_time=open('data.txt','r+')
del_time.truncate(0)
del_time.close

def Ring(time):

    time_to_set=str(time)
    time_now=time_to_set.replace("veronica","")
    time_now=time_to_set.replace("set alarm for","")
    time_now=time_to_set.replace("alarm","")
    time_now=time_to_set.replace("set","")
    time_now=time_to_set.replace("for","")
    time_now=time_to_set.replace("and",":")

    Alarm_time=str(time_now)
    print(Alarm_time)

    while True:
        current_time=datetime.datetime.now().strftime("%H:%M")
        if current_time==Alarm_time:
            print("Wake up")
            playsound("")
        elif current_time>Alarm_time:
            break    
     

