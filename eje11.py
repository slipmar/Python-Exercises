import csv
import os
from bs4 import BeautifulSoup

def tablehtmltotxt(tableIn, pathOut):
	soup = BeautifulSoup(tableIn)
	table = soup.find('table')
	headers = [header.text for header in table.find_all('th')]

	rows = []
	for row in table.find_all('tr'):
		rows.append([val.text.encode('utf8') for val in row.find_all('td')])

	filename = r'output_file.csv'
	p = os.path.join(pathOut, filename)

	with open(p, 'wb') as f:
		writer = csv.writer(f)
		writer.writerow(headers)
		writer.writerows(row for row in rows if row)

