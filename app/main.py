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
    set_row_color("green")



def pressure():
        sense.show_message("Pressure: "+str(round(sense.pressure,2))+" Millibar",
                           text_colour=red,
                           back_colour=off,
                           scroll_speed=0.05)
        set_row_color("blue")

        
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
def flashlight():
    for i in range(10):
        o = sense.get_orientation()
        pitch = int(o["pitch"] / 1.42)
        roll = int(o["roll"] / 1.42)
        yaw = int(o["yaw"] / 1.42)
        for x in range(8):
            for y in range(8):
                sense.set_pixel(x, y, (pitch, roll, yaw))
        time.sleep(1)
        
def temperature():
    sense.show_message(str(round(sense.temperature,1))+" Celsius", text_colour=white, back_colour=off, scroll_speed=0.05)
    set_row_color()
    
def sensor_dump():
    while True:
        print(str(round(sense.temperature,1)))
        print(str(round(sense.humidity)))
        print(str(round(sense.pressure)))
        time.sleep(3)

def set_row_color(color: str = "red"):
    RED = (255,0,0)
    GREEN = (0, 255, 0)
    BLUE = (0, 0, 255)

    if color == "red":
        for num in range(0,8):
            sense.set_pixel(num, 0, RED)
    if color == "blue":
        for num in range(0,8):
            sense.set_pixel(num, 4, BLUE)
    else:
        for num in range(0,8):
            sense.set_pixel(num, 5, GREEN)
        
        
while True:
    sense.stick.direction_up = humidity
    sense.stick.direction_down = disco
    sense.stick.direction_left = pressure
    sense.stick.direction_right = temperature
    acceleration = sense.get_accelerometer_raw()
    x = acceleration['x']
    y = acceleration['y']
    z = acceleration['z']

    x = abs(x)
    y = abs(y)
    z = abs(z)
    if x > 2 or y > 2 or z > 2:
        for i in range(2):
            sense.show_message(str(round(sense.temperature,1))+" Celsius", text_colour=white, back_colour=off, scroll_speed=0.05)
    else:
        print("Use the joystick, or shake the Pi")
        time.sleep(0.1)
    sensor_dump()