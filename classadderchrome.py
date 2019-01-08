#UF Class Adder
#Created by Andrew Ratz

from tkinter import *
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import time
import os
import platform
import threading
import sys
from tkinter.scrolledtext import ScrolledText

chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--window-size=1920x1080")
if hasattr(sys, "_MEIPASS"):
	if platform.system() == "Windows":
		chrome_driver = sys._MEIPASS + os.sep + "driver" + os.sep + "chromedriver.exe"
	else:
		chrome_driver = sys._MEIPASS + os.sep + "driver" + os.sep + "chromedriver"
else:
	if platform.system() == "Windows":
		chrome_driver = os.getcwd() + os.sep + "driver" + os.sep + "chromedriver.exe"
	else:
		chrome_driver = os.getcwd() + os.sep + "driver" + os.sep + "chromedriver"
driver = None

def start(username, password, course, section):
	 thread = threading.Thread(target=addClass, args=(username, password, course, section))
	 thread.setDaemon(True)
	 thread.start()

def addClass(username, password, course, section):
	global driver
	driver = webdriver.Chrome(options=chrome_options, executable_path=chrome_driver)
	driver.get("https://one.uf.edu/shib/login")

	j_username = driver.find_element_by_name("j_username")
	j_password = driver.find_element_by_name("j_password")

	j_username.clear()
	j_password.clear()
	j_username.send_keys(username)
	j_password.send_keys(password)
	submit = driver.find_element_by_id("submit")
	submit.click()

	driver.get("https://one.uf.edu/myschedule/2191")
	time.sleep(3)

	wait = WebDriverWait(driver, 5)
	while True:
		driver.get("https://one.uf.edu/soc/registration-search/2191")

		while True:
			try:
				courseCode = wait.until(EC.presence_of_element_located((By.NAME, "courseCode")))
				courseCode.clear()
			except:
				print("Timeout, retrying")
				out.insert(END, "Timeout, retrying\n")
				out.see(END)
				continue
			try:
				classNum = wait.until(EC.presence_of_element_located((By.NAME, "classNum")))
				classNum.clear()
				break
			except:
				print("Timeout, retrying")
				out.insert(END, "Timeout, retrying\n")
				out.see(END)
				continue

		courseCode.send_keys(course)
		classNum.send_keys(section)
		submit = driver.find_element_by_class_name("filter-sidebar-search-button")
		submit.click()

		searchedCourse = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "course-block")))
		searchedCourse.click()

		try:
			clickCourse = wait.until(EC.presence_of_element_located((By.XPATH, "//span[@ng-click=\"filterCtrl.addSection(mainCtrl.socUserData.userName, mainCtrl.termDesc, mainCtrl.termCode, course.code, course.name, course.cNote, section)\"]")))
			clickCourse.click()

			addButton = wait.until(EC.presence_of_element_located((By.XPATH, "//button[@ng-click=\"modalCtrl.importantNote = !modalCtrl.importantNote\"]")))
			addButton.click()

			confirmButton = wait.until(EC.presence_of_element_located((By.XPATH, "//button[@ng-click=\"modalCtrl.confirmSelection(modalCtrl.addSectionData)\"]")))
			confirmButton.click()

			break

		except:
			print("Class Full, retrying")
			out.insert(END, "Class Full, retrying\n")
			out.see(END)
			continue
	print("Class Added!")
	out.insert(END, "Class Added!\n")
	out.see(END)
	quit()

def quit():
	sys.exit()

master = Tk()
master.update_idletasks()
width = master.winfo_width() + 450
height = master.winfo_height()
x = (master.winfo_screenwidth() // 2) - (width // 2)
y = (master.winfo_screenheight() // 2) - (height // 2)
master.geometry('{}x{}+{}+{}'.format(width, height, x, y))
master.title("UF Class Adder")
Label(master, text="Username").grid(row=0)
Label(master, text="Password").grid(row=1)
Label(master, text="Course Code").grid(row=2)
Label(master, text="Section Number").grid(row=3)

e1 = Entry(master)
e2 = Entry(master, show="*")
e3 = Entry(master)
e4 = Entry(master)

e1.grid(row=0, column=1)
e2.grid(row=1, column=1)
e3.grid(row=2, column=1)
e4.grid(row=3, column=1)

out = ScrolledText(master, width=50, height=10)
out.grid(row=0,column=2,rowspan=1000)

submitButton = Button(master, text="Submit", width=10, command=lambda:start(e1.get(), e2.get(), e3.get(), e4.get()))
submitButton.grid(row=4, column=1)

cancelButton = Button(master, text="Cancel", width=10, command=quit)
cancelButton.grid(row=5, column=1)

master.mainloop()

