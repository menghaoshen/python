# 1. 数字和字母都表示它本身
# 2. 很多字母前面添加\会有特殊含义
# 3. 绝大数标点符号都有特殊含义


# 字母x表示它本身
import re

re.search(r'x','hello xyz')
re.search(r'5','23fds5fda8')

print(re.search(r'd','good')) # 字母d是普通的字符
print(re.search(r'\d','good')) #\d 有特殊的含义，不在表示字母d
print(re.search(r'\d','fada7897fda')) #

# print(re.search(r'+', '1+2'))  #不能直接使用,有特殊含义
print(re.search(r'\+', '1+2')) 

#看到224集