import shutil
import os
from database import DB


server='10.10.240.45'
user='ZLYY'
password='ZLYY'
database='medexmemrs'
db = DB(server, user, password, database)
message = db.get_data()
print(len(message))
db.close()

dst_path = r'I:\\download'

paths = [one[2] for one in message]
paths = [path[:len(path)-1] for path in paths]
# paths = [path.replace('E', 'N') for path in paths]
paths = [path.replace('m', 'M') for path in paths]

for ite, path in enumerate(paths):
	if 'N:' in path or 'n:' in path:
		continue
	basename = os.path.basename(path)
	# part = path.replace('N:\\US\\','')
	part = path[6:]
	k = part.rfind('\\')
	middle_name = part[:10]
	src = path
	dst = os.path.join(dst_path, middle_name,  basename)
	try:
		print('no.{} copy {} to {}'.format(ite+1, src, dst))
		shutil.copytree(src, dst)
	except Exception as e:
		print(e)
		print("error path: {}".format(src))