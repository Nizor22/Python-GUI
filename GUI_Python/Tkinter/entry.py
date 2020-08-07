from tkinter import *

root = Tk()


def myClick():
	myLabel = Label(root, text=f'Hello {e.get()} !\n Nice to meet you!', bg='#4dffff', fg='Black')
	myLabel.pack()


# Entry is the input field Widget
e = Entry(root, width=50, borderwidth=3, bg='#4dffff', fg='Black')
e.insert(0, 'Enter your name..')
e.pack()


# Button is the Button Widget.
# State=Disabled makes the button unclickable.
myButton = Button(root, text="Can't click me", state=DISABLED)

# Pad{x/y} expands in either direction
# Command keyword calls the function w/o parenthesis!
myButton2 = Button(root, text='Try', padx=50, command=myClick, bg='Yellow', fg='Black')
myButton.pack()
myButton2.pack()

root.mainloop()
