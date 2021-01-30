# 在python里面一个py文件，就可以理解理解为模块
# 不是所有的py文件都能作为一个模块来导入
# 如果想让一个py文件能够被导入，模块名字必须遵守命名规则
# python 为了方便我们开发，内置了很多模块

# 使用import 模块名的方式，导入一个模块
import time

# 2. from 模块名 import 函数名，导入一个模块里的方法，或者变量
from random import randint  #

print(randint(0, 2))  # 0,2的随机整数

# 3. 导入这个模块里面的所有变量和方法

from math import *

print(pi)  # 不用写模块名了

# 4,导入一个模块，并给这个模块起个别名
import datetime as dt  # dt 就代表datetime 了

print(dt.MAXYEAR)

# 5. 给函数起个别名
from copy import deepcopy as dp

dp('hello', 'good', [1, 2, 3], 'hi')

