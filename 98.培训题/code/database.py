
class DB:
    def __init__(self,server, user, password, database):
        # server    数据库服务器名称或IP
        # user      用户名
        # password  密码
        # database  数据库名称
        import pymssql
        self.conn = pymssql.connect(server, user, password, database)
        self.cursor = self.conn.cursor()

    def get_data(self):
        # 查询操作
        self.cursor.execute("select * from dbo.v_xbsj")
        self.rows = self.cursor.fetchall()
        return self.rows

    def close(self):
        # 关闭连接
        self.conn.close()