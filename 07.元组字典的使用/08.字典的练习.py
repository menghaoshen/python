# 拿出最多的那个值
chars = ['a', 'c', 'x', 'd', 'p', 'a', 'm', 'q', 's', 't', 'p', 'a', 't', 'c','c']
# {}
# 先统计，每个数出现的次数
char_count = {}
for char in chars:
    if char in char_count:
        char_count[char] += 1
    else:
        char_count[char] = 1
print(char_count)

vs = char_count.values()
#取最大数可以使用max，取最大数
print(max(vs))

for k,v in char_count.items():
    if v == max(vs):
        print(k)