from tkinter import *
from PIL import ImageTk, Image

# root.iconbitmap('icon.ico')
# This works only w. black/white icons so I did something diff.

root = Tk()
root.title('Images and Icons')
icon = PhotoImage(file='icon.ico')
root.tk.call('wm', 'iconphoto', root._w, icon)

my_img = ImageTk.PhotoImage(Image.open('download.jpg.png'))
my_label = Label(image=my_img)
my_label.pack()


button_quit = Button(root, text='Exit Program', command=root.quit)
button_quit.pack()


root.mainloop()
