from machine import Pin
from utime import sleep

# buttons_on and _off will later decide if the pages moving backwards or forwards
# for now the LED is used as a stand-in for the servo motors - before they arrive
button_on = Pin(14,Pin.IN,Pin.PULL_DOWN)
button_off = Pin(15,Pin.IN,Pin.PULL_DOWN)
led = Pin(25, Pin.OUT)

# light led immediately to show power on
led.on()

# constantly wait for input comma and toggle led accordingly
while True:
    if button_off.value():
        led.off()
    elif button_on.value():
        led.on()

    # sleep as a lazy form of debounce
    sleep(0.15)

