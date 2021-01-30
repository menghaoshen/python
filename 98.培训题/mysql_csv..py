# 通过 python 读取数据库并将读取的数据写入 csv。

import csv
import mysql.connector
mydb = mysql.connector.connect(
    host='192.168.13.33',  # host
    user='root',  # user
    passwd='XBsj.1234',  # passwd
    database='test'  # database
)

#获取数据库里面的数据
mycursor = mydb.cursor()
sql = "select * from sites"
mycursor.execute(sql)
data = mycursor.fetchall()
mydb.close()

# 打开csv文件，并写入
with open('./mysql_data.csv', 'w', encoding='utf8', newline='') as csvfile:
    w = csv.writer(csvfile)
    d = ['name','url','id']
    w.writerow(d)
    w.writerows(data)
csvfile.close()
