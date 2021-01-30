import  re

# 在python的正则表达式里面，默认是贪婪模式，就是尽可能多的匹配
#在贪婪模式后面添加? 可以将贪婪模式转换为非贪婪模式
m = re.search(r'm.*a','o3mfdsaaddas')
print(m)
#尽可能少的匹配
m = re.search(r'm.*?a','o3mfdsaaddas')
print(m)

print(re.match(r'aa(\d+)', 'aa2343dd').group()) #aa2343
print(re.match(r'aa(\d+?)', 'aa2343dd').group()) #aa2
print(re.match(r'aa(\d+?)dd', 'aa2343dd').group(0)) #aa2343dd
print(re.match(r'aa(\d+?).*', 'aa2343dd').group(1)) #2
print(re.match(r'aa(\d??)(.*)', 'aa2343dd').group(1)) #空
src = 'https://img2020.cnblogs.com/blog/35695/202012/35695-20201218110459403-299239562.png  https://img2020.cnblogs.com/blog/35695/202012/35695-20201218110459403-299239562.png'
x6 = re.search(r'https://.*?\.png',src)
print(x6.group())