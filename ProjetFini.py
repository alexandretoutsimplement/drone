import tkinter
import threading 
import socket
import sys
import time

host = ''
port = 9000
locaddr = (host,port) 

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

tello_address = ('192.168.10.1', 8889)

sock.bind(locaddr)

msg = "command".encode()
sock.sendto(msg, tello_address)

msg = "streamon".encode()
sock.sendto(msg, tello_address)

def video():
    print("demare thread")
    host = '0.0.0.0'
    port = 11111
    locaddr = (host,port) 

    sockv = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

   # tello_address = ('192.168.10.1', 11111)
    
    global continuer
   # sockv.bind(locaddr)

    reader, writer = asyncio.open_connection ('127.0.0.1', 11111)

    #sockv.listen()
    cap=cv2.VideoCapture(reader)
    if not cap.isOpened():
        print("ne peux pas ouvrir la caméra")
        exit()
        

    while continuer: 
     ret, frame = cap.read()
     cv2.imshow('frame', frame)
     print("continue")
     time.sleep(2)
     if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    cap.release()
    cv2.destroyAllWindows()

def recv():
    count = 0
    while True: 
        try:
            data, server = sock.recvfrom(1518)
            print(data.decode(encoding="utf-8"))
        except Exception:
            print ('\nExit . . .\n')
            break

def getresp(label):
	sock.timeout(1)

	try: 
		msg, address=sock.recvfrom(1024)
	except:
		msg= "Problème de connexion"
	label.config(text=msg)
def decoller():
	msg = "takeoff".encode()
	sock.sendto(msg, tello_address)
	getresp(label)
def atterir():
	msg = "land".encode()
	sock.sendto(msg, tello_address)
	getresp(label)
def droite():
	msg = "right 40".encode()
	sock.sendto(msg, tello_address)
	getresp(label)
def gauche():
	msg = "left 40".encode()
	sock.sendto(msg, tello_address)
	getresp(label)
def avancer():
	msg = "forward 40".encode()
	sock.sendto(msg, tello_address)
	getresp(label)
def reculer():
	msg = "back 40".encode()
	sock.sendto(msg, tello_address)
	getresp(label)
def pivdroite():
	msg = "cw 90".encode()
	sock.sendto(msg, tello_address)
	getresp(label)
def pivgauche():
	msg = "ccw 90".encode()
	sock.sendto(msg, tello_address)
	getresp(label)

window=tkinter.Tk()

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

label= tkinter.Label(window,text="")
label.place(x=810, y=0)

button_1 = tkinter.Button(window, text="Décoller", command=decoller)
button_1.place(x=col2, y=ligne1)

button_2 = tkinter.Button(window, text="Atterir", command=atterir)
button_2.place(x=col2, y=ligne3)

button_3 = tkinter.Button(window, text="Droite", command=droite)
button_3.place(x=col3, y=ligne2)

button_4 = tkinter.Button(window, text="Gauche", command=gauche)
button_4.place(x=col1, y=ligne2)

button_5 = tkinter.Button(window, text="Avancer", command=avancer)
button_5.place(x=col5, y=ligne1)

button_6 = tkinter.Button(window, text="Reculer", command=reculer)
button_6.place(x=col5, y=ligne3)

button_7 = tkinter.Button(window, text="Pivgauche", command=pivgauche)
button_7.place(x=col4, y=ligne2)

button_8 = tkinter.Button(window, text="Pivdroite", command=pivdroite)
button_8.place(x=col6, y=ligne2)

zonecam = tkinter.Canvas(window, width="480", height="480", background= "black")
zonecam.place(x=0, y=600)

zonemap = tkinter.Canvas(window, width="480", height="480", background= "blue")
zonemap.place(x=1440, y=600)

window.mainloop()

print ('\r\n\r\nTello Python3 Demo.\r\n')

print ('Tello: command takeoff land flip forward back left right \r\n       up down cw ccw speed speed?\r\n')

print ('end -- quit demo.\r\n')

recvThread = threading.Thread(target=recv)
threading.Thread(target=video).start()
recvThread.start()

while True: 

    try:
        msg = input("");

        if not msg:
            break  

        if 'end' in msg:
            print ('...')
            sock.close()  
            break

        msg = msg.encode(encoding="utf-8") 
        sent = sock.sendto(msg, tello_address)
    except KeyboardInterrupt:
        print ('\n . . .\n')
        sock.close()  
        break