import time
import pyupm_ttp223 as ttp223
import pyupm_servo as servo
import pyupm_grove as grove


gServo = servo.ES08A(5)
button = grove.GroveButton(6)
touch = ttp223.TTP223(0)

def checkTouchPulse(touch):
    if touch.isPressed():
        while True:
            if not touch.isPressed():
                return True
    return False

def doubleTouchPulse(touch):
    while True:
        if checkTouchPulse(touch):
            while True:
                if checkTouchPulse(touch):
                    return True

while(True):
    if button.value() == 1:
        gServo.setAngle(90)
        time.sleep(1)
        gServo.setAngle(0)

    if doubleTouchPulse(touch):
        print "Yey"
