nums = [6, 5, 3, 1, 8, 7, 2, 4]

# 冒泡排序的思想
# 让一个数字和它相邻的下一个数据进行比较运算
# 如果前一个数字大于后一个数字，交换两个数据的位置


# 最后一个比较应该是
# nums[length -2 ] nums [length -1 ]

# 每一趟比较次数的优化
# 总比较趟数的优化

i = 0
count = 0

#第一趟比较时候i=0 没有多比较
#第二趟比较时候j=1,多比较1次
#第二趟比较时候j=2,多比较2次
while i < len(nums) - 1:
    flag = True  # 有序标记，每一轮的初始是true，用于判断元素间是否需要交换 ，假设每一趟都没有换行
    n = 0
    while n < len(nums) - 1 -i :  # 每趟的优化
        # print(nums[n], nums[n + 1])
        count += 1

        if nums[n] > nums[n + 1]:
            #只要数据发生了交换，假设就不成立
            nums[n], nums[n + 1] = nums[n + 1], nums[n]  # 有交换行为设为 False
            flag = False
        n += 1
    if flag:  # 无交换行为（flag = True），直接跳过本次循环
        break #每一趟走完以后，flag没有倒，说明这一趟没有进行数据交换
    i += 1
print(nums)

print('循环了%d次'%count)