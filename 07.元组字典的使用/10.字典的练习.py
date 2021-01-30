# dict1 = {"a":100,"b":200,"c":300}
# {100:"a",200:"b",300:"c"} 代码改成这样  #kv 换个位置

dict1 = {"a":100,"b":200,"c":300}
dict2 ={}

#第一种写法
# for k,v in dict1.items():
#     dict2[v] = k
# dict1 = dict2
#
# print(dict2)

dict1 = {v:k for k ,v in dict1.items()}
print(dict1)