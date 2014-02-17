import codecs
import datetime
import os

def create(pathOut):
	filename = r'data'
	filename += datetime.datetime.now().strftime('_%H_%M_%d_%m_%Y_')
	filename += ".txt"

	p = os.path.join(pathOut, filename)

	f = open(p, 'w')

	s = 'just example'
	f.write(s)