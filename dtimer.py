import time
import Tkinter as tk

import argparse
#WORKING_DAYS = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri']

def tick(time1=''):
	#time2 = time.strftime('%I:%M:%S')
	time2 = time.strftime("%a, %d %b %Y %H:%M:%S", time.gmtime())
	#print time2[:3]€
	if time2 != time1:
		time1 = time2
		#clock_frame.config(text=time2)
		clock_frame.config(text='hello')
	clock_frame.after(200, tick)

root = tk.Tk()
root.title('Digital Clock')
clock_frame = tk.Label(root, font=('times', 50, 'bold'), bg='black', fg='green')
clock_frame.pack(fill='both', expand=1)
root.geometry('800x500')
tick()
root.mainloop()

