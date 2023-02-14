# Myles Wilson
# 02-13-2023
#
# You will need:
# https://github.com/adafruit/Adafruit_CircuitPython_CircuitPlayground
#
# Thanks for for the help, https://learn.adafruit.com/.
#
# code.py

import time
from adafruit_circuitplayground import cp

# Color variables.
RED = (10, 0, 0)
GREEN = (0, 10, 0)
BLUE = (0, 0, 10)
LED_OFF = (0, 0, 0)

# Value to change tone by.
TONE_ARITHMETIC = 0


# Color handling and button timing for button_press.
def led_sec(ledclr):
    cp.pixels.fill(ledclr)
    time.sleep(0.1)
    cp.pixels.fill(LED_OFF)


# Color handling for touch.
# Lights will come on depending on what was passed
# in from the while loop. Always will be green.
def color_press(lednum):
    cp.pixels[lednum] = GREEN
    cp.pixels[lednum] = LED_OFF


# Handles tone changes.
# Blue for lower tones, red for higher tones.
def button_press(button, i):
    if button == "A":
        print("A button pressed.")
        led_sec(BLUE)
        i = i - 50
    elif button == "B":
        print("B button pressed.")
        led_sec(RED)
        i = i + 50
    return i


# Plays music via user input. Generates tones on-the-fly.
# Tone modification can be done via the 'A' and 'B' buttons.
while True:

    # Anything with 'touch' handles the keyboard input.
    # Anything with 'button' handles tone change input.
    if cp.touch_A1:
        cp.start_tone(200 + TONE_ARITHMETIC)
        print("A1 pressed.")
        color_press(6)
    elif cp.touch_A2:
        cp.start_tone(250 + TONE_ARITHMETIC)
        print("A2 pressed.")
        color_press(8)
    elif cp.touch_A3:
        cp.start_tone(300 + TONE_ARITHMETIC)
        print("A3 pressed.")
        color_press(9)
    elif cp.touch_A4:
        cp.start_tone(350 + TONE_ARITHMETIC)
        print("A4 pressed.")
        color_press(0)
    elif cp.touch_A5:
        cp.start_tone(400 + TONE_ARITHMETIC)
        print("A5 pressed.")
        color_press(1)
    elif cp.touch_A6:
        cp.start_tone(450 + TONE_ARITHMETIC)
        print("A6 pressed.")
        color_press(3)
    elif cp.touch_A7:
        cp.start_tone(500 + TONE_ARITHMETIC)
        print("A7 pressed.")
        color_press(4)
    elif cp.button_a:
        TONE_ARITHMETIC = button_press("A", TONE_ARITHMETIC)
        print("TONE_ARITHMETIC NOW: ", TONE_ARITHMETIC)
        cp.start_tone(200 + TONE_ARITHMETIC)
        time.sleep(0.5)
    elif cp.button_b:
        TONE_ARITHMETIC = button_press("B", TONE_ARITHMETIC)
        print("TONE_ARITHMETIC NOW: ", TONE_ARITHMETIC)
        cp.start_tone(200 + TONE_ARITHMETIC)
        time.sleep(0.5)
    else:
        cp.stop_tone()
