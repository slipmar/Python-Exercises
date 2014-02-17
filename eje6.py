import math
import sys

def add(op1, op2):
	return op1+op2

def sub(op1, op2):
	return op1-op2

def mul(op1, op2):
	return op1*op2

def div(op1, op2):
	return op1/op2

def sqrr(root, rad):
	return math.pow(rad,1.0/root)

def sqr(rad):
	return math.sqrt(rad)

def cub(rad):
	return math.pow(rad,1.0/3)

def sin(degrees):
	return math.sin(degrees)

def cos(degrees):
	return math.cos(degrees)

def tan(degrees):
	return math.tan(degrees)

def fact(op1):
	return math.factorial(op1)

def inv(op1):
	return 1/op1

def mod(op1, op2):
	return op1%op2


flag = True

while flag:
	try:
		print 'Calculator in Python'
		print ' '
		print 'Select an operation you want to perform (by number)'
		print '	1 - Addition'
		print '	2 - Substraction'
		print '	3 - Multiplication'
		print '	4 - Divition'
		print '	5 - Square-root'
		print '	6 - Square'
		print '	7 - Cube'
		print '	8 - Sine'
		print '	9 - Cosise'
		print '	10 - Tangent'
		print '	11 - Factorial'
		print '	12 - Inverse'
		print '	13 - Modulo'
		print ' '
		option = input('Option : ')
		print ' '

		if option == 1:
			op1 = input('First operand : ')
			op2 = input('Second operand : ')

			print op1,
			print ' + ',
			print op2,
			print ' = ',
			print add(op1,op2)

		if option == 2:
			op1 = input('First operand : ')
			op2 = input('Second operand : ')

			print op1,
			print ' - ',
			print op2,
			print ' = ',
			print sub(op1,op2)

		if option == 3:
			op1 = input('First operand : ')
			op2 = input('Second operand : ')

			print op1,
			print ' * ',
			print op2,
			print ' = ',
			print mul(op1,op2)

		if option == 4:
			op1 = input('First operand : ')
			op2 = input('Second operand : ')

			print op1,
			print ' / ',
			print op2,
			print ' = ',
			print div(float(op1),float(op2))

		if option == 5:
			op1 = input('Root : ')
			op2 = input('Operand : ')

			print op2,
			print ' ^ (1/',
			print op1,
			print ') = ',
			print sqrr(float(op1),float(op2))

		if option == 6:
			op1 = input('Operand : ')

			print ' sqrt(',
			print op1,
			print ') = ',
			print sqr(float(op1))

		if option == 7:
			op1 = input('Operand : ')

			print op1,
			print ' ^ (1/3) = ',
			print cub(float(op1))

		if option == 8:
			op1 = input('Radians : ')

			print 'Sin(',
			print op1,
			print ') = ',
			print sin(float(op1))

		if option == 9:
			op1 = input('Radians : ')

			print 'Cos(',
			print op1,
			print ') = ',
			print cos(float(op1))

		if option == 10:
			op1 = input('Radians : ')

			print 'Tan(',
			print op1,
			print ') = ',
			print tan(float(op1))

		if option == 11:
			op1 = input('N : ')

			print op1,
			print '! = ',
			print fact(float(op1))

		if option == 12:
			op1 = input('Operand : ')

			print '1/',
			print op1,
			print ' = ',
			print inv(float(op1))

		if option == 13:
			op1 = input('First operand : ')
			op2 = input('Second operand : ')

			print op1,
			print ' % ',
			print op2,
			print ' = ',
			print mod(float(op1),float(op2))

		if option < 1 or option > 13:
			print 'Option not valid!'

		print ' '
		answer = input('Do you want to calculate again (y/n) ')

		if answer == 'n':
			flag = False
		print ' '

	except:
		print "Unexpected error: ", sys.exc_info()[0]
		print ' '
