#序列化，将数据从内存持久化保存到硬盘的过程
#反序列化：将数据从硬盘加载到内存的过程


#write 时，只能写入字符串或者二进制
#字典，列表，数字，都不能直接写入到文件里

#将数据转换成字符串 repr/str  使用json模块
#json 本质就是字符串，区别在于json里要使用双引号表示字符串
#将数据转换成二进制，使用pickle 模块

# file = open('name.txt','w',encoding='utf8')
# name = ['zhangsan','lishi','jack']
# file.write(str(name))
# file.close()

#使用json
# json 里将数据持久化有两个方法
# json.dumps 的作用是将数据转换成为字符串，不会保存到文件里面
# josn.dump  将数据转换成字符串，同时写入到指定文件
# import  json
# names = ['zhangsan','lishi','jack']
# x = json.dumps(names)
# file = open('name.txt','w',encoding='utf8')
# file.write(x)
# file.close()

#dump
# import  json
# names = ['zhangsan','lishi','jack']
# file = open('name.txt','w',encoding='utf8')
# json.dump(names,file)
# file.close()

#json 反序列化，也有两个方法
# loads 将json字符串加载成为python里面的数据
# load  读取文件，把读取的内容加载成为python里的数据
import json
#loads
name  = '{"name":"zhangsan","age":"18"}' #复合json规则的字符串
p = json.loads(name)
print(type(p)) #字符串变为字典
# load

#load 读取一个文件，并把文件里面的json字符串加载成为一个对象
file1 = open('name.txt','r',encoding='utf8')
x = json.load(file1)
print(x)
print(x[0])
file1.close()