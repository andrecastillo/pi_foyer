# Import required Python libraries
from __future__ import division
import RPi.GPIO as GPIO
import time
import subprocess
import datetime

# Use BCM GPIO references
# instead of physical pin numbers
GPIO.setmode(GPIO.BCM)

# Define GPIO to use on Pi for motion sensor
GPIO_PIR = 4

# Set pin as input
GPIO.setup(GPIO_PIR,GPIO.IN)

# My averaging array
sensor_state_average = []

# Movement rate variable
movement_rate = 33

# Function to let the PIR sensor settle before starting
def settlePir():
  print "Waiting for the PIR to settle"
  # Loop until PIR output is 0
  while GPIO.input(GPIO_PIR) == 1:
    # no reason to print anything here
    print "  Waiting"

  print "  Ready"
  return
# end func

# Function to turn monitor on
def turnMonitorOn():
  # There's motion, turn on monitor
  subprocess.call("./turnmonitor_on.sh")
  return
# end func

# Function to turn monitor on
def turnMonitorOff():
  # There's no motion, turn off monitor
  subprocess.call("./turnmonitor_off.sh")
  return
# end func

# Heart of the script
# Quits with CTRL-C
try:

  settlePir()
   
  # Loop... FOREVER...Ever...ever...ver..er.r
  while True :
  
    if GPIO.input(GPIO_PIR) == 1:
      # print "monitor on" 
      turnMonitorOn() 
      with open("log.txt", "a") as logfile:
        logfile.write("Monitor On" + str(datetime.datetime.now()) + "\n")
      del sensor_state_average[:] 
      sensor_state_average.append(1)
      while (sum(sensor_state_average) / len(sensor_state_average)) * 100 >= 13:
        # Stay here until there's no more motion
        # print "calculation"
        # print (sum(sensor_state_average) / len(sensor_state_average)) * 100
        time.sleep(1)
        sensor_state_average.append(GPIO.input(GPIO_PIR))
        if len(sensor_state_average) > 20:
          del sensor_state_average[:] 
          sensor_state_average.append(1)
          sensor_state_average.append(1)
        # print "Motion"
        # print GPIO.input(GPIO_PIR)
        # print sensor_state_average
    else:
      # print "monitor off"
      turnMonitorOff()
      del sensor_state_average[:] 
      sensor_state_average.append(0)
      while (sum(sensor_state_average) / len(sensor_state_average)) * 100 <= 13:
        # Stay here until there's motion
        # print "calculation"
        # print (sum(sensor_state_average) / len(sensor_state_average)) * 100
        time.sleep(1)
        sensor_state_average.append(GPIO.input(GPIO_PIR))
        if len(sensor_state_average) > 20:
          del sensor_state_average[:] 
          sensor_state_average.append(0)
          sensor_state_average.append(0)
        # print "Motion"
        # print GPIO.input(GPIO_PIR)
        # print sensor_state_average

    # Wait for 10 milliseconds
    time.sleep(0.01)      
      
except KeyboardInterrupt:
  print "  Quit" 
  # Reset GPIO settings
  GPIO.cleanup()
