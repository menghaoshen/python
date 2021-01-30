#权限校验

user_permission = 15 #
# user_permission = 11 # 1101
DEL_PERMISSION = 8 #1000
READ_PERMISSION = 4 # 0100
WRITE_PERMISSION = 2 #0010
EXE_PERMISSION = 1  #0001
#权限因子

#用户权限 & 权限因子！=0 就是有权限 #& 运算同为1着为1


def check_permission(x, y):
    def handle_action(fn):
        def do_action():
            if x & y != 0: # 有权限，可以执行
                fn()
            else:
                print('对不起，您没有权限')
        return  do_action

    return handle_action

@check_permission(user_permission,READ_PERMISSION)
def read():
    print('我正在读取内容')

@check_permission(user_permission,WRITE_PERMISSION)
def write():
    print('我正在写入内容')

@check_permission(user_permission,EXE_PERMISSION)
def execute():
    print('我在执行内容')

@check_permission(user_permission,DEL_PERMISSION)
def delete():
    print('我正在删除东西')

execute()
delete()
write()
read()