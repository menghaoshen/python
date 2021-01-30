nums = [4, 8, 2, 1, 7, 6]
#列表的sort方法，会对列表进行排序
nums.sort()
print(nums)

# sorted 内置函数，不会改变原有的数据，而是生产一个新的结果
ints = (5,9,1,3,5,8,7,4)
x = sorted(ints)
print(x)

students = [
    {'name':'zhansan','age':18,'score':98,'height':180},
    {'name':'lisi','age':19,'score':95,'height':185},
    {'name':'wanwu','age':18,'score':85,'height':170},
    {'name':'jack','age':20,'score':80,'height':175}
]
#字典和字典直接不能使用比较运算
# students.sort()
#没有比较规则，需要传递key
#key是一个函数
def foo(ele):
    # print(x)
    return  ele['age'] #t通过返回值告诉sort方法，按照元素的那个属性进行排序
students.sort(key=foo)
print(students)

#用lambda 写
students.sort(key=lambda ele:ele['score'])
print(students)
