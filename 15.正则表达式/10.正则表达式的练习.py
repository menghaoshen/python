# 判断用户的输入判断是否是数字，如果是数字转换成为数字类型
import  re
#\d+ \.? \d+ #匹配数字
# num = input('请输入一段数字：')
# # if num.isdigit():  #小数判断不了 ? 零次到或者1次
# if re.fullmatch(r'\d+(\.\d+)?',num): #fullmatch 匹配整个字符串
#     print(float(num))
# else:
#     print('不是一个数字')

#以非数字开头，后面有字母数字_ 组成的长度4到14位，并且不能以数字开头
# r'^\D[a-z0-9A-Z_\-]{3,13}'
x = re.match(r'^\D[a-z0-9A-Z_\-]{3,13}','j3pqtr')
print(x)
#匹配邮箱


