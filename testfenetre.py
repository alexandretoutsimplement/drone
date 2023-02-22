from tkinter import *
import socket

def getresp(label):
	client_socket.timeout(1)

	try: 
		message, address=client_socket.recvfrom(1024)
	except:
		message= "Problème de connexion"
	label.config(text=message)
	
def decoller():
	message = "takeoff".encode()
	client_socket.sendto(message, (SERVER_IP, SERVER_PORT))
	getresp(label)
def atterir():
	message = "land".encode()
	client_socket.sendto(message, (SERVER_IP, SERVER_PORT))
	getresp(label)
def droite():
	message = "right 20".encode()
	client_socket.sendto(message, (SERVER_IP, SERVER_PORT))
	getresp(label)
def gauche():
	message = "left 20".encode()
	client_socket.sendto(message, (SERVER_IP, SERVER_PORT))
	getresp(label)
	
SERVER_IP = "192.168.10.1"
SERVER_PORT =  8889

window=Tk()

window.title("Manette")
window.geometry("1920x1080")

col1=100
col2=200
col3=300

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

zonecam = Canvas(window, width="480", height="480", background= "black")
zonecam.place(x=0, y=600)

zonemap = Canvas(window, width="480", height="480", background= "blue")
zonemap.place(x=1440, y=600)


window.mainloop()

client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)


message = "command".encode()
client_socket.sendto(message, (SERVER_IP, SERVER_PORT))


getresp(label)



client_socket.close()
