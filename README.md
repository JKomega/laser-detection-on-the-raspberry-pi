# laser-detection-on-the-raspberry-pi
   This code both runs the  photocells, which detect brightness, and the code which uses the brightness data to detect when a laser beam, hitting the photocell, has been broken.

#  -laser_sensor.py
   this file controls the first laser sensor. The program works by increasing a variable, count, while a capacitor is charging and ends    the while loop, and the incrementing of the variable, when the capacitor hits about 3/4 its capacitence. For this reason if you use a larger capacitence capacitor the value of the variable count will be proportionally larger than it would have been with a smaller capacitence capacitor.
   
#  -laser_sensor2.py
   this file works the same way as laser_sensor.py but is used for the second photocell.

#  -main.py
  this file runs the program which detects if the photocell's readings change dramatically; this likely means the laser beam, hitting    the photocell, has been crossed. In the code the Raspberry Pi is polling for responses from a GPIO pin connected to a photocell. If the values fall below a baseline, which is the value output by the photcell when it is hit by the laser, then a varible crossed increases.
To poll values from the photocell faster the program uses two threads, one for each photocell. Currently, I need to find ways to stop the 
threads when there is not a need to be polling for values.
