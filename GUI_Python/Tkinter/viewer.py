import os
from pathlib import Path
from tkinter import *
from PIL import ImageTk, Image


def forward(img_num):
	global my_label, button_forward, button_back
	my_label.grid_forget()
	my_label = Label(image=img_list[img_num-1])
	my_label.grid(row=0, column=0)
	button_forward = Button(root, text='>>', command=lambda: forward(img_num+1))
	button_back = Button(root, text='<<',  command=lambda: forward(img_num-2))

	if img_num == 4:
		button_forward = Button(root, '>>', state=DISABLED)

	my_label.grid(row=0, column=0, columnspan=3)
	button_back.grid(row=1, column=0)
	button_forward.grid(row=1, column=2)


def backward():
	pass


root = Tk()
root.title('Simple Image Viewer')
icon = PhotoImage(file='icon.ico')
root.tk.call('wm', 'iconphoto', root._w, icon)

img_list = []

for i in range(1, 5):
	img_list.append(ImageTk.PhotoImage(Image.open(f'images\{i}.jpg')))

my_label = Label(image=img_list[0])
my_label.grid(row=0, column=0, columnspan=3)

button_back = Button(root, text='<<', command=backward)
button_exit = Button(root, text='EXIT PROGRAM', command=root.quit)
button_forward = Button(root, text='>>', command=lambda: forward(0))

button_back.grid(row=1, column=0)
button_exit.grid(row=1, column=1)
button_forward.grid(row=1, column=2)


root.mainloop()
