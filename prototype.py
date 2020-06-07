import argparse
import time
import sys
import os
import tkinter as tk


ODD = [1, 3, 5, 7, 8, 10, 12]

sys.path.append(os.path.realpath('..'))

class App(object):

	def __init__(self):

		self.f = open('log.txt', 'r+')
		self.first_line = self.f.readline()
		self.alist = self.first_line.split()
		self.before, self.base, self.hours = float(self.alist[0]), float(self.alist[1]), float(self.alist[2])
		self._base = 0
		self.root = tk.Tk()
		self.root.title('Salary Counter')
		self.root.geometry('400x150')
		self.clock_frame = tk.Label(self.root, font=('times', 50, 'bold'), bg='black', fg='white')
		self.clock_frame.pack(fill='both', expand=1)
		now = time.time()
		if time.localtime(now)[1] in ODD:
			self.days = 31
		else:
			if time.localtime(now)[1] == 2:
				#if ((time.localtime(now)[0] % 4 == 0 and time.localtime(now)[0] % 100 != 0) or (time.localtime(now)[0] % 400 == 0 and time.localtime(now)[0] % 3200 != 0)):
				if ((time.localtime(now)[0] % 4 == 0 and time.localtime(now)[0] % 100 != 0) or time.localtime(now)[0] % 400 == 0:
					self.days = 29
				else:
					self.days = 28
			else:
				self.days = 30

		self.sigle = self.cal(2244.41, self.hours)

		if now != self.before:
			self.base += self.sigle * (now - self.before)


	def cal(self, salary, week_working_hours):

		one_SEC_salary = salary / (60 * 60 * 24 * self.days)
		return one_SEC_salary

	def get_time(self):
		now = time.time()
		if now:
			self.base += self.sigle
			self._base = self.base
		self.clock_frame.config(text=("%.3f" % self.base))
		self.clock_frame.after(1000, self.get_time)


	def main(self):

		self.get_time()
		
		while 1:
			try:
				self.root.mainloop()
			except KeyboardInterrupt:
				self.root.quit()
				self.f.seek(0)
				self.f.write(str(time.time()) + " " + str(self.base) + " " + str(40) + "\n")
				self.f.close()
				sys.exit(0)


def get_val():

	parser = argparse.ArgumentParser(description=__doc__)
	parser.add_argument("--s", type=float, help='monthly salary netto')
	parser.add_argument("--wwh", type=int, help='weekly working hours')
	args = parser.parse_args()
	return args.s, args.wwh

if __name__ == '__main__':

	app = App()
	app.main()
