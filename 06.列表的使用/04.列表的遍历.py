# 遍历就是将所有的数据数据都访问一遍，遍历针对的是可迭代对象
# while 循环，/ for .. in 循环

killers = ['李白','兰陵王','韩信','赵信','阿珂','孙悟空']

#for.. in 循环的本质就是不断调用next 方法，查找下一个数据
for killer in killers:
    print(killer)

i = 0
while i < len(killers):
    print(killers[i])
    i += 1
