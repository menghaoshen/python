import sys

sys.stdin  # 接收用户的输入
sys.stdout  # 标出输出
sys.stderr  # 错误输出

# s_in = sys.stdin
# while True:
#     content = s_in.readline().rstrip('\n')
#     if content == '':
#         break
#     print(content)

#将日志打印到文件
sys.stdout = open('logs.txt','w',encoding='utf8')
print('hello')
print('hello')

#将错误日志输出到文件
sys.stderr = open('err.log','w',encoding='utf8')
print(1 / 0)
