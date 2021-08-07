from machine import Pin
from machine import PWM
from utime import sleep, sleep_ms

# set pins for button and led
right_button = Pin(15,Pin.IN,Pin.PULL_DOWN)
left_button = Pin(14,Pin.IN,Pin.PULL_DOWN)
led = Pin(25, Pin.OUT)

# blink led to show power on
led.on()
sleep(1)
led.off()

# define the frequencies used for the servo motors
frequency = 50
right_servo.freq(frequency)
left_servo.freq(frequency)

def right_tap(screen_pos, home_pos, wait_ms):
    right_servo = PWM(Pin(17)) # right servo pin

    right_servo.duty_ns(screen_pos) # move servo to screen 
    sleep_ms(wait_ms) # wait for tap to register
    right_servo.duty_ns(home_pos) # re-home servo
    sleep_ms(wait_ms) # wait for re-home

def left_tap(screen_pos, home_pos, wait_ms):
    left_servo = PWM(Pin(16)) # left servo pin

    left_servo.duty_ns(screen_pos) # move servo to screen
    sleep_ms(wait_ms) # wait for tap to register
    left_servo.duty_ns(home_pos) # re-home servo
    sleep_ms(wait_ms) # wait for re-home

# constantly wait for input, and tap screen accordingly
while True:
    if right_button.value():
        right_tap(500000, 1300000, 200) # tap right side on right button press
    elif left_button.value():
        left_tap(2500000, 1600000, 200) # tap left side on left button press

