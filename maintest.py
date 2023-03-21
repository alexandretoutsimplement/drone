from tkinter import *
import cv2
import threading
import socket
import pickle
import struct
import time

class Treadvideo (threading.Thread):
	def __init__(self, zonecam):
		threading.Thread.__init__(self)
		self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
		self.server_socket.bind(("127.0.0.1", 11111))
		self.server_socket.listen()
		self.zonecam=zonecam

	
	
	def run (self):
		self.continuer = True
		while self.continuer:
			drone_socket, addr = self.server_socket.accept()
			print('Connecter depuis', addr)
		
			if drone_socket:
				vid = cv2.VideoCapture(0)
				while(vid.isOpened()):
					img,frame = vid.read()
					a = pickle.dumps(frame)
					message = struct.pack("Q",len(a))+a
					drone_socket.sendall(message)
					cv2.imshow(self.zonecam,frame)
			time.sleep(0.01)

	

ACCES_DRONE = ('192.168.10.1', 8889)
nombre=30

def getresp(label):
	print("getresp")
	try: 
		client_socket.timeout(1)
		message, address=client_socket.recvfrom(1024)
	except:
		message= "Problème de connexion"
	label.config(text=message)
	
def decoller():
	global label
	message = "takeoff".encode(encoding="utf-8")
	client_socket.sendto(message, ACCES_DRONE)
	getresp(label)
def atterir():
	global label
	message = "land".encode(encoding="utf-8")
	client_socket.sendto(message, ACCES_DRONE)
	getresp(label)
def droite():
	global label
	message = "right 030".encode(encoding="utf-8")
	client_socket.sendto(message, ACCES_DRONE)
	getresp(label)
def gauche():
	global label, client_socket
	label.config(text="mouvement gauche")
	message="f'left {nombre}'".encode(encoding="utf-8")
	client_socket.sendto(message, ACCES_DRONE)
	getresp(label)
	
def avancer():
	global label
	message = "forward 30".encode(encoding="utf-8")
	client_socket.sendto(message, ACCES_DRONE)
	getresp(label)

def reculer():
	global label
	message = "back 30".encode(encoding="utf-8")
	client_socket.sendto(message, ACCES_DRONE)
	getresp(label)
	
def pivdroite():
	global label
	message = "cw 30".encode(encoding="utf-8")
	client_socket.sendto(message, ACCES_DRONE)
	getresp(label)

def pivgauche():
	global label
	message = "ccw x=030".encode()
	client_socket.sendto(message, ACCES_DRONE)
	getresp(label)

def fermeture():
	client_socket.close()
	tv.server_socket.close()
	tv.contiuer = False
	window.destroy()

window=Tk()

window.title("Manette")
window.geometry("1920x1080")

col1=100
col2=200
col3=300
col4=1620
col5=1720
col6=1820

ligne1=100
ligne2=200
ligne3=300

label= Label(window,text="")
label.place(x=810, y=0)


button_1 = Button(window, text="Décoller", command=decoller)
button_1.place(x=col2, y=ligne1)

button_2 = Button(window, text="Atterir", command=atterir)
button_2.place(x=col2, y=ligne3)

button_3 = Button(window, text="Droite", command=droite)
button_3.place(x=col3, y=ligne2)

button_4 = Button(window, text="Gauche", command=gauche)
button_4.place(x=col1, y=ligne2)

button_5 = Button(window, text="Avancer", command=avancer)
button_5.place(x=col5, y=ligne1)

button_6 = Button(window, text="Reculer", command=reculer)
button_6.place(x=col5, y=ligne3)

button_7 = Button(window, text="Pivgauche", command=pivgauche)
button_7.place(x=col4, y=ligne2)

button_8 = Button(window, text="Pivdroite", command=pivdroite)
button_8.place(x=col6, y=ligne2)

button_quit = Button(window, text="Quitter", command=fermeture)

zonecam = Canvas(window, width="480", height="480", background= "black")
zonecam.place(x=0, y=600)

zonemap = Canvas(window, width="480", height="480", background= "blue")
zonemap.place(x=1440, y=600)


window.mainloop()

client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

message = "command".encode()
client_socket.sendto(message, ACCES_DRONE)

message = "streamon".encode()
client_socket.sendto(message, ACCES_DRONE)

message = "setbitrate bitrate 3".encode()
client_socket.sendto(message, ACCES_DRONE)

message = "setresolution resoltion low".encode()
client_socket.sendto(message, ACCES_DRONE)

tv = Treadvideo(zonecam)
tv.start()

getresp(label)

