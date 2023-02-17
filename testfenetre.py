from tkinter import *
import socket

SERVER_IP = "192.168.10.1"
SERVER_PORT =  8889

window=Tk()

window.title("Manette")
window.geometry("1920x1080")


client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

message = "Command".encode()
client_socket.sendto(message, (SERVER_IP, SERVER_PORT))

def on_button_1_click():
        message = "takeoff".encode()
client_socket.sendto(message, (SERVER_IP, SERVER_PORT))

def on_button_2_click():
        message = "land".encode()
client_socket.sendto(message, (SERVER_IP, SERVER_PORT))
    
def on_button_3_click():
        message = "right 20".encode()
client_socket.sendto(message, (SERVER_IP, SERVER_PORT))

def on_button_4_click():
        message = "left 20".encode()
client_socket.sendto(message, (SERVER_IP, SERVER_PORT))

button_1 = Button(window, text="Monter", command=on_button_1_click)
button_1.grid(row=0,column=1)

button_2 = Button(window, text="Décendre", command=on_button_1_click)
button_2.grid(row=2, column=1)

button_3 = Button(window, text="Droite", command=on_button_1_click)
button_3.grid(row=1, column=2)

button_4 = Button(window, text="Gauche", command=on_button_1_click)
button_3.grid(row=1, column=0)


window.mainloop()

client_socket.close()