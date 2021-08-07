from machine import Pin
from machine import PWM
from utime import sleep, sleep_ms

# buttons_on and _off will later decide if the pages moving backwards or forwards
# for now the LED is used as a stand-in for the servo motors - before they arrive
right_button = Pin(15,Pin.IN,Pin.PULL_DOWN)
left_button = Pin(14,Pin.IN,Pin.PULL_DOWN)
right_servo = PWM(Pin(17))
left_servo = PWM(Pin(16))
led = Pin(25, Pin.OUT)

# blink led to show power on
led.on()
sleep(1)
led.off()

# define the frequencies used for the servo motors
frequency = 50
right_servo.freq(frequency)
left_servo.freq(frequency)

# constantly wait for input, and toggle led accordingly
while True:
    if right_button.value():
        right_servo.duty_ns(500000) # move servo to screen 
        sleep_ms(200) # wait for tap to register
        right_servo.duty_ns(1300000) # re-home servo
        sleep_ms(200) # wait for re-home
    elif left_button.value():
        left_servo.duty_ns(2500000) # move servo to screen
        sleep_ms(200) # wait for tap to register
        left_servo.duty_ns(1600000) # re-home servo
        sleep_ms(200) # wait for re-home

