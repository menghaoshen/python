# {}也可以进行占位
# {}什么都不会写,会读取后面的内容,一一填充对应
x = '大家好,我是{},我今年{}岁了'.format('张三', 18)
print(x)

# {数字},根据数字的顺序来进行填入,数字从0开始
y = '我是{1},我今年{0}岁了'.format(10, 'jerry')
print(y)

# 变量名
z = '大家好,我是{name},我今年{age}岁了,我来自{addr}'.format(age=18, name='jack', addr='地球')
print(z)

# 混合使用 {数字} {变量}
# name = 要写在最后面
a = '大家好,我是{name},我今年{1}岁了,我来来自{0}'.format('地球', 23, name='xiaobai')
print(a)
# {} {数字} 不能混合使用
d = ['zhangsan', '18', 'shanghai', 180]
# b = '大家好,我是{},我今年{}岁了,我来自{},我身高{}cm'.format(d[0],d[1],d[2],d[3])
b = '大家好,我是{},我今年{}岁了,我来自{},我身高{}cm'.format(*d)  # 会自动拆包

print(b)

info = {'name':'chis', 'age':13, 'addr':'北京', 'height':'190'}
c = '大家好,我是{name},我今年{age}岁了,我来自{addr},身高{height}cm'.format(**info)
print(c)
