from machine import Pin
from machine import PWM
from utime import sleep, sleep_ms

# set pins for button and led
right_button = Pin(15,Pin.IN,Pin.PULL_DOWN)
right_servo_pin = 17
left_button = Pin(14,Pin.IN,Pin.PULL_DOWN)
left_servo_pin = 16
led = Pin(25, Pin.OUT)
frequency = 50

# blink led to show power on
led.on()
sleep(1)
led.off()

def screen_tap(servo_pin, frequency, screen_pos, home_pos, wait_ms):
    servo = PWM(Pin(servo_pin)) # set servo pin

    # define the frequencies used for the servo motors
    servo.freq(frequency)

    servo.duty_ns(screen_pos) # move servo to screen 
    sleep_ms(wait_ms) # wait for tap to register
    servo.duty_ns(home_pos) # re-home servo
    sleep_ms(wait_ms) # wait for re-home

# constantly wait for input, and tap screen accordingly
while True:
    if right_button.value():
        screen_tap(right_servo_pin, frequency, 500000, 1300000, 200)
    elif left_button.value():
        screen_tap(left_servo_pin, frequency, 2500000, 1600000, 200)

