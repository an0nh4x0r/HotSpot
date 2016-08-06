from tkinter import *
from tkinter import ttk 
from os import system 
import sys

class Hotspot(object):
	def __init__(self, master):
		self.label1 = ttk.Label(text = 'Hotspot')
		self.label1.grid(row = 0, column = 0, columnspan = 2)

		self.label2 = ttk.Label(text = "Enter Hotspot Name")
		self.label2.grid(row = 1, column = 0)
		self.e1 = ttk.Entry()
		self.e1.grid(row = 1, column = 1)

		self.label3 = ttk.Label(text = 'Enter Password')
		self.label3.grid(row = 2, column = 0)
		self.e2 = ttk.Entry()
		self.e2.config(show = '*')
		self.e2.grid(row = 2, column = 1)

		self.label4 = ttk.Label(text = "Again Enter Password ")
		self.label4.grid(row = 3, column = 0)
		self.e3 = ttk.Entry()
		self.e3.config(show = '*')
		self.e3.grid(row = 3, column = 1)

		ttk.Button(text = 'Start', command = self.start_start, state = 'normal').grid(row = 4, column = 0)
		ttk.Button(text = 'Stop', command = self.stop_stop, state = 'disabled').grid(row = 4, column = 1)

	def start_start(self):
		name = self.e1.get()
		if self.e2.get() == self.e3.get() and len(self.e2.get()) > 7:
			password = self.e2.get()
			self.e1.state(['disabled'])
			self.e2.state(['disabled'])
			self.e3.state(['disabled'])
			system('netsh wlan set hostednetwork mode=allow ssid={} key={}'.format(name,password))
			system('netsh wlan start hostednetwork')
			ttk.Button(text = 'Start', command = self.start_start, state = 'disabled').grid(row = 4, column = 0)
			ttk.Button(text = 'Stop', command = self.stop_stop, state = 'normal').grid(row = 4, column = 1)
		else:
			win = Tk()
			win.title('Alert!')
			laabel = ttk.Label(win, text = 'Passwords don\'t match or Password is less then 8 characters or You have not entered the name!')
			laabel.config(wraplength = 170)
			laabel.pack()
			buutton = ttk.Button(win, text = 'okay', command = win.destroy).pack()
			win.mainloop() 

	def stop_stop(self):
		system('netsh wlan stop hostednetwork')
		self.e1.state(['!disabled'])
		self.e2.state(['!disabled'])
		self.e3.state(['!disabled'])
		ttk.Button(text = 'Start', command = self.start_start, state = 'normal').grid(row = 4, column = 0)
		ttk.Button(text = 'Stop', command = self.stop_stop, state = 'disabled').grid(row = 4, column = 1)

def main():
	root = Tk()
	root.title('Pythoneshwar')
	app = Hotspot(root)
	root.mainloop()

if __name__ == '__main__':
	main()