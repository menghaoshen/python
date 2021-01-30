#一个模块本质上就一个一个py文件
# #如果一个py文件想要当作一个模块被导入，文件名一定要遵守命名规范
#由数字，字母下划线组成，不能以数字开头
import  sys
import  sys
sys.path.append("07.使用自定义模块.py")
import my_module as my
print(my.a)
my.test()
print(my.add(1, 2))

#使用from demo import * 写法不用在写模块名了
#本质是读取模块里的__all__属性，看这个属性里定义了那些变量和函数
#如果模块里面没有定义__all__ 才会导入，不以_开头的变量和函数
#用import demo 可以绕过__all__
from  demo import *
test()
# foo()

from hello import *

print(x)
print(y)
# print(_age) #这方法导入不了

import hello

#_ 一个下划线开始的变量，建议在本模块里面使用，别的模块无法调用，调用的时候可能出错
# print(hello._age)

#__name__ 的使用
print(dvi(5, 1))