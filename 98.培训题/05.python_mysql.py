# 1.5 通过 python 连接数据库
# 作业：
# 准备工作：自行创建 mysql 数据库并写入数据
# 1、通脱 python 连接数据库，做到能够使用 python 增删查改数据。
# 2、通过 python 读取数据库并将读取的数据写入 csv。
# python -m pip install mysql-connector
import mysql.connector

# 连接数据库
mydb = mysql.connector.connect(
    host='192.168.13.33',  # host
    user='root',  # user
    passwd='XBsj.1234',  # passwd
    database='test'  # database
)

mycursor = mydb.cursor()

# 创建数据库
# mycursor.execute('create database test')


# 创建数据表
# mycursor.execute('create table test.sites (name varchar(255),url varchar(155))')

# 查看表
# mycursor.execute('show tables')
# for table in mycursor:
#     print(table)

# 给表增加主键
# mycursor.execute('alter table sites add column id int auto_increment primary key')

# 插入数据
# sql = 'insert into sites (name,url) values (%s,%s)'
# varl = ('baidu','https://www.baidu.com')
# mycursor.execute(sql,varl)
# mydb.commit()


# 批量插入
# sql = "insert into sites (name,url) values (%s,%s)"
# val = [
#     ('google', 'https://www.google.com'),
#     ('github', 'https://www.github.com'),
#     ('Taobao', 'https://www.taobao.com')
# ]
# mycursor.executemany(sql, val)
# mydb.commit()
# print(mycursor.rowcount,'记录插入成功')

# 查询数据
# mycursor.execute('select name,url from sites ')
# myresult = mycursor.fetchall() #获取所有的记录
# for data in myresult:
#     print(data)
#
# mycursor.execute('select name,url from sites ')
# myresult = mycursor.fetchone() #查看一条数据
# print(myresult)

# 查询指定的数据
# mycursor.execute('select * from sites where name = "baidu"')
# myresult = mycursor.fetchall()
# print(myresult)

#使用通配符
# print('-------->')
# sql = 'select *from sites where url like "%oo%"'
# mycursor.execute(sql)
# myresult = mycursor.fetchall()
# for data in myresult:
#     print(data)

# 使用order by 排序
# sql = "select * from sites order by name"
# mycursor.execute(sql)
# myresule = mycursor.fetchall()
# for data in myresule:
#     print(data)

# 降序排序
# sql = "select * from sites order by name desc"
# mycursor.execute(sql)
# myresult = mycursor.fetchall()
#
# for x in myresult:
#     print(x)

#limit 限制代码的输出
# mycursor.execute("select * from sites limit 3")
# myresult = mycursor.fetchall()
#
# for x in myresult:
#     print(x)
#
#删除记录

# sql = "delete from sites where name = 'Google'"
# mycursor.execute(sql)
# mydb.commit()
# print(mycursor.rowcount,"条记录被删除了")

#更新表数据
# sql = 'update sites set name = "ZH" where id = 1 '
# mycursor.execute(sql)
# mydb.commit()
# print(mycursor.rowcount,"条记录被修改了")


#删除表
sql = 'drop table if exists test1' #删除表
mycursor.execute(sql)

#