# Import required Python libraries
import RPi.GPIO as GPIO
import time

# Use BCM GPIO references
# instead of physical pin numbers
GPIO.setmode(GPIO.BCM)

# Define GPIO to use on Pi for motion sensor
GPIO_PIR = 4

# Set pin as input
GPIO.setup(GPIO_PIR,GPIO.IN)

# lets watch it get ready
print "Waiting for the PIR to settle"
while GPIO.input(GPIO_PIR) == 1:
  # no reason to print anything here
  print GPIO.input(GPIO_PIR)
  time.sleep(1)
  
print "  Ready"

# now just looping to see the data we get in real time
try:

  while True :
    print GPIO.input(GPIO_PIR)
    time.sleep(1)


except KeyboardInterrupt:
  print "  Quit" 
  # Reset GPIO settings
  GPIO.cleanup()
