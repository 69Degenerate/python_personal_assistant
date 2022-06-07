import ISS_Info
import turtle
import time


screen=turtle.Screen()
screen.setup(720,360)
screen.setworldcoordinates(-180,-90,180,90)
screen.bgpic("C:\\Users\\Amol\\Desktop\\project\\project\\vishal\\world.png")
screen.register_shape("C:\\Users\\Amol\\Desktop\\project\\project\\vishal\\iss.gif")

iss=turtle.Turtle()
iss.shape("C:\\Users\\Amol\\Desktop\\project\\project\\vishal\\iss.gif")
iss.penup()

while True:
    loc=ISS_Info.iss_current_loc()
    lat=loc['iss_position']['latitude']
    lon=loc['iss_position']['longitude']
    print("Position: \n latitude: {}, longitude: {}".format(lat,lon))
    iss.goto(float(lon),float(lat))
    time.sleep(5)