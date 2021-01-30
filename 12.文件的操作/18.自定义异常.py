# 系统异常
# ZeroDivisionError 1/0 的异常
# FileNotFoundError  文件不存在
# ValueError  # key 不存在
# KeyError  int('hello')
# FileExistsError 文件已经存在的异常
# SyntaxError  中英文符号不对称
# IndexError  下标错误

# 要求：让用户名输入用户名和密码，如果用户名和密码的长度在6~12位正确，否则不正确
#自定义异常的类，可以放到文件里面，import调用
class MyError(Exception):
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __str__(self):
        return '长度必须要在{}和{}之间'.format(self.x,self.y)

password = input('请输入密码')
m = 6
n = 12
if m <= len(password) <= n:
    print('密码正确')
else:
    # print('密码不正确')
    # 使用raise 关键字可以抛出一个异常
    raise MyError(m,n)

# 把密码保存到数据库里面
print('讲密码保存到数据里面')
