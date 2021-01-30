#pip install requests 是第三方的模块，可以用来发送网络连接
import  requests

response =  requests.get('http://localhost:9999/')
# print(response)  #结果是一个response对象

#content 指的是返回结果，是一个二进制
# print(response.content.decode('utf8'))

# 获取的结果就是一个文本
# print(response.text)
#
# print(response.status_code) #获取状态码

r = requests.get('http://localhost:9999/test')
t = r.text  #获取到json字符串
print(t,type(t))

j = r.json() #把josn 字符串解析成python里的对应的数据类型

print(type(j))
