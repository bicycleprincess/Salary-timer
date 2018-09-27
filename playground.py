PATH = u'/Users/yangwei/ENV/iphone_app/'
with open(PATH +'log.txt', 'r+') as f:
	first_line = f.readline()
	alist = first_line.split()
	month, money, hours = alist[0], float(alist[1]), int(alist[2])
	#print money, month, hours
	f.seek(0)
	f.write('102018 2092.10 40 \n')
	f.write(first_line)
f.close()