#删除列表里面的空字符串
words = ['hello','good',' ',' ','yes','ok',' ']

#用for循环的时候，尽量不要增删，删掉以后，下标会发生变化
for word in words:
    if word == ' ':
        words.remove(word)
print(words)

#比较好的方法
i = 0
while i < len(words):
    if words[i] ==' ':
        words.remove(words[i])
        i -= 1
    i += 1
print(words)

#另一种思路
words2 = []
for word in words:

    
    if word != '':
        words2.append(word)
words2 = words
print(words)
