#break 和continue 在python里面只能用在循环语句里面

#break：用来结束整个循环
#continue：用来结束本轮循环，开启下一轮循环

# i = 0
# while i < 5:
#     if i == 3:
#         i += 1
#         continue
#     print(i)
#     i += 1

#不断询问用户，我爱你，你爱我么？ 只要答案不是，就一直问，直到答案是爱
# answer = input('我爱你，你爱我么？')
# while answer != '爱':
#     answer = input('我爱你，你爱我么？')
#优化




#不断让用户输入用户名和密码，只要用户名不是zhansan，密码不是123 就一直问
# username = input('请输入用户名：')
# passw = input('请输入密码')

# while not(username == '张三' and passw == '123'):
#     username = input('请输入用户名：')
#     passw = input('请输入密码')

#优化

while True:
    username = input('请输入用户名：')
    passw = input('请输入密码:')
    if username == '张三' and passw == '123':
        break
