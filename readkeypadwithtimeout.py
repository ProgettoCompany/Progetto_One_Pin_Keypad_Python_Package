# readkeypadwithtimeout example sketch, details can be found here:
# https://www.instructables.com/id/Meet-One-Pin-Keypad/

import time
from onepinkeypad import OnePinKeypad

# Define Analog Pin:
pin = 0

# Variable to store button being pressed:
key_value = '\0'

# Create a keypad object:
keypad = OnePinKeypad(pin)

# 5 second time limit to wait for input (in milliseconds)
timeout = 5000

# Insert your calibrated array here:
# ex: my_thresholds = [calibrated values would be here]
  
# If calibrated values are being used, use_calibrated_thresholds below:
# ex: keypad.use_calibrated_thresholds(your array name)

# This while loop runs over and over again forever:
while(True):
    # Run the read_keypad_with_timeout function to determine which button is pressed within the timeout, in milliseconds
    # Store that value in the variable keyValue
    # If no timeout is desired, pass the NO_TIMEOUT constant as a parameter to readKeypadWithTimeout
    key_value = keypad.read_keypad_with_timeout(5000)

    # Print the key being pressed to the console
    print("You pressed: " + str(key_value))
    time.sleep(0.01)
