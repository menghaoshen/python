# 内置的类 list tuple set
nums = [9, 8, 4, 3, 2, 1]
x = tuple(nums)  # 使用tuple 内置类转换成元组
print(x)

y = set(nums)  # 使用set 内置类转换成集合
print(y)

z = list({'name': 'zhang', 'age': 18, 'score': 98})  # 使用list 内置的类把字典转换成列表
print(z)

# python 里面有一个比较强大的内置函数eval ，可以执行字符串里面的代码
# a = 'input("请输入您的用户名")'  # a 是一个字符串
b = '1 + 1'

# print(eval(a))  # 执行字符串里面的代码
print(eval(b))  # 执行1+1

#json 的使用，把列表，元组，字典，转换成json字符串 json 里面的字符串只能用双引号
import  json
person = {'name': 'zhang', 'age': 18, 'score': 98}
m = json.dumps(person)  #dumps 将字典，列表，集合，元组，等转换成json字符串
print(m)
# print(m['name']) #不能这样使用 m是个字符串 ，不能在向字典一样根据key获取value

# n = '{"name": "zhang", "age": 18, "score": 98}'
n = '["hello","good"]'
# p = eval(n) #也可以转换成字典
# print(p)
s = json.loads(n)   #将loads 可以将json字符串转换成python里面的数据
print(s)


#python                 json
#字符串                   字符串
#字典                     对象
#列表，元组                数组