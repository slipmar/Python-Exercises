def extractUppercase(pathIn):
	f = open(pathIn, 'r')
	s = f.read()
	list1=[]
	words=s.split()

	for w in words:
		temporalFlag = True
		for c in w:
			if c.isupper()==False:
				temporalFlag = False
				break

		if temporalFlag:
			list1.append(w)

	print list1

def extractUniquewords(pathIn):
	f = open(pathIn, 'r')
	s = f.read()
	list1=[]
	words=s.split()

	for w in words:
		if w in list1:
			continue
		else:
			list1.append(w)

	print list1