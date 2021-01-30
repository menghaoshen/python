# 有一个列表names，保存了一组姓名names = ['zhansan','lishi','chris','jerry','henry']

# names = ['zhansan', 'lishi', 'chris', 'jerry', 'henry']
# username = input('请输入一个用户名')
# if username in names:
#     print('用户名已经存在')
# else:
#     names.append(username)
# print(names)

# 用遍历的方法写
# for name in names:
#     if username == name:
#         print('用户名已经存在')
#         break
# else:
#     names.append(name)
# print(names)

# 统计列表里面出现次数最多的元素
# 求列表里面的最大数
nums = [3, 1, 9, 8, 4, 2, 0, 7, 5]
# nums.sort()
# print(nums[-1])
# nums.sort(reverse=True)
# print(nums[0])

# 用假设的方法
# x = nums[0]
# for num in nums:
#     if num > x:  # 如果发现列表里存在比假设还要大的数字
#         # 说明假设不存在，把假设的值设置为为发现的数字
#         x = num
# print('发现最大数%d，它的下标是%d' % (x, nums.index(x)))

#不用idnex方法找到下标
i = 0
x = nums[0]
inde = 0
while i < len(nums):
    if nums[i] > x:
        x = nums[i]
        index = i
    i += 1
print('发现的最大数是%d,它的下标是%d' %(x,index))