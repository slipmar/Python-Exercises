def reynolds():
	d = input('Diametro : ')
	v = input('Velocidad : ')
	rho = input('Densidad : ')
	mu = input('Viscosidad : ')

	result = (d*v*rho)/mu
	print 'Número Reynold es ',
	print result

	if result < 2100:
		print 'Flujo laminar'
	elif result >= 2100 and result <= 4000:
		print ' flujo transitorio'
	else:
		print 'Flujo turbulento'
