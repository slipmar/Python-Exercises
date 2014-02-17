def sortASC():
	counter = 1
	print 'Escribe diez números o cadenas (sólo tienes que seleccionar un tipo de datos): '
	list = []

	while counter != 10:
		a = input('Value = ')
		list.append(a)
		cont += 1

	list.sort()
	print list



def sortDESC():
	counter = 1
	print 'Escribe diez números o cadenas (sólo tienes que seleccionar un tipo de datos): '
	list = []

	while counter != 10:
		a = input('Value = ')
		list.append(a)
		counter += 1

	list.sort()
	list.reverse()
	print list
