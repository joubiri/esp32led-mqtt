from machine import Pin, PWM
import time
from umqttsimple import MQTTClient
import ubinascii
import machine
import micropython
import network
import sys

#default PINS for LEDs
first_led=Pin(23, Pin.OUT)
second_led=Pin(22, Pin.OUT)
third_led=Pin(21, Pin.OUT)
fourth_led=Pin(19, Pin.OUT)

#callback function upon receiving a message
def call_back_function(topic, msg): 
     global message, top
     message = msg.decode().strip("'\n") 
     top=topic
     # print((topic, msg)) 
  
message = "" 

#initializing MQTT client 
client = MQTTClient(client_id,mqtt_server)  
client.set_callback(call_back_function) 

#establishing connection
try: 
    client.connect() 
except Exception as e: 
    machine.reset 

#subscribe to topics     
client.subscribe(topic_sub1) 
client.subscribe(topic_sub2)
client.subscribe(topic_sub3)
client.subscribe(topic_sub4)

while True: 
    try: 
        client.wait_msg()
        if top==topic_sub1:
        	if message=="1":
        		print('led 1 is ON')
        		first_led.on()
        	else:
        		print('led 1 is OFF')
        		first_led.off()

        if top==topic_sub2:
        	if message=="1":
        		print('led 2 is ON')
        		second_led.on()
        	else:
        		print('led 2 is OFF')
        		second_led.off()

        if top==topic_sub3:
        	if message=="1":
        		print('led 3 is ON')
        		third_led.on()
        	else:
        		print('led 3 is OFF')
        		third_led.off()

        if top==topic_sub4:
        	if message=="1":
        		print('led 4 is ON')
        		fourth_led.on()
        	else:
        		print('led 4 is OFF')
        		fourth_led.off()

        print("\n")
             
    except KeyboardInterrupt: 
        print('Exit.') 
        client.disconnect() 
        sys.exit()

