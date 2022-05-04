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

#setup wifi connection and broker IP address
ssid = 'wifi_name'
password = 'password'
mqtt_server = '172.20.10.13'
client_id = ubinascii.hexlify(machine.unique_id())

#topics to subscribe to
topic_sub1=b"led1"
topic_sub2=b"led2"
topic_sub3=b"led3"
topic_sub4=b"led4"

station = network.WLAN(network.STA_IF)

station.active(True)
station.connect(ssid, password)

#testing ESP32 wifi connection
while station.isconnected() == False:
  pass

print('Connection successful')
print(station.ifconfig())

#import webrepl
#webrepl.start()
