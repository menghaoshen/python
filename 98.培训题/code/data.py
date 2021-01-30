# encoding:utf8
import csv
from database import DB


def csv_(path, data):
	with open(path, 'w', newline='') as csvfile:
		writer = csv.writer(csvfile)
		for row_i, row_values in enumerate(data):
			writer.writerow(row_values)
		print('save to {}'.format(path))


server='10.10.240.45'
user='ZLYY'
password='ZLYY'
database='medexmemrs'
path = r'I:\\reports.csv'
db = DB(server, user, password, database)
message = db.get_data()
print(len(message))
csv_(path, message)
db.close()