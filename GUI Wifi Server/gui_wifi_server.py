from tkinter import *
import socket
import threading


def runserver():
    serverip = '192.168.0.54'
    port = 9002
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
        # data = 'LED1:ON' or 'LED1:OFF'
        data_split = data.split(':')

        if float(data_split[1]) > 32:
            img = PhotoImage(file='level3.png')
            ICON.configure(image=img)
            ICON.image = img
            v_status.set('{} temperature is {} °C'.format(data_split[0], data_split[1]))
        elif float(data_split[1]) > 28.5:
            img = PhotoImage(file='level2.png')
            ICON.configure(image=img)
            ICON.image = img
            v_status.set('{} temperature is {} °C'.format(data_split[0], data_split[1]))
        elif float(data_split[1]) > 25.5:
            img = PhotoImage(file='level1.png')
            ICON.configure(image=img)
            ICON.image = img
            v_status.set('{} temperature is {} °C'.format(data_split[0], data_split[1]))
        else:
            img = PhotoImage(file='level1.png')
            ICON.configure(image=img)
            ICON.image = img
            v_status.set('Temperature is cold')
            


        # if data_split[1] == 'ON':
        #     v_status.set('{} status is {} '.format(data_split[0], data_split[1]))
        #     label2.configure(fg='green')
        # else:
        #     v_status.set('{} status is {} '.format(data_split[0], data_split[1]))
        #     label2.configure(fg='red')

        client.send('received your messages.'.encode('utf-8'))
        client.close()


GUI = Tk()
GUI.geometry('750x500')
GUI.title('IoT-Wifi-Server Develope By Anitocorn Inc.')

FONT = ('Roman', 20)
FONT1 = (15)

label1 = Label(GUI, text='Check status LED', font=FONT)
label1.pack()

v_status = StringVar()
v_status.set('<<< NO STATUS >>>')
label2 = Label(GUI, textvariable=v_status, font=FONT1)
label2.configure(fg='red')
label2.pack()

img = PhotoImage(file='level1.png')
ICON = Label(GUI,image=img)
ICON.pack()

# -------------runserver-------------
task = threading.Thread(target=runserver)
task.start()


GUI.mainloop()