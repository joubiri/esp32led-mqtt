from tkinter import *
from tkinter.messagebox import showinfo
import paho.mqtt.client as paho
import time 

class MQTTconnect:
	def __init__(self):
		broker="172.20.10.13"
		# broker="localhost"
		port=1883
		self.client1= paho.Client("test")
		self.client1.connect(broker,port)
		self.client1.on_publish=self.on_publish

	def senddata(self,topic,v):
		self.client1.publish(topic,v)

	def on_publish(self,client,userdata,result):
		print("data passed")
		pass

class App(Tk):
	 def __init__(self):
	 	super().__init__()
	 	self.title('ESP32 LED control')
	 	self.geometry('250x250')
	 	logo=PhotoImage(file="logo.png")
	 	self.iconphoto(True,logo)
	 	self.resizable(False, False)

class AppFrame(Frame):
	def __init__(self,container):
		super().__init__(container)
		param={'padx':5,'pady':5,'ipadx':5,'ipady':5}
		
		self.i_flag=[False]
		self.j_flag=[False]
		self.k_flag=[False]
		self.l_flag=[False]

		self.ledlabel1=Label(self, text='LED 1')
		self.ledlabel1.grid(column=0,row=0, sticky=W, **param)
		self.buttonled1=Button(self,text='Toggle LED')
		self.buttonled1['command']= lambda: [self.i_flag.__setitem__(0,self.reverseflag(self.i_flag[0])),self.send2ESP()]
		self.buttonled1.grid(column=1,row=0,sticky=W, **param)

		self.ledlabel2=Label(self, text='LED 2')
		self.ledlabel2.grid(column=0,row=1, sticky=W, **param)
		self.buttonled2=Button(self,text='Toggle LED')
		self.buttonled2['command']=lambda: [self.j_flag.__setitem__(0,self.reverseflag(self.j_flag[0])),self.send2ESP()]
		self.buttonled2.grid(column=1,row=1,sticky=W, **param)

		self.ledlabel3=Label(self, text='LED 3')
		self.ledlabel3.grid(column=0,row=2, sticky=W, **param)
		self.buttonled3=Button(self,text='Toggle LED')
		self.buttonled3['command']=lambda: [self.k_flag.__setitem__(0,self.reverseflag(self.k_flag[0])),self.send2ESP()]
		self.buttonled3.grid(column=1,row=2,sticky=W, **param)

		self.ledlabel4=Label(self, text='LED 4')
		self.ledlabel4.grid(column=0,row=3, sticky=W, **param)
		self.buttonled4=Button(self,text='Toggle LED',command=lambda: [self.l_flag.__setitem__(0,self.reverseflag(self.l_flag[0])),
		self.send2ESP()])
		self.buttonled4.grid(column=1,row=3,sticky=W, **param)

		self.grid(padx=10,pady=10,sticky=NSEW)


	def reverseflag(self, b):
		return not b

	def send2ESP(self):
		c=MQTTconnect()
		if self.i_flag[0]==True:
			print("data 'ON' sent to LED1")
			c.senddata('led1',1)
		else:
			print("data 'OFF' sent to LED1")
			c.senddata('led1',0)

		if self.j_flag[0]==True:
			print("data 'ON' sent to LED2")
			c.senddata('led2',1)
		else:
			print("data 'OFF' sent to LED2")
			c.senddata('led2',0)

		if self.k_flag[0]==True:
			print("data 'ON' sent to LED3")
			c.senddata('led3',1)
		else:
			print("data 'OFF' sent to LED3")
			c.senddata('led3',0)

		if self.l_flag[0]==True:
			print("data 'ON' sent to LED4")
			c.senddata('led4',1)
		else:
			print("data 'OFF' sent to LED4")
			c.senddata('led4',0)


if __name__== "__main__":
	app=App()
	myframe=AppFrame(app)
	app.mainloop()