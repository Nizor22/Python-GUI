from tkinter import *
from PIL.ImageTk import PhotoImage, Image


def testButton():
    print('Button Clicked!')


root = Tk()

HEIGHT = 400
WIDTH = 500


canvas = Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()

background_img = PhotoImage(Image.open('images/back.jpg'))
background_label = Label(root, image=background_img)
background_label.place(relwidth=1, relheight=1)

frame = Frame(root, bg='#80c1ff', bd=5)
frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.1, anchor='n')

entry = Entry(frame, font=40)
entry.place(relwidth=0.65, relheight=1)

button = Button(frame, text='Get Weather', font=40, highlightbackground='#3E4149', command=testButton)
button.place(relx=0.7, relwidth=0.3, relheight=1)

lower_frame = Frame(root, bg='#80c1ff', bd=10)
lower_frame.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.6, anchor='n')

label = Label(lower_frame)
label.place(relwidth=1, relheight=1)

root.mainloop()

