# Kindle Page Turner

**Documentation still ongoing, but all required files are in the repo**

The code in this repository, along with the physical components outlined in the [Bill of Materials](####Bill-of-Materials)

The goal of this project is to turn the pages of a kindle using external buttons, for when the kindle is in a stand. Navigating the user interface of the kindle is outside the capabilities of this project.

This will be done with a kindle, a 3D-printed case, a Raspberry Pi Pico, a pair of servo motors, and some external buttons.

## Instructions

### Hardware

#### Bill of Materials
Item # | Quantity | Part # | Part Name                                                                         | Description
------:|---------:|-------:|:----------------------------------------------------------------------------------|-------------
1      | 1        | G0910  | [Kindle](https://www.amazon.co.uk/dp/B07FQ4XCR1)                                  | The 10th Generation Kindle e-reader
2      | 1        | N/A    | [kindle_holder_and_servo_housing.stl](./stls/kindle_holder_and_servo_housing.stl) | A case for the Kindle
3      | 1        | N/A    | [pico_housing.stl](./stls/pico_housing.stl)                                       | The housing for the Raspberry Pi Pico at the back of the case
4      | 1        | N/A    | [pico_cover.stl](./stls/pico_cover.stl)                                           | A cover for the Raspberry Pi Pico Housing, to keep wires contained
5      | 1        | N/A    | [servo_horn_sheaths.stl](./stls/servo_horn_sheaths.stl)                           | For attaching stylus tips pads to the servo motors
6      | 2        | N/A    | [Stylus Pen Tips](https://www.ebay.ie/itm/174215638532)                           | Capacitive stylus tips for the touch screen
7      | 2        | SG90   | [SG90 Servo Motor](https://www.ebay.ie/itm/373323581713)                          | Servo motors for moving the stylus tips
8      | 1        | SCO915 | [Raspberry Pi Pico](https://www.raspberrypi.org/products/raspberry-pi-pico/)      | Raspberry Pi Pico Microcontroller
9      | 1        | N/A    | Micro-USB cable                                                                   | A power cable for the Raspberry Pi Pico
10     | 1        | N/A    | [Tablet holder](https://www.amazon.co.uk/gp/product/B074GNPSC7/)                  | **Optional:** Tablet holder for positioning the kindle at a comfortable height hands-free
11     | 6        | N/A    | [Wires](https://www.ebay.ie/itm/232901601951)                                     | Lengths of wire, to your preference (I used over 4 m of wire)
12     | 2        | N/A    | [Buttons](https://www.ebay.ie/itm/224192810260) or [Key Switches](https://splitkb.com/collections/switches-and-keycaps) | Buttons or Switches to push when wanting to turn the page on the Kindle — I use light-weight low-profile choc switches

#### Tools
- Soldering Iron
- Solder Wire
- 3D Printer/ 3D Printing Service/ or some arts and crafts to mimic [the case and parts](./stls/) above
- Scissors/ wire cutter
- **Optional:** wire stripper

#### 3D Printing
I recommend 3D printing the stl files at the following settings:
### Filament
PLA or similar
### Nozzle Diameter
0.4 mm or smaller
### Layer Height
0.2 mm or less
### Infill
20% or more
### Supports
Off

### Software
I recommend following [this article](https://www.twilio.com/blog/programming-raspberry-pi-pico-microcontroller-micropython) on how to install micropython and transfer files onto the Raspberry Pi Pico.
If you copy [main.py](./main.py) onto the Raspberry Pi Pico, after installing micropython and setting up the hardware, it should allow buttons to turn the pages of the kindle.


