# Import required Python libraries
import RPi.GPIO as GPIO
import time
import subprocess

# Use BCM GPIO references
# instead of physical pin numbers
GPIO.setmode(GPIO.BCM)

# Define GPIO to use on Pi for motion sensor
GPIO_PIR = 4

print "PIR Module Test (CTRL-C to exit)"

# Set pin as input
GPIO.setup(GPIO_PIR,GPIO.IN)

Current_State = 0
Previous_State = 0

try:

  print "Waiting for PIR to settle ..."

  # Loop until PIR output is 0
  while GPIO.input(GPIO_PIR)==1:
    Current_State = 0    

  print "  Ready"
 
  # Loop until user quits with CTRL-C
  while True :
    # Read PIR state
    Current_State = GPIO.input(GPIO_PIR)
  
    if Current_State==1:
      # There's motion, turn on monitor
      subprocess.call("./turnmonitor_on.sh")

      # wait for 5 seconds before checking if there's motion again
      time.sleep(5)

    else:
      # There's no motion, turn off the monitor
      subprocess.call("./turnmonitor_off.sh")

    # Wait for 10 milliseconds
    time.sleep(0.01)      
      
except KeyboardInterrupt:
  print "  Quit" 
  # Reset GPIO settings
  GPIO.cleanup()
