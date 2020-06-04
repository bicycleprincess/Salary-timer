import argparse
import time, datetime
import Tkinter as tk

WORKING_DAYS = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri']

def cal():
	localtime = time.localtime(time.ti)
	print datetime.datetime(*localtime[:6])

def tick(*arg):
	time1=''
	#time2 = time.strftime('%I:%M:%S')
	time2 = time.strftime("%a. %d %b %Y %H:%M:%S", time.gmtime())
	if time2[:3] in WORKING_DAYS:
		if time2 != time1:
			time1 = time2

			clock_frame.config(text=time2)
			#clock_frame.config(text='hello')
		clock_frame.after(200, tick)

def get_val():

	parser = argparse.ArgumentParser(description=__doc__)
	parser.add_argument("-s", type=float, help="monthly salary netto")
	parser.add_argument("-wh", type=int, help="monthly workong hours")
	#TODO add log

	args = parser.parse_args()

	return args

def make_frame(text):
	root = tk.Tk()
	root.title('Digital Clock')
	clock_frame = tk.Label(root, font=('times', 50, 'bold'), bg='black', fg='green')
	clock_frame.pack(fill='both', expand=1)
	root.geometry('800x500')
	return root

if __name__ == '__main__':
	info = get_val()
	print info
	#screen = screen()
	tick(info)
	screen.mainloop()
