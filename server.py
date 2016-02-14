#####################################
# Server component for LightUp IoT project.
# This will be run in Bluemix and send controlling commands to Client component
# to control the appliances connected to the system (turn on/off)
####################################
import time
import sys
import os,json
import pprint
import uuid
from uuid import getnode as get_mac
from flask import Flask,redirect
from flask import render_template
from flask import request

vcap = json.loads(os.getenv("VCAP_SERVICES"))

try:
	import ibmiotf.application
	import ibmiotf.device
except ImportError:
	# This part is only required to run the sample from within the samples
	# directory when the module itself is not installed.
	#
	# If you have the module installed, just use "import ibmiotf.application" & "import ibmiotf.device"
	import os
	import inspect
	cmd_subfolder = os.path.realpath(os.path.abspath(os.path.join(os.path.split(inspect.getfile( inspect.currentframe() ))[0],"../../src")))
	if cmd_subfolder not in sys.path:
		sys.path.insert(0, cmd_subfolder)
	import ibmiotf.application
	import ibmiotf.device


def appEventCallback(event):
	print("%s",json.dumps(event.data))

def myStatusCallback(status):
	if status.action == "Disconnect":
		print(tableRowTemplate % (status.time.isoformat(), status.device, status.action + " " + status.clientAddr + " (" + status.reason + ")"))
	else:
		print(tableRowTemplate % (status.time.isoformat(), status.device, status.action + " " + status.clientAddr))
#####################################
#Change this setting based on your specific setup
#####################################
organization = "1eaiiu"
deviceType = "RaspberryPi"
deviceId = "RaspberryPi-Lightup"
#appId = str(uuid.uuid4())
##API TOKEN AND KEY
#authkey = "a-1qdfa9-qauu2byt5q"
#authtoken = "E?cLpBcYJ3pTfKbx?+"
# Initialize the application client.
appOptions = {
	"org": vcap["iotf-service"][0]["credentials"]["org"],
	"id": vcap["iotf-service"][0]["credentials"]["iotCredentialsIdentifier"],
	"auth-method": "apikey",
	"auth-key": vcap["iotf-service"][0]["credentials"]["apiKey"],
	"auth-token": vcap["iotf-service"][0]["credentials"]["apiToken"]
}

#appOptions = {"org": organization, "id": appId,"auth-method": "apikey", "auth-key" : authkey, "auth-token":authtoken }
	#sys.exit()

# Connect and configuration the application
# - subscribe to live data from the device we created, specifically to "greeting" events
# - use the myAppEventCallback method to process events
appCli = None
try:
	appCli = ibmiotf.application.Client(appOptions)
	appCli.connect()
    #appCli.deviceEventCallback = myCommandCallback
    #appCli.subscribeToDeviceEvents(event="status")

except Exception as e:
	print("Some problem occured: " + str(e))

app = Flask(__name__)

if os.getenv("VCAP_APP_PORT"):
    port = int(os.getenv("VCAP_APP_PORT"))
else:
	port = 8080

@app.route('/')
def hello():
    return render_template('index.html')

@app.route('/light/<command>', methods=['GET', 'POST'])
def light_route(command):
	print command
	commandData = {'command' : command}
	try:
		appCli.publishCommand(deviceType, deviceId, command, "json",commandData)
		#appCli.deviceEventCallback = appEventCallback
		#appCli.subscribeToDeviceEvents(even="status")
		#appCli.publishEvent(deviceType, deviceId, command, "json",commandData)
    #client.publishEvent("raspberrypi", deviceId, "light", "json", myData)
	except Exception as e:
		print("Error occured: " + str(e))
	return redirect("/", code=302)
if __name__ == '__main__':
	app.run(host='0.0.0.0', port=port)
