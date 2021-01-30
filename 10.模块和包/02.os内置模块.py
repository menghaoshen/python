#os,模块里面提供的方法，就是调用操作系统里面的方法
import  os
print(os.name) #获取操作系统的名字
print(os.sep)  #分隔符
print(os.path)
print(os.path.abspath('01.导入模块的语法.py')) #绝对路径
print(os.path.isdir('10.模块和包')) #判断是否一个文件夹
print(os.path.isfile('xx.txt')) #判断是否是个文件
print(os.path.exists('01.导入模块的语法.py')) #判断是否存在
print(os.path.splitext('2020.2.21.18.demo.py')) #('2020.2.21.18.demo', '.py')

#os 的其他方法
os.getcwd() #获取当前的工作目录
os.chdir('/home') #改变当前的工作目录
os.listdir('/home/menghao') #列出所有的文件和文件夹。默认是当前的目录的文件和文件夹
os.rename('1.txt 2.txt') #修改文件名
os.remove('1.txt') #删除文件
os.rmdir('demo') #删除空文件夹
os.removedirs('demo') #删除空文件夹
os.mkdir('demo') #创建文件夹
os.chdir('/home') #切换工作目录
os.environ #获取环境变量
os.environ.get('PATH') #获取指定的环境配置
#os path 我们经常使用
print(os.path.abspath('高阶函数.py'))  #拿到绝对路径
print(os.path.isdir('高阶函数.py')) #判断是否是文件夹
print(os.path.isfile('xxx')) #判断是否是个文件
print(os.path.exists('1-100.py')) #判断是否存在
print(os.path.splitext('2020.2.21.demo.py'))#文件切割，切割出脚本后缀