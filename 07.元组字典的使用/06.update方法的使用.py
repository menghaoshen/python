# 列表可以使用extend方法将两个列表合并成为一个列表
nums1 = [1, 2, 3, 4]
nums2 = [5, 6, 7]
print(nums2 + nums1)
# nums1.extend(nums2)
# print(nums1)

# 元组可以用加法
word1 = ('hello', 'good')
word2 = ('yes', 'ok')
w1 = (word1 + word2)  # 原有的值没有改变
print(w1)
# 字典和合并,字典之间不能用+法
person1 = {'name': 'zhangsan', 'age': 18}
person2 = {'addr': 'zmd', 'height': 180}

person1.update(person2)
print(person1)
