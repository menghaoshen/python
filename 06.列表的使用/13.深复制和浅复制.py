# 浅复制
import copy

nums = [1, 2, 3, 4, 5]
nums1 = nums  # 这是一个赋值

nums2 = nums.copy()  # 浅拷贝，，两个内容一模一样，但是不是同一个对象
nums3 = copy.copy(nums)  # 和nums.copy 功能一致，都是浅拷贝

# 深拷贝，只能使用copy模块实现
# 浅拷贝了只拷贝了一层，只拷贝了外层，内层没有拷贝
words = ['hello', 'good', [100, 200, 300], 'yes', 'hi', 'ok']
words1 = words.copy() #浅拷贝
words2 = copy.deepcopy(words) #深拷贝

words[0] = '你好'
print(words1)

words[2][1] = 1
print(words1)

print(words2)