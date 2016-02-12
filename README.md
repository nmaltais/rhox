# IBM FAU Hackathon
This is an IoT project named LightUp aiming to introduce to FAU Hackathon event an example as for how to build an IoT application using.
The resulting application is a small mobile web page that allows the user to turn-on and turn-off an electronic device from anywhere using his smartphone.
Here is the architecture overview of the application:

![alt text](./images/lightup.png "Lightup architecture")

# Stuffs needed for building project
## Hardware:
1. Raspberry Pi 2 / B+.
2. USB wifi dongle
3. USB keyboard and mouse.
4. HDMI monitor and cable.
5. Micro USB power adapter (smartphone charger).
6. PIR motion sensor.
7. Male-female and male-male jumpers.
8. Breadboard.
9. BC547 transistor.
10. 5V SPDT relay and 1n4001 diode.
11. LED and 220Ohm resistor.

## Software:
1. Raspbian OS
2. Python
3. CloudFoundry cli

## Circuit wiring up:
Below is the detailed diagram as illustrates how to connect the parts together on the breadboard and with the Pi.

![alt text](./images/circuit.jpg "Circuit wire up")

## Basic steps to setup the environment:
1. Setup your Rapberry pi
- Format your SD or Micoro SD card being used for your Pi
- Download Raspbian OS or NOOBS from Raspberry pi website and copy it over to your card
https://www.raspberrypi.org/downloads/
You may need a monitor and
2. Register you Pi to Bluemix
You can use this recipes to register your Pi to Bluemix.
https://developer.ibm.com/iotfoundation/recipes/raspberry-pi/
Remember to write down the following necessary information for connecting your code with Bluemix iotf later:

organization = ""
deviceType = ""
deviceId = ""
authMethod = "token"
authToken = ""

3. Run your client code

4. Deploy your server code to Bluemix

5. Try it out

More instructions about how to work with Python iotf library can be found here:
https://docs.internetofthings.ibmcloud.com/libraries/python.html
