from math import ceil
import string

def roundup(number):
	num = ceil(number*100000)/100000.0
	print num

def truncate(number):
	print '%.2f' % number

def zeroL(number, numberZeros):
	print str(number).zfill(numberZeros)

def zeroR(number, numberZeros):
	print str(number).ljust(numberZeros,'0')

def justR(text):
	print string.rjust(text, len(text)+3)

def justL(text):
	print string.ljust(text, len(text)+3)
