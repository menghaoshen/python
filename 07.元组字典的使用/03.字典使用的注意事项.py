person = {'name': 'zhangsan',
          'age': 18,
          'math': 98,
          'Chines': 97,
          'English': 96,
          'gym': 93,
          'height': 180,
          'age':90, #重复了会覆盖前一个
          'IsPass':True, #可以是布尔值
          'hobbies':['唱','跳','rap'], #可以是列表
          4:'good', #key 只能是不可变的数据类型，
          ('yes','hello'):100, #
          }
print(person)
#字典里面的key不允许重复，如果key重复了，后一个key对于的值会覆盖前一个
#字典里面的value 可以是任意数据类型，但是key只能使用不可变数据类型，一般是字符串

