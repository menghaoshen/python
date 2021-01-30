#使用bool内置类可以将其他数据类型转换成为布尔值
print(bool(100)) #将数字转换成为布尔值
print(bool(-1)) #-1转换成为布尔值也是True
print(bool(0)) #False

#数字里，只有数字0 被转换成布尔值是False，其他数字转换成为布尔值都是True

print(bool('hello')) #True
print(bool('False')) #True
print(bool('')) #False
print(bool("")) #False
#字符串里，只有空字符串'' "" 可以转换成为False，其他字符串都转成True

#None 转换成布尔值False
print(bool(None)) #False
print(bool("None")) #True

print(bool([])) #False
print(bool({})) #False
print(bool())   #False
s = set() #空集合
print(bool(s)) #False

#在python里面 数字0，空字符串'' "" 空列表[],空元组(),空字典{}，空集合set{}，空数据None，会被转换成False，其他都是True
#在计算机里面，True和False其实都是说字1和0来保存
#在计算机里面，True和False其实都是说字1和0来保存

print(True + 1) #2
print(False + 1) #1

#隐式类型转换
if 1: #0 不会打印，1或者别的数字都可以打印
    print(hello)