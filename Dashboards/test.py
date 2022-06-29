from tkinter import *
from PIL import Image, ImageTk
from threading import Thread
import time

GUI = Tk()
GUI.geometry('1000x636')
GUI.title('SMART IOT BY ANITOCORN INC.')
GUI.state('zoomed')

# Canvas กระดานวาดภาพ
canvas = Canvas(GUI, width=1920, height=1080)
canvas.place(x=0, y=0)

# path = r'C:\Users\Uncle Engineer\Desktop\MicroPython Course\WiFi\farm.png'
# background = ImageTk.PhotoImage(Image.open(path))

# ใส่ background
background = ImageTk.PhotoImage(Image.open('farm.png'))
canvas.create_image(300, 200, anchor=NW, image=background)  # 1


# ----------------------Door----------------------
# ໃສ່ຫຼາຍຫຼ່ຽມ square
canvas.create_polygon([630, 426, 675, 450, 675, 495, 629, 470],fill='#01262e', width=1, outline=None, tags='d1')
# ໃສ່ຂໍ້ຄວາມ text
canvas.create_text(300, 300, text='Window is going to close',fill='#01262e', font=('bold', 20), tags='d1')
# ໃສ່ເສັ້ນ line
canvas.create_line(425, 320, 640, 455, fill='grey', width=1, tags='d1')
# canvas.create_line(150,50,120,100,50,0,0,50,smooth=1)


# ສະຖານະປະຕູ
door_state = True


def DoorOnOff(event):
    # ປ່ຽນໂຕແປດ້ານນອກຟັງຊັ່ນ
    global door_state
    # ສະຫຼັບສະຖານະ
    door_state = not door_state
    canvas.delete('d1')
    if door_state == True:
        canvas.create_polygon([630, 426, 675, 450, 675, 495, 629, 470],fill='#01262e', width=1, outline=None, tags='d1')
        canvas.create_text(300, 300, text='Window is going to close', fill='#01262e', font=('bold', 20), tags='d1')
        canvas.create_line(425, 320, 640, 455, fill='grey', width=1, tags='d1')
    else:
        canvas.create_polygon([630, 426, 675, 450, 675, 495, 629, 470],fill='#e8c307', width=1, outline=None, tags='d1')
        canvas.create_text(300, 300, text='Window is going to open',fill='#e8c307', font=('bold', 20), tags='d1')
        canvas.create_line(425, 320, 640, 455, fill='grey', width=1, tags='d1')


# ----------------------Fan----------------------
fan = ImageTk.PhotoImage(Image.open('fan.png'))
canvas.create_image(1063, 461, image=fan, tags='img3', anchor=CENTER)

angle = 0
fan_state = True


def run_fan(event=None):
    # fan = ImageTk.PhotoImage(resize_image('fan-icon.png',100))
    global angle
    while True:
        if fan_state:
            canvas.delete('img3')
            fan = ImageTk.PhotoImage(image=Image.open('fan.png').rotate(angle))
            canvas.create_image(1063, 461, image=fan,tags='img3', anchor=CENTER)
            angle += 30
            # if angle > 360:
            # 	angle = 0
        else:
            fan = ImageTk.PhotoImage(image=Image.open('fan.png').rotate(angle))
            canvas.create_image(1063, 461, image=fan,tags='img3', anchor=CENTER)

        time.sleep(0.1)
    print('break')


task = Thread(target=run_fan)
task.start()


def reset_fan(event):
    global fan_state
    fan_state = not fan_state
    try:
        if fan_state:
            canvas.itemconfig('img3', state='normal')
        else:
            canvas.itemconfig('img3', state='hidden')
    except:
        pass


GUI.bind('<F12>', reset_fan)
GUI.bind('<Return>', DoorOnOff)
GUI.mainloop()
