# This file is executed on every boot (including wake-boot from deepsleep)
import time
from umqttsimple import MQTTClient
import ubinascii
import machine
import micropython
import network
import esp
esp.osdebug(None)
import gc
gc.collect()

ssid = 'chev akil'
password = 'joubir123'
mqtt_server = '172.20.10.13'
#EXAMPLE IP ADDRESS
#mqtt_server = '192.168.1.144'
client_id = ubinascii.hexlify(machine.unique_id())

topic_sub1=b"led1"
topic_sub2=b"led2"
topic_sub3=b"led3"
topic_sub4=b"led4"

station = network.WLAN(network.STA_IF)

station.active(True)
station.connect(ssid, password)

while station.isconnected() == False:
  pass

print('Connection successful')
print(station.ifconfig())

#import webrepl
#webrepl.start()
