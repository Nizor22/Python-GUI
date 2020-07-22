from tkinter import *

root = Tk()

canvas = Canvas(root, width=500, height=400)
canvas.pack()

top_frame = Frame(root, bg='#4da6ff', bd=5)
top_frame.place(relx=0, rely=0, relwidth=1, relheight=0.2)

label = Label(top_frame, text='PUPILPATH++', font=('Ariel', 20, 'bold'), fg='WHITE', bg='#d9b3ff')
label.place(relx=0.01, rely=0.05, relwidth=0.99, relheight=0.95, anchor='nw')


middle_frame = Frame(root, bg='#4da6ff', bd=5)
middle_frame.place()

root.mainloop()