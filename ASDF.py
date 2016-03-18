import time
import sensors
import pyupm_i2clcd as lcd
import pyupm_ttp223 as ttp223
import paho.mqtt.client as mqtt

touch = ttp223.TTP223(7)
display = lcd.Jhd1313m1(0, 0x3E, 0x62)
mqttc = mqtt.Client("zone_2")
mqttc.connect("10.43.28.194")
regSpaces = 17
avSpaces = regSpaces

def on_connect(client, userdata, flags, rc):
    client.subscribe("zone_2")

def on_message(client, userdata, message):
    available -= 1
    sensors.displayUpdate(display, avSpaces, regSpaces)

mqttc.on_connect = on_connect
mqttc.on_message = on_message

while(True):
    print sensors.doubleTouchPulse(touch) 
    if sensors.doubleTouchPulse(touch):
        avSpaces +=1
        mqttc.publish("zone_1", "zone_2")
        sensors.displayUpdate(display, avSpaces, regSpaces)
