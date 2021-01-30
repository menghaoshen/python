#in 和not in 运算符
#用来判断一个内容在可迭代对象里面是否存在

word = 'hello'
x = input('请输入一个字符')

#判断用户输入的字符是否存在
# for c in word:
#     if x in c:
#         print('您输入的字符存在')
#         break
# else:
#     print('你输入的字符串不存在')
# if word.find(x) == -1:
#     print('不存在')
# else:
#     print('存在')

if x in word:
    print('存在')
else:
    print('不存在')
