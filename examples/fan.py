''' THIS SCRIPT CONTROL Orange Pi FAN FOR H3/5 BASED BOARD
    Create a CRON job to make it run as service, edit CRON as Super User
    to give permission for file control GPIO. 
'''

# Used PIN 29 (PA7) 

import subprocess
import logging
import logging.handlers
from time import sleep
from pyA20.gpio import gpio
from pyA20.gpio import port

myLogger = logging.getLogger("SystemFan")
myLogger.setLevel(logging.INFO)

handler = logging.handlers.SysLogHandler(address = "/dev/log")

myLogger.addHandler(handler)

outputPort = port.PA7

fanOn = False

### Return Armbian CPU temperature
def get_temp():
        sp = subprocess
        temp_zone0 = ["cat","/sys/devices/virtual/thermal/thermal_zone0/temp"]

        command = sp.Popen(temp_zone0, stdout=sp.PIPE)
        output, err = command.communicate()
        temp = int(output)/1000

        return temp

#Change fan state if temp is over threshold
def fan_state(temp):
        global fanOn
        if temp > 60:
    	        if fanOn == False:
        	        #Change output state
        	        gpio.output(outputPort, gpio.HIGH)
		        fanOn = True
                
                #Debug line
        	myLogger.info("System Fan - CPU temp: " + str(temp) + " deg C" + " - Fan On!")
        	#Turn on fan at least 60 seconds
        	sleep(60)
        else:
    	        if fanOn == True:
        	        #Turn off fan
        	        gpio.output(outputPort, gpio.LOW)
		        fanOn = False

                        #Debug line
        	        myLogger.info("System Fan - CPU temp: " + str(temp) + " deg C" + " - Fan Off!")

#Work as service, every 2 seconds
def main():
        myLogger.info("System Fan - Loop routine started.")
        gpio.output(outputPort, gpio.LOW)

        while True:
                fan_state(get_temp())
                sleep(2)

gpio.init()
gpio.setcfg(outputPort, gpio.OUTPUT)

main()