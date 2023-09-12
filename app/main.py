from sense_hat import SenseHat
import time
from random import randint

sense = SenseHat()
white = (128, 128, 128)
red = (128,0,0)
off = (0,0,0)

def humidity():
    sense.show_message("Humidity: "+str(round(sense.humidity,1))+"%",
                       text_colour=white,
                       back_colour=off,
                       scroll_speed=0.05)


def pressure():
        sense.show_message("Pressure: "+str(round(sense.pressure,2))+" Millibar",
                           text_colour=red,
                           back_colour=off,
                           scroll_speed=0.05)
        
def disco():
    for i in range(64):
        x = randint(0,7)
        y = randint(0,7)
        z = randint(0,7)
        r = randint(0,255)
        g = randint(0,255)
        b = randint(0,255)
        
        sense.set_pixel(x, y, (r, g, b))
        time.sleep(0.1)