#系统相关的方法
import  sys
print('hwllo')
# sys.exit() #退出 ，和内置函数exit 功能是一样的
print('world')

print(sys.path)   #结果是一个列表，表示查找模块的路径
# ['D:\\01.Work\\14.scripts\\python\\10.模块和包',
#  'D:\\01.Work\\14.scripts\\python',
#  'C:\\Users\\menghao\\AppData\\Local\\Programs\\Python\\Python37\\python37.zip',
#  'C:\\Users\\menghao\\AppData\\Local\\Programs\\Python\\Python37\\DLLs',
#  'C:\\Users\\menghao\\AppData\\Local\\Programs\\Python\\Python37\\lib',
#  'C:\\Users\\menghao\\AppData\\Local\\Programs\\Python\\Python37',
#  'C:\\Users\\menghao\\AppData\\Roaming\\Python\\Python37\\site-packages',
#  'C:\\Users\\menghao\\AppData\\Local\\Programs\\Python\\Python37\\lib\\site-packages']

sys.stdin #接受用户的输入
sys.stdout #可以改变默认输出位置
sys.stderr #可以改变错误输出的默认位置
