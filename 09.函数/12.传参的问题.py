def test(a):
    a  = 100

def demo(nums):
    nums[0] = 10

x = 1
test(x)
print(x) #字符串是是不可变的数据类型

y = [3,5,6,8,2]
demo(y)
print(y) #[10, 5, 6, 8, 2]  列表是可变的数据类型