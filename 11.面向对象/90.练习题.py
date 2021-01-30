#编写一个函数，求最大数
def get_max(*args):
    x = args[0]
    for arg in args:
        if arg > x:
            x = arg
    return x


print(get_max(1, 5, 8, 9))

#编写一个函数，实现摇骰子的功能，打印N个骰子的点数和
import  random
def get_sum(n):
    m = 0
    for i in range(n):
        x = random.randint(1,6)
        m += 1
    return m
print(get_sum(5))

# 编写一个函数，提取指定字符串中所有的字母，然后拼接在一起产生一个新的字符串
def get_alphas(word):
    new_str = ''
    for w in word:
        if w.isalpha():
            new_str += w
    return  new_str

print(get_alphas('hwlllo123dfsa323'))