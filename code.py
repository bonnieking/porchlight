import board
import digitalio
import neopixel
import time

pixels = neopixel.NeoPixel(board.NEOPIXEL, 10, brightness=.1)
pixels.fill((0, 0, 0))
pixels.show()

LED_PIN = board.D13  # Pin number for the board's built in LED.
PIR_PIN = board.A4   # Pin number connected to PIR sensor output wire.

# Setup digital input for PIR sensor:
pir = digitalio.DigitalInOut(PIR_PIN)
pir.direction = digitalio.Direction.INPUT

# Setup digital output for LED:
led = digitalio.DigitalInOut(LED_PIN)
led.direction = digitalio.Direction.OUTPUT

def wheel(pos):
    # Input a value 0 to 255 to get a color value from green to red
    if pos < 85:
        return (int(pos * 3), int(255 - (pos * 3)), 0)
    elif pos < 170:
        pos -= 85
        return (int(255 - (pos * 3)), 0, int(pos * 3))
    else:
        pos -= 170
        return (0, int(pos * 3), int(255 - pos * 3))


def change(pos):
    for i in range(len(pixels)):
        pixels[i] = wheel(pos)
        pixels.show()


color = 30
change(color)

while True:
    if pir.value == True:
        #print('Motion detected!')
        if color > 235:
            color = 195
        else:
             color += 20
        change(color)
    else:
        led.value = False
        #print('Motion ended!')
        if color < 20:
            color = 10
        else:
            color -= 20
        change(color)
