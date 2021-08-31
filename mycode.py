import board
import digitalio
import time

led = digitalio.DigitalInOut(board.LED)
led.direction = digitalio.Direction.OUTPUT

ramp_time = 1  # Time to ramp up, in seconds
period = 0.01  # Time per cycle, in seconds
step = period / ramp_time  # how much to increment/reduce the brightness each cycle

#weak-short snoting

while True:
    brightness = 0  # Start off
    while brightness < 0.5:
        T_on = brightness * period
        T_off = period - T_on
        led.value = True
        time.sleep(T_on)
        led.value = False
        time.sleep(T_off)
        brightness += step
    while brightness > 0:
        T_on = brightness * period
        T_off = period - T_on
        led.value = False
        time.sleep(T_off)
        led.value = True
        time.sleep(T_on)
        brightness -= step
    brightness = 0

    ramp_time = 1.8  # Time to ramp up, in seconds
    period = 0.01  # Time per cycle, in seconds
    step = period / ramp_time  # how much to increment the brightness each cycle

#stronger-longer snoring
    while brightness < 1:
        T_on = brightness * period
        T_off = period - T_on
        led.value = True
        time.sleep(T_on)
        led.value = False
        time.sleep(T_off)
        brightness += step
    brightness = 1
    while brightness > 0:
        T_on = brightness * period
        T_off = period - T_on
        led.value = False
        time.sleep(T_off)
        led.value = True
        time.sleep(T_on)
        brightness -= step

