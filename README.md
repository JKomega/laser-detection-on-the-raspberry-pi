# laser-detection-on-the-raspberry-pi
This code both runs the  photocells, which detect brightness, and the code which uses the brightness data to detect when a laser beam, hitting the photocell, has been broken.

#  -laser_senssor.py
    this file controls the first laser sensor. The program works by increasing a variable, count, while a capacitor is charging and ends    the while loop, and the incrementing of the variable, when the capacitor hits about 3/4 its capacitence. For this reason if you use a larger capacitence capacitor the value of the variable count will be proportionally larger than it would have been with a smaller capacitence capacitor.
