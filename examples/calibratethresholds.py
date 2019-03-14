# calibrate_thresholds example sketch, details can be found here:
# https://www.instructables.com/id/Meet-One-Pin-Keypad/

import time
import onepinkeypad.onepinkeypad as opk

# Define Analog Pin:
pin = 0

# Variable to store button being pressed:
key_value = '\0'

# Keypad button names:
buttonIDs = ['1', '2', '3', 'A', '4', '5', '6', 'B', '7', '8', '9', 'C', '*', '0', '#', 'D']

# default analog values that correspond to each button:
thresholds = [
  225,    # 1
  2116,   # 2
  3904,   # 3
  5200,   # A
  6300,   # 4
  7350,   # 5
  8450,   # 6
  9325,   # B
  10000,  # 7
  10750,  # 8
  11500,  # 9
  12100,  # C
  12550,  # *
  13100,  # 0
  13800,  # #
  14250   # D
]

new_thresholds = [0] * 16

# Create a keypad object:
keypad = opk.OnePinKeypad(pin)

def calibrate_button(button, array_index):
  tolerance = 500
  print("Press " + str(button) + ":")
  
  while (True):
    button_val = keypad.analog_read()
    if(button_val < 20000):
      calibration_check = button_val - thresholds[array_index]
      if (abs(calibration_check) <= tolerance):
        print("Passed button analog value: " + str(button_val))
        tolerance -= 1
        new_thresholds[array_index] = button_val
        print("Release the button")
        return
    time.sleep(0.01)

print("\nKeypad Calibration for Progetto One Pin Keypad Boards:")
print("Please note: for your convenience a tolerance is used ")
print("to avoid bad values from pressing the wrong button. ")
print("Unfortunately, the analog values get closer and closer")
print("together as they increase so if you press 0 instead of #")
print("the analog value will still be accepted.")
print("\nTL;DR: Press the correct button when prompted!!!\n")
time.sleep(0.5)

# less than is used because array indexing starts at 0
for button_index in range(16):
    calibrate_button(buttonIDs[button_index], button_index)
    time.sleep(1)

print("\nInsert the following line of code in your code before it loops:")
print("my_thresholds = [", end = "");
for thresholds_index in range(16):
    print (str(new_thresholds[thresholds_index]), end = ", ")

print(str(new_thresholds[15]) + "]")

print("\nNext, insert the following line of code right below the previous")
print("one in order to use the newly calibrated analog thresholds:")
print("keypad.use_calibrated_thresholds(my_thresholds)")

keypad.use_calibrated_thresholds(new_thresholds);

print("\nCalibrated value demo beginning in 5 seconds...")
print("Feel free to test out your calibrated values by pressing ")
print("any button at random, it should be printed to the Console.")
print("If a button fails, run this program again to recalibrate.")
time.sleep(5)
print("\nBegin.")

# This while loop runs over and over again forever:
while(True):
    # Run the read_keypad_with_timeout function to determine which button is pressed within the timeout, in milliseconds
    # Store that value in the variable keyValue
    # If no timeout is desired, pass the NO_TIMEOUT constant as a parameter to readKeypadWithTimeout
    key_value = keypad.read_keypad_with_timeout(keypad.NO_TIMEOUT)

    # Print the key being pressed to the console
    print("You pressed: " + str(key_value))
    time.sleep(0.01)
