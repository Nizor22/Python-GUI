import os
from selenium import webdriver
# from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
from tkinter import *
# from PIL.ImageTk import PhotoImage, Image


def parser():
    with open('PupilPath.html', 'r') as html_file:
        soup = BeautifulSoup(html_file, 'html.parser')
        # table = soup.find('tbody')
        grades = soup.find('tbody').find_all('span')
        for grade in grades:
            grade_list.append(float(grade.contents[1].strip()))


def parser_gui():

    # Title Frame
    title_frame = Frame(root, bg='#4da6ff', bd=5)
    title_frame.place(relx=0, rely=0, relwidth=1, relheight=0.2)

    label = Label(title_frame, text='PUPILPATH++', font=('Ariel', 20, 'bold'), fg='WHITE', bg='#d9b3ff')
    label.place(relx=0.01, rely=0.05, relwidth=0.99, relheight=0.95, anchor='nw')

    # Working Frame
    main_frame2 = Frame(root, bg='#6666ff')
    main_frame2.place(relx=0.0, rely=0.2, relwidth=1, relheight=1)

    welcome = Label(main_frame2, text='Welcome to PupilPath++', font=('Ariel', 20))
    instruction = Label(main_frame2, text='To get your grades just click the button', font=('Ariel', 14))

    welcome.place(relx=0.21, rely=0.03)
    instruction.place(relx=0.21, rely=0.1)
    button = Button(main_frame2, text='Parse Grades', highlightbackground='blue', command=parser)
    button.place(relx=0.21, rely=0.5)

# saves login info to a separate file from which it will read next time.
def save_credentials(username, password):
    with open('credentials.txt', 'w') as f:
        f.write(f'{username}:{password}')


def login(username, password, checkbox):
    if checkbox:
        save_credentials(username, password)

    # driver = webdriver.Chrome(ChromeDriverManager().install())
    # driver.get('https://pupilpath.skedula.com/')
    # driver.find_element_by_id('sign_in').click()
    # driver.find_element_by_id('user_username').send_keys(username)
    # driver.find_element_by_id('sign_in').click()
    # driver.find_element_by_id('user_password').send_keys(password)
    # driver.find_element_by_id('sign_in').click()
    # driver.find_element_by_class_name('ui-button-text').click()
    # with open('PupilPath.html', 'w') as file:
    #     file.write(driver.page_source)
    main_frame.destroy()
    parser_gui()


def login_gui():
    # Title Frame
    title_frame = Frame(root, bg='#4da6ff', bd=5)
    title_frame.place(relx=0, rely=0, relwidth=1, relheight=0.2)

    label = Label(title_frame, text='PUPILPATH++', font=('Ariel', 20, 'bold'), fg='WHITE', bg='#d9b3ff')
    label.place(relx=0.01, rely=0.05, relwidth=0.99, relheight=0.95, anchor='nw')

    # Working Frame
    global main_frame

    main_frame = Frame(root, bg='#6666ff')
    main_frame.place(relx=0.0, rely=0.2, relwidth=1, relheight=1)

    # labels for text fields
    username_label = Label(main_frame, text='Username', fg='blue')
    password_label = Label(main_frame, text='Password', fg='blue')

    username_label.place(relx=0.21, rely=0.03, relheight=0.05)
    password_label.place(relx=0.21, rely=0.1, relwidth=0.131, relheight=0.05)

    # text fields for getting data
    username_entry = Entry(main_frame)
    # username_entry.insert(0, 'Erase this first..')
    username_entry.place(relx=0.4, rely=0.03, relwidth=0.55, relheight=0.05)

    password_entry = Entry(main_frame, bg='White')
    # password_entry.insert(0, 'Erase this first..')
    password_entry.place(relx=0.4, rely=0.1, relwidth=0.55, relheight=0.05)

    username = username_entry.get()
    password = password_entry.get()

    # button to login
    login_button = Button(main_frame, text='login', highlightbackground='blue', command=lambda: login(username, password, c))
    login_button.place(relx=0.7, rely=0.2, relwidth=0.2, relheight=0.05)

    # save password checkbox
    c = BooleanVar()
    checkbox = Checkbutton(main_frame, text='Save password?', var=c)
    checkbox.place(relx=0.6, rely=0.2, relwidth=0.05, relheight=0.05)
    # Label for checkbox
    label = Label(main_frame, text='Save password?')
    label.place(relx=0.4, rely=0.2, relheight=0.05)


def main():
    global root, canvas, grade_list

    grade_list = []
    root = Tk()
    canvas = Canvas(root, width=500, height=400)
    canvas.pack()
    if not os.path.isfile('credentials.txt'):
        login_gui()
    else:
        parser_gui()


    root.mainloop()


if __name__ == '__main__':
    main()
