import argparse
import time
import sys
import os
import tkinter as tk


ODD = [1, 3, 5, 7, 8, 10, 12]

sys.path.append(os.path.realpath('..'))

class App():

    def __init__(self):

        self.f = open('log.txt', 'r+')
        self.first_line = self.f.readline()
        self.alist = self.first_line.split()
        
        self.initial, self.before, self.base, self.hours, self.salary, self.starter = int(self.alist[0]), float(self.alist[1]), float(self.alist[2]), float(self.alist[3]), float(self.alist[4]), str(self.alist[5])
        #self.before, self.base, self.hours, self.salary, self.starter = float(self.alist[0]), float(self.alist[1]), float(self.alist[2]), float(self.alist[3]), str(self.alist[4])#, str(self.alist[5])

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
                if (time.localtime(now)[0] % 4 == 0 and time.localtime(now)[0] % 100 != 0) or time.localtime(now)[0] % 400 == 0:
                    self.days = 29
                else:
                    self.days = 28
            else:
                self.days = 30

        self.single = self.cal(self.salary, self.hours)

        if now != self.before:
            self.base += self.single * (now - self.before)

        if self.initial=='0':
            hello()

    def hello(self):
        pass

    def cal(self, salary, week_working_hours):

        one_SEC_salary = salary / (60 * 60 * 24 * self.days)
        return one_SEC_salary

    def get_time(self):
        if time.time() - self.before > 0:
            self.base += self.single
        else:
            self.base = 0
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
                self.f.write(str(time.time()) + " " + str(self.base) + " " + str(40) + "\n") + "2020-08-28"
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
