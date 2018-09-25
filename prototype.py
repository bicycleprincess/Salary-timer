import argparse
import time
import Tkinter as tk

WORKING_DAYS = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri']

BASE = 2092.

def get_time():
	global BASE
	global sigle
	sigle = cal(2092., 40.)
	time1 = ''
	time2 = time.strftime("%a. %d %b %Y %H:%M:%S", time.gmtime())
	#if time2[:3] in WORKING_DAYS:
	if time2[:3] in WORKING_DAYS:
		if time2[-9:-6] <= 17 or time2[-9:-6] >= 10:
			if time2 != time1:
				#time1 = time2
				BASE += sigle
				#clock_frame.config(text=BASE)
				#clock_frame.config(text=time2)
				clock_frame.config(text=("%.2f" % BASE))
			clock_frame.after(200, get_time)

def cal(salary, week_working_hours):
	one_SEC_salary = salary / (60*60*week_working_hours*4)
	return one_SEC_salary

def get_val():

	parser = argparse.ArgumentParser(description=__doc__)
	parser.add_argument("--s", type=float, help='monthly salary netto')
	parser.add_argument("--wwh", type=int, help='weekly workong hours')
	args = parser.parse_args()
	return args.s, args.wwh

if __name__ == '__main__':

	#sigle = cal(2092., 40.)
	#print sigle
	root = tk.Tk()
	root.title('Digital Clock')
	root.geometry('800x500')
	
	clock_frame = tk.Label(root, font=('times', 50, 'bold'), bg='black', fg='green')
	clock_frame.pack(fill='both', expand=1)
	get_time()
	root.mainloop()

