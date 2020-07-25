import os
import threading
import time
import datetime as dt
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
from tkinter import messagebox, ttk
from tkinter import *
from PIL.ImageTk import PhotoImage, Image


def done():
	try:
		os.remove('PupilPath.html')
	except:
		quit(0)


# Checks the if html file is outdated
# def checkDate():
# 	creation_date = int(dt.datetime.fromtimestamp(os.path.getctime('PupilPath.html')).strftime('%d'))
# 	today = int(dt.datetime.today().strftime('%d'))
# 	result = today - creation_date
# 	return result

def gpa_parser():
	messagebox.showinfo('COMING SOON', 'The feature will be available in the next update..')


def grade_parser(username, password):
	if not os.path.isfile('PupilPath.html'):
		sign_in(username, password)
	with open('PupilPath.html', 'r') as html_file:
		soup = BeautifulSoup(html_file, 'html.parser')
		# table = soup.find('tbody')
		grades = soup.find('tbody').find_all('span')
		for grade in grades:
			grade_list.append(float(grade.contents[1].strip()))
	honors = []
	not_honors = []
	textbox.delete('1.0', 'end')
	textbox.insert(INSERT, 'PUPILPATH GRADES\n\n')
	for grade in grade_list:
		if grade >= 91:
			honors.append(grade)
		else:
			not_honors.append(grade)

	textbox.insert(INSERT, '===============HONORS===============\n')
	for grade in honors:
		textbox.insert(INSERT, f'{grade}\n')
	textbox.insert(INSERT, '===============NOT HONORS===========\n')
	for grade in not_honors:
		textbox.insert(INSERT, f'{grade}\n')

	textbox.insert(INSERT, '\nEND')


def parser_gui(username, password):
	# Working Frame
	main_frame2 = Frame(root)
	main_frame2.place(relwidth=1, relheight=1)

	# Background
	img = PhotoImage(Image.open('after_login_back.png'))
	background = Label(main_frame2, image=img)
	background.place(relwidth=1, relheight=1)
	background.image = img

	# Button Images
	grades_button_img = PhotoImage(Image.open("Grades_button.png"))
	gpa_button_img = PhotoImage(Image.open("GPA_button.png"))
	done_button_img = PhotoImage(Image.open('Done.png'))
	# Buttons
	grades_button = Button(main_frame2, image=grades_button_img, bg='#4a6eb5', bd=0, command=lambda: grade_parser(username, password))
	grades_button.place(relx=0.15, rely=0.43)
	grades_button.image = grades_button_img

	gpa_button = Button(main_frame2, image=gpa_button_img, bg='#4a6eb5', bd=0, command=gpa_parser)
	gpa_button.place(relx=0.15, rely=0.53)
	gpa_button.image = gpa_button_img

	done_button = Button(main_frame2, image=done_button_img, bg='#4a6eb5', bd=0, command=done)
	done_button.place(relx=0.18, rely=0.68)
	done_button.image = done_button_img
	# Screen for output
	global textbox
	textbox = Text(main_frame2, font=('Arial', 9, 'bold'), fg='#1a1a1a', bg='#f2f2f2')
	textbox.insert(INSERT, '\n When you are done with the program\n please press done before closing.')
	textbox.place(relx=0.48, rely=0.43, relwidth=0.4, relheight=0.35)


# saves login info to a separate file from which it will read next time.
def save_credentials(username, password):
	with open('credentials.txt', 'w') as f:
		f.write(f'{username}:{password}')


# Logs into PupilPath account
def sign_in(username, password):
	try:
		driver = webdriver.Chrome(ChromeDriverManager().install())
		driver.get('https://pupilpath.skedula.com/')
		time.sleep(1)
		driver.find_element_by_id('sign_in').click()
		driver.find_element_by_id('user_username').send_keys(username)
		driver.find_element_by_id('sign_in').click()
		time.sleep(1)
		driver.find_element_by_id('user_password').send_keys(password)
		driver.find_element_by_id('sign_in').click()
		time.sleep(1)
		driver.find_element_by_class_name('ui-button-text').click()
		with open('PupilPath.html', 'w') as file:
			file.write(driver.page_source)
		driver.close()
	except UnicodeEncodeError:
		messagebox.showerror('Error', 'Delete PupilPath.html and restart the app')


def login(username, password):
	# if checkbox.instate(['selected']):
	t1 = threading.Thread(target=save_credentials, args=(username, password.get()))
	t1.start()
	t2 = threading.Thread(target=sign_in, args=(username.get(), password.get()))
	t2.start()
	t2.join()
	t1.join()
	# else:
	# 	sign_in(username, password)

	if not os.path.isfile('credentials.txt'):
		main_frame.destroy()
	parser_gui(username, password)


def login_gui():
	# Working Frame
	global main_frame
	main_frame = Frame(root)
	main_frame.place(relwidth=1, relheight=1)

	# Background
	img = PhotoImage(Image.open('back.png'))
	background = Label(main_frame, image=img)
	background.place(relwidth=1, relheight=1)
	background.image = img

	# text fields for getting data
	username_entry = ttk.Entry(main_frame)
	username_entry.place(relx=0.4, rely=0.4899, relwidth=0.4, relheight=0.045)

	password_entry = ttk.Entry(main_frame, show='*')
	password_entry.place(relx=0.4, rely=0.5799, relwidth=0.4, relheight=0.045)

	# save password checkbox
	global checkbox
	checkbox = ttk.Checkbutton(main_frame, text='Save password?')
	checkbox.state(['!alternate'])
	checkbox.place(relx=0.45, rely=0.6799, relheight=0.049)
	# button to login
	login_button = Button(main_frame, text='login', command=lambda: login(username_entry, password_entry))
	login_button.place(relx=0.65, rely=0.6799, relwidth=0.2, relheight=0.05)


def main():
	global root, canvas, grade_list

	grade_list = []
	root = Tk()
	root.title('PupilPath++')

	canvas = Canvas(root, width=700, height=500)
	canvas.pack()

	if not os.path.isfile('credentials.txt'):
		login_gui()
	else:
		with open('credentials.txt', 'r') as f:
			line = f.readline().strip('\n')
			username = line.split(':')[0]
			password = line.split(':')[1]
		parser_gui(username, password)
	root.mainloop()


if __name__ == '__main__':
	main()
