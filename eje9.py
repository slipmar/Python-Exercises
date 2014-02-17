import datetime

def dateFormat():
	d = datetime.datetime.now()
	print d.date().strftime("%d/%m/%y")
	print d.date().strftime("%m/%d/%y")
	print d.date().strftime("%y/%m/%d")
	print d.date().strftime("%A %d. %B %Y")
	
