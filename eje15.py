def intercambio(x,y):
	print 'Funcion Original'
	print 'x = ',
	print x
	print 'y = ',
	print y

	temporal = x
	x = y
	y = temporal

	print 'Intercambio'
	print 'x = ',
	print x
	print 'y = ',
	print y

x=input('Ingrese X: ')
y=input('Ingrese Y: ')
intercambio(x,y)