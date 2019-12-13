import RPi.GPIO as GPIO
import time
 
GPIO.setwarnings(False)
# doing this first, since we're using a while True.
GPIO.cleanup()

GPIO.setmode(GPIO.BCM)
TRIG = 5  #GPO number
ECHO = 6

GREEN = 13 #make sure lights correlates with pin
YELLOW = 19
RED = 26

GPIO.setup(TRIG,GPIO.OUT)
GPIO.setup(ECHO,GPIO.IN)

GPIO.setup(GREEN,GPIO.OUT)
GPIO.setup(YELLOW,GPIO.OUT)
GPIO.setup(RED,GPIO.OUT)


def green_light():
    GPIO.output(GREEN, GPIO.HIGH)
    GPIO.output(YELLOW, GPIO.LOW)
    GPIO.output(RED, GPIO.LOW)

def yellow_light():
    GPIO.output(GREEN, GPIO.LOW)
    GPIO.output(YELLOW, GPIO.HIGH)
    GPIO.output(RED, GPIO.LOW)

def red_light():
    GPIO.output(GREEN, GPIO.LOW)
    GPIO.output(YELLOW, GPIO.LOW)
    GPIO.output(RED, GPIO.HIGH)


def get_distance():


    GPIO.output(TRIG, True)
    time.sleep(0.00001)
    GPIO.output(TRIG, False)

    while GPIO.input(ECHO) == False:
        start = time.time()

    while GPIO.input(ECHO) == True:
        end = time.time()

    sig_time = end-start

    #CM:
    #distance = sig_time / 0.000058
    #print('Distance: {} centimeters'.format(distance))
    #inches:
    distance = sig_time / 0.000148
    #print('Distance: {} inches'.format(distance))

    return distance

try:
    # Where the magic happens.
    while True:
        distance = get_distance()
        time.sleep(0.05)
        #print(distance)
        print('Distance: {d:1.2f} Inches'.format(d=distance))
        # This statement will activate green light if distance is greater than or equal to value
        if distance >= 36:
            green_light()
        # Activates yellow light if value is less than distance but greater than another value
        elif 36 > distance > 12:
            yellow_light()
        # Activates red light if distance is less than or equal to value
        elif distance <= 12:
            red_light()
        # Change the values and test what it does
            
except KeyboardInterrupt:
    pass
finally:
    GPIO.cleanup()            
            
    
