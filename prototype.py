import time, datetime, Tkinter

def cal():
	localtime = time.localtime(time.time())
	print localtime, type(localtime), len(localtime)

	print datetime.datetime(*localtime[:6])


if __name__ == '__main__':
	#cal()
