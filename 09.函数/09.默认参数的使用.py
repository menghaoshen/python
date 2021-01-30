# 缺省参数
# 有些函数的参数是：如果你传递了参数，就是用传递的参数
# 如果没有传递参数，就使用默认的值


# print函数里面end就是一个缺省参数
print('hello work', end='')
print('hi')


def say_hello(name, age, city='银河系地球'):  # 缺省产生要放在后面
    print('大家好，我是{}，我今年{}岁了,我来自{}'.format(name, age, city))  # 如果


say_hello('jack', 19, )  # 如果没有传递参数，会使用默认值
say_hello('tony', 20, '天马星系')  # 如果传递参数，就会使用传递的实参
say_hello(name='jerry', age=20, city='南京')  #如果传递参数，就使用传递的实参 一对一对的关键字参数

#如果有位置参数和关键字参数，关键字参数一定要放在位置参数的后面
say_hello('jerry', age=20, city='南京')  #
