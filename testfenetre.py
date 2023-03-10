from tkinter import *
import cv2
import socket
import pickle
import struct


def getresp(label):
	client_socket.timeout(1)

	try: 
		message, address=client_socket.recvfrom(1024)
	except:
		message= "Problème de connexion"
	label.config(text=message)
	
def decoller():
	message = "takeoff".encode()
	client_socket.sendto(message, (COMMAND_IP, COMMAND_PORT))
	getresp(label)
def atterir():
	message = "land".encode()
	client_socket.sendto(message, (COMMAND_IP, COMMAND_PORT))
	getresp(label)
def droite():
	message = "right 20".encode()
	client_socket.sendto(message, (COMMAND_IP, COMMAND_PORT))
	getresp(label)
def gauche():
	message = "left 20".encode()
	client_socket.sendto(message, (COMMAND_IP, COMMAND_PORT))
	getresp(label)
	
def avancer():
	message = "forward 20".encode()
	client_socket.sendto(message, (COMMAND_IP, COMMAND_PORT))
	getresp(label)

def reculer():
	message = "back 20".encode()
	client_socket.sendto(message, (COMMAND_IP, COMMAND_PORT))
	getresp(label)
	
def pivdroite():
	message = "cw 20".encode()
	client_socket.sendto(message, (COMMAND_IP, COMMAND_PORT))
	getresp(label)

def pivgauche():
	message = "ccw 20".encode()
	client_socket.sendto(message, (COMMAND_IP,COMMAND_PORT))
	getresp(label)
	
COMMAND_IP = "192.168.10.1"
COMMAND_PORT =  8889

VIDEO_IP = "127.0.0.1"
VIDEO_PORT = 11111

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

button_5 = Button(window, text="Avancer", command=decoller)
button_5.place(x=col5, y=ligne1)

button_6 = Button(window, text="Reculer", command=reculer)
button_6.place(x=col5, y=ligne3)

button_7 = Button(window, text="Pivgauche", command=pivgauche)
button_7.place(x=col4, y=ligne2)

button_8 = Button(window, text="Pivdroite", command=pivdroite)
button_8.place(x=col6, y=ligne2)

zonecam = Canvas(window, width="480", height="480", background= "black")
zonecam.place(x=0, y=600)

zonemap = Canvas(window, width="480", height="480", background= "blue")
zonemap.place(x=1440, y=600)


window.mainloop()

client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

sock.bind((VIDEO_IP, VIDEO_PORT))

sock.listen()

while True:
	drone_socket, addr = server_socket.accept()
	print('Connecter depuis', addr)
	if drone_socket:
		vid = cv2.VideoCapture(0)
		while(vid.isOpened()):
			img,frame = vid.read()
			a = pickle.dumps(frame)
			message = struct.pack("Q",len(a))+a
			drone_socket.sendall(message)
			cv2.imshow(zoncam,frame)

message = "command".encode()
client_socket.sendto(message, (COMMAND_IP, COMMAND_PORT))

message = "streamon".encode()
client_socket.sendto(message, (COMMAND_IP, COMMAND_PORT))

message = "setbitrate bitrate 3".encode()
client_socket.sendto(message, (COMMAND_IP, COMMAND_PORT))

message = "setresolution resoltion low".encode()
client_socket.sendto(message, (COMMAND_IP, COMMAND_PORT))



getresp(label)



client_socket.close()
