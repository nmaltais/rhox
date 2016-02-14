#####################################
# Client component for LightUp IoT project.
# This will be run on Raspberry Pi and listen to the commands from Server component to control
# appliances connected to the system (turn on/off)
####################################
import time
import sys
import pprint
import uuid
import json
from uuid import getnode as get_mac

import RPi.GPIO as GPIO
import time
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(3,GPIO.OUT,initial=GPIO.LOW)
GPIO.setup(7,GPIO.IN,pull_up_down=GPIO.PUD_UP)
GPIO.setup(11,GPIO.IN)
ls='OFF'

try:
	import ibmiotf.application
	import ibmiotf.device
except ImportError:
	# This part is only required to run the sample from within the samples
	# directory when the module itself is not installed.
	# If you have the module installed, just use "import ibmiotf.application" & "import ibmiotf.device"
	import os
	import inspect
	cmd_subfolder = os.path.realpath(os.path.abspath(os.path.join(os.path.split(inspect.getfile( inspect.currentframe() ))[0],"../../src")))
	if cmd_subfolder not in sys.path:
		sys.path.insert(0, cmd_subfolder)
	import ibmiotf.application
	import ibmiotf.device

def myAppEventCallback(event):
	print("Received live data from %s (%s) sent at %s: hello=%s x=%s" % (event.deviceId, event.deviceType, event.timestamp.strftime("%H:%M:%S"), data['hello'], data['x']))

def myCommandCallback(cmd):
  print("Command received: %s" % json.dumps(cmd.data))
  if cmd.command == "on":
    print("Turning Light ON")
    GPIO.output(3,1)
  elif cmd.command == "off":
    print("Turning Light OFF")
    GPIO.output(3,0)
print
######################################################
#Update this section to match your environment setting
######################################################
organization = "1qdfa9"
deviceType = "RaspberryPi"
deviceId = "RaspberryPi-Lightup"
authMethod = "token"
authToken = "y+q@!u9h@YesuGV1iJ"

# Initialize the device client.
try:
	deviceOptions = {"org": organization, "type": deviceType, "id": deviceId, "auth-method": authMethod, "auth-token": authToken}
	deviceCli = ibmiotf.device.Client(deviceOptions)
except Exception as e:
	print(str(e))
	sys.exit()

deviceCli.connect()
deviceCli.commandCallback = myCommandCallback

try:
        while(1):
                lightStatus=GPIO.input(7)
                if lightStatus==0:
                        ls='ON'
                else:
                        ls='OFF'
                intruder=GPIO.input(11)
                data = { 'LightStatus': ls, 'Intruder': intruder}
                deviceCli.publishEvent(deviceType, deviceId, "status","json", data)

                time.sleep(1)
except KeyboardInterrupt:
        print "Cleaning up ..."
        GPIO.cleanup()
# Disconnect the device and application from the cloud
deviceCli.disconnect()
