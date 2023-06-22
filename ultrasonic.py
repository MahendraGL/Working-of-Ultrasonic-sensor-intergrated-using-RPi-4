import RPi.GPIO as GPIO
import time 
GPIO.setwarnings(False)

GPIO.setmode(GPIO.BOARD)

trigpin=40
echopin=38
LED=36

GPIO.setup(trigpin,GPIO.OUT)
GPIO.setup(echopin,GPIO.IN)
GPIO.setup(LED,GPIO.OUT)

try:
    while True:
        
        GPIO.output(trigpin,0)
        time.sleep(0.2)
        GPIO.output(trigpin,1)
        time.sleep(10E-6)
        GPIO.output(trigpin,0)
        
        while GPIO.input(echopin)==0:
            starttime=time.time()
            pass
        
        while GPIO.input(echopin)==1:
            endtime=time.time()
            pass
        
        t_time=endtime-starttime
        distance=t_time*17510
        distance=round(distance,2)
        print("Distance in cm is: ",distance)
        time.sleep(0.2)
        
        if distance<15:
            GPIO.output(LED,0)
            print("Something detected within 15cm: ")
        else:
            GPIO.output(LED,1)
            
            
except KeyboardInterrupt:
    GPIO.cleanup()
    print('DONE')