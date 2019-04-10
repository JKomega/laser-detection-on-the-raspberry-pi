from light_sensor import rc_time, pin_to_circuit
from light_sensor2 import rc_time as rc_time2, pin_to_circuit as pin_to_circuit2
from threading import Thread
import RPi.GPIO as GPIO
import time


crossed = 0

def phc1(crossed):
    while True:
        if (rc_time(pin_to_circuit) > 25):
            print(time.strftime('%a %H:%M:%S'))
            crossed += 1
	    print("phc1 crossed")
    return crossed

def phc2(crossed):
    while True:
        if (rc_time2(pin_to_circuit2) > 250):
            print(time.strftime('%a %H:%M:%S'))
            crossed += 1
            print("phc2 crossed")
    return crossed

t1 = Thread(target = phc1, args = (0, ))
t2 = Thread(target = phc2, args = (0, ))

try:
    #while True:

        #phc1(0)
	t1.start()
        #phc2(0)
	t2.start()


except KeyboardInterrupt:
    t1.join()
    t2.join()
    crossed += phc1(0) + phc2(0)
    print(crossed)
finally:
       GPIO.cleanup(pin_to_circuit)
