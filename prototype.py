import argparse
import time
import sys
import os
import tkinter as tk

from test import get_epoch_time


ODD = [1, 3, 5, 7, 8, 10, 12]

sys.path.append(os.path.realpath('..'))

class App():

    def __init__(self):

        self.f = open('log.txt', 'r+')
        self.first_line = self.f.readline()
        self.base = 0
        self.days = self.get_days_in_month()
        self.initial = 0
        self.before = 0

        if len(self.first_line) == 0:
            self.hello()
            self.initial = 1
        else:
            self.alist = self.first_line.split()
            self.initial, self.before, self.base, self.hours, self.salary, self.starter = \
            int(self.alist[0]), float(self.alist[1]), float(self.alist[2]), float(self.alist[3]), float(self.alist[4]), str(self.alist[5])
            self.single = self.cal(self.salary, self.hours)
            self.root = self.ui_window()

    def ui_window(self):

        self.root = tk.Tk()
        self.root.title('Salary Counter')
        self.root.geometry('400x150')
        self.clock_frame = tk.Label(self.root, font=('times', 50, 'bold'), bg='black', fg='white')
        self.clock_frame.pack(fill='both', expand=1)
        return self.root

    def get_days_in_month(self):

        self.now = time.time()

        if time.localtime(self.now)[1] in ODD:
            days = 31
        else:
            if time.localtime(self.now)[1] == 2:
                if (time.localtime(self.now)[0] % 4 == 0 and time.localtime(self.now)[0] % 100 != 0) or time.localtime(self.now)[0] % 400 == 0:
                    days = 29
                else:
                    days = 28
            else:
                days = 30

        return days 

    def hello(self):

        salary = float(input('How much you earn monthly after tax?: '))
        hours = int(input('How many hours you work monthly?: '))
        print("When do you offically start your job?")
        year = int(input("Which year?: "))
        month = int(input("Which month?: "))
        day = int(input("Which day?: "))

        time_string = str(year)+"-"+str(month)+"-"+str(day)        
        now = time.time()
        start = get_epoch_time(time_string)

        self.f.write(str(self.initial) + " " + str(time.time()) + " " + str(self.base) + " " + str(hours) + " " + str(salary) + " " + time_string)
        self.f.close()

    def cal(self, salary, week_working_hours):

        one_SEC_salary = salary / (60 * 60 * 24 * self.days)
        return one_SEC_salary

    def get_time(self):

        if time.time() - get_epoch_time(self.starter) > 0 and self.before > get_epoch_time(self.starter):
            self.base = self.single * (time.time() - get_epoch_time(self.starter))
        else:
            self.base = 0
        self.base += self.single
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
                self.f.write(str(self.initial) + " " + str(time.time()) + " " + str(self.base) + " " + str(39) + " " + str(self.salary) + " " + "2020-09-01 ")
                self.f.close()
                sys.exit(0)


    def make_decision(self):
        #TODO
        #to remeber the running times and also the initial question for writting the file later
        pass


def get_val():

    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--s", type=float, help='monthly salary netto')
    parser.add_argument("--wwh", type=int, help='weekly working hours')
    args = parser.parse_args()
    return args.s, args.wwh

if __name__ == '__main__':

    app = App()
    app.main()
