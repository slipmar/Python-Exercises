			
def Fibonacci(num):
	if num ==0:
		print '0'
	
	if num==1:
		print '0 1'
		
	print '0 1'
	
	a=0
	b=1
	cont=2
	
	while cont<=num:
		temp=a
		a=b
		b=temp+b
		print b,
		cont +=1
	
num=input('Ingrese un numero')
Fibonacci(num)
	
	
	
	