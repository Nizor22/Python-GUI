from tkinter import *

root = Tk()

# Creating a label
myLabel = Label(root, text='Hello World')
myLabel2 = Label(root, text='My name is Nizor')
myLabel3 = Label(root, text='                   ')
# Shoving it onto the screen
myLabel.grid(row=0, column=0)
myLabel3.grid(row=0, column=1)
myLabel2.grid(row=1, column=5)

root.mainloop()