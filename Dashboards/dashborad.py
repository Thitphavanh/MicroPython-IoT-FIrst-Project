from tkinter import *
from PIL import Image, ImageTk
from matplotlib import image
from threading import Thread
import time

GUI = Tk()
GUI.geometry('1280x720')
GUI.title('SMART IOT BY ANITOCORN INC.')
GUI.state('zoomed')

canvas = Canvas(GUI, width=1580, height=720)
canvas.place(x=0, y=0)

background = ImageTk.PhotoImage(Image.open('farm.png'))
canvas.create_image(300, 200, anchor=NW, image=background)


# ----------------------Door----------------------
# square
canvas.create_polygon([630, 426, 675, 450, 675, 495, 629, 470],fill='red', width=1, outline=None, tags='d1')
# text
canvas.create_text(300, 300, text='Window is going to open',fill='black', font=('bold', 20), tags='d1')
# line
canvas.create_line(425, 320, 640, 455, fill='grey', width=1, tags='d1')
# canvas.create_line(150,50,120,100,50,0,0,50,smooth=1)

door_state = True


def DoorOnOff(event):
    global door_state
    door_state = not door_state
    canvas.delete('d1')
    if door_state == True:
        canvas.create_polygon([630, 426, 675, 450, 675, 495, 629, 470],fill='yellow', width=1, outline=None, tags='d1')
        canvas.create_text(300, 300, text='Window is going to open',fill='black', font=('bold', 20), tags='d1')
        canvas.create_line(425, 320, 640, 455, fill='grey', width=1, tags='d1')
    else:
        canvas.create_polygon([630, 426, 675, 450, 675, 495, 629, 470],fill='red', width=1, outline=None, tags='d1')
        canvas.create_text(300, 300, text='Window is going to close',fill='black', font=('bold', 20), tags='d1')
        canvas.create_line(425, 320, 640, 455, fill='grey', width=1, tags='d1')


fan = ImageTk.PhotoImage(Image.open('fan.png')) 
canvas.create_image(1063,461,image=fan,tags='img3',anchor=CENTER)

angle = 0

def run_fan(event=None):
	# fan = ImageTk.PhotoImage(resize_image('fan-icon.png',100))
	global angle
	while True:	
		if angle != 0:
			canvas.delete('img3')
			fan = ImageTk.PhotoImage(image = Image.open('fan.png').rotate(angle)) 
			canvas.create_image(1063,461,image=fan,tags='img3',anchor=CENTER)
		angle += 45
		if angle >= 360:
			angle = 0
		time.sleep(0.1)

task = Thread(target=run_fan)
task.start()


GUI.bind('<Return>',DoorOnOff)
GUI.mainloop()
