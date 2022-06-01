from tkinter import *
import socket
import threading


def runserver():
	serverip = '192.168.0.54'
	port = 9000
	buffsize = 4096

	while True:
		server = socket.socket()
		server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
		server.bind((serverip, port))
		server.listen(1)
		print('waiting micropython...')

		client, addr = server.accept()
		print('connected from:', addr)

		data = client.recv(buffsize).decode('utf-8')
		print('Data from MicroPython: ', data)
		client.send('received your messages.'.encode('utf-8'))
		client.close()


GUI = Tk()
GUI.geometry('650x400')
GUI.title('IoT-Wifi-Server Develope By Anitocorn Inc.')

FONT = ('Roman', 20)
FONT1 = (15)

label1 = Label(GUI, text='LED status from MicroPython', font=FONT)
label1.pack()

v_status = StringVar()
v_status.set('<<< NO STATUS >>>')
label2 = Label(GUI, textvariable=v_status, font=FONT1)
label2.configure(fg='grey')
label2.pack()


GUI.mainloop()
