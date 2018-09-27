import argparse
import time
import os
import Tkinter as tk

WORKING_DAYS = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri']

BASE = 2092.

PATH = u'/Users/yangwei/ENV/iphone_app/'

class App(object):
	def __init__(self):

		with open(PATH +'log.txt', 'r+') as f:
			self.first_line = f.readline()
			self.alist = self.first_line.split()
			self.month, self.base, self.hours = self.alist[0], float(self.alist[1]), float(self.alist[2])
			self.sigle = self.cal(self.base, self.hours)

		self.root = tk.Tk()
		self.root.title('Digital Clock')
		self.root.geometry('800x500')
		self.clock_frame = tk.Label(self.root, font=('times', 50, 'bold'), bg='black', fg='green')
		self.clock_frame.pack(fill='both', expand=1)

	def cal(self, salary, week_working_hours):
		one_SEC_salary = salary / (60*60*week_working_hours*4)
		return one_SEC_salary

	def get_time(self):
		time1 = ''
		time2 = time.strftime("%a. %d %b %Y %H:%M:%S", time.gmtime())
		if time2[:3] in WORKING_DAYS:
			if time2[-9:-6] <= 17 or time2[-9:-6] >= 10:
				if time2 != time1:
					self.base += self.sigle
					self.clock_frame.config(text=("%.2f" % self.base))
				self.clock_frame.after(200, self.get_time)

	def main(self):

		self.get_time()
		self.root.mainloop()

def get_val():

	parser = argparse.ArgumentParser(description=__doc__)
	parser.add_argument("--s", type=float, help='monthly salary netto')
	parser.add_argument("--wwh", type=int, help='weekly working hours')
	args = parser.parse_args()
	return args.s, args.wwh

if __name__ == '__main__':

	app = App()
	app.main()
