from tkinter import *

root = Tk()


def myClick():
	myLabel = Label(root, text='Look I clicked a button!', bg= '#4dffff', fg='Black')
	myLabel.pack()


myButton = Button(root, text="Can't click me", state=DISABLED)
# Pad{x/y} expands in either direction
# Command keyword calls the function w/o parenthesis!
myButton2 = Button(root, text='Click me', padx=50, command=myClick, bg='Yellow', fg='Black')
myButton.pack()
myButton2.pack()

root.mainloop()
