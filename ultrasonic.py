#Import nessesary files
import RPi.GPIO as GPIO
import time 
GPIO.setwarnings(False)

#GPIO is set to board numbering mode
GPIO.setmode(GPIO.BOARD)

trigpin=40
echopin=38
LED=36

#Set the GPIO pins as input and/or output as per requirement
GPIO.setup(trigpin,GPIO.OUT)
GPIO.setup(echopin,GPIO.IN)
GPIO.setup(LED,GPIO.OUT)

try:
    while True:

        #Set the triggerpin for 10 microseconds
        GPIO.output(trigpin,0)
        time.sleep(0.2)
        GPIO.output(trigpin,1)
        time.sleep(10E-6)
        GPIO.output(trigpin,0)

        #Measure the travel_time from echopin
        while GPIO.input(echopin)==0:
            starttime=time.time()
            pass
        
        while GPIO.input(echopin)==1:
            endtime=time.time()
            pass
        
        t_time=endtime-starttime

        #Calculate the distance from the measured time.
        distance=t_time*17510
        distance=round(distance,2)
        print("Distance in cm is: ",distance)
        time.sleep(0.2)

        #Glow LED for any condition depending on the distance.
        if distance<15:
            GPIO.output(LED,0)
            print("Something detected within 15cm: ")
        else:
            GPIO.output(LED,1)
            
            
except KeyboardInterrupt:
    GPIO.cleanup()
    print('DONE')
