import time
import sensors
import pyupm_i2clcd as lcd
import pyupm_ttp223 as ttp223
import pyupm_servo as servo
import pyupm_grove as grove
import paho.mqtt.client as mqtt


gServo = servo.ES08A(5)
button = grove.GroveButton(6)
touch = ttp223.TTP223(7)
display = lcd.Jhd1313m1(0, 0x3E, 0x62)
mqttc = mqtt.Client("zone_2")
mqttc.connect("10.43.28.194")
regSpaces = 17
available = 17


def on_connect(client, userdata, flags, rc):
    client.subscribe("zone_1")

def on_message(client, userdata, message):
    available -= 1
    displayUpdate(display, avSpaces, regSpaces)

mqttc.on_connect = on_connect
mqttc.on_message = on_message

while(True)
    if doubleTouchPulse(touch):
        avSpaces +=1
        mqttc.publish("zone_1", "zone_2")
        displayUpdate(display, avSpaces, regSpaces)
