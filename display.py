# Download ssd1306
# https://github.com/micropython/micropython/blob/master/drivers/display/ssd1306.py
# and save to pyboard flash

import ssd1306
import machine
import time
import math

WIDTH = const(128)
HEIGHT = const(64)

ssd1306_scl = machine.Pin(22, machine.Pin.OUT)
ssd1306_sda = machine.Pin(21, machine.Pin.OUT)
i2c_ssd1306 = machine.I2C(scl=ssd1306_scl, sda=ssd1306_sda)

print(i2c_ssd1306.scan())
oled = ssd1306.SSD1306_I2C(WIDTH, HEIGHT, i2c_ssd1306)
oled.fill(0)

oled.text("No", 0, 0)
oled.text("OLED(ssd1306)", 0, 10)
oled.text("pyboard", 0, 20)
oled.show()


btn = machine.Pin(13, machine.Pin.IN, machine.Pin.PULL_UP)
#IR = machine.Pin(2, machine.Pin.IN)

# connections to the three IR distance sensors
# left = Pin(8, Pin.IN, Pin.PULL_DOWN)
#center = machine.Pin(2, machine.Pin.IN, machine.Pin.PULL_DOWN)
#right = machine.Pin(6, machine.Pin.IN, machine.Pin.PULL_DOWN)


def pressed(x=10):
    oled.fill(0)
    circle(x)
    
    
def not_pressed():
    oled.fill(0)
    oled.text("Not Pressed", 0, 0)
    oled.show()

def middle(x,y,r):
    oled.hline(2, 32, 128, 1)
    oled.show()
    
        
def circle(x=10):
    r = 5
    y = 32
    oled.hline(x-r, y, r*2,1)
    for i in range(1,r):
        a = int(math.sqrt(r*r-i*i))
        oled.hline(x-a, y+i, a*2, 1)
        oled.hline(x-1, y-i, a*2, 1)
    oled.show()

def terminate():
    oled.fill(0)
    oled.text("Game Over", 28,32)
    oled.show()

def start():
    oled.fill(0)
    oled.text("Click to start", 10,30)
    oled.show()

step = 8
x = 10
y = 32
game_loop = False
while True:
    start()
    if (btn.value()):
        game_loop = True
        
    while game_loop:
    
        current = btn.value()
      
        if (current):
            x+=step

        oled.fill(0)
        circle(x)
        oled.show()
        
        if x >= 123:
            x = 10
            terminate()
            time.sleep(1)
            game_loop = False
    
    

#while True:
#    if (center.value()):
    #time.sleep(1)
#        oled.invert(not center.value())
    #time.sleep(1)
    #oled.invert(0)
