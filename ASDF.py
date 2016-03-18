import time
import pyupm_servo as servo
import pyupm_grove as grove


gServo = servo.ES08A(5)
button = grove.GroveButton(6)


while(True):
    if button.value() == 1:
        gServo.setAngle(90)
        time.sleep(1)
        gServo.setAngle(-90)
