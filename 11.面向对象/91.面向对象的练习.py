# 需求如下：
#
# 1. 房子(House) 有 户型、总面积 、剩余面积 和 家具名称列表 属性
#    - 新房子没有任何的家具
#    - 将 家具的名称 追加到 家具名称列表 中
#    - 判断 家具的面积 是否 超过剩余面积，如果超过，提示不能添加这件家具
# 2. 家具(HouseItem) 有 名字 和 占地面积属性，其中
#    - 席梦思(bed) 占地 4 平米
#    - 衣柜(chest) 占地 2 平米
#    - 餐桌(table) 占地 1.5 平米
# 3. 将以上三件 家具 添加 到 房子 中
# 4. 打印房子时，要求输出：户型、总面积、剩余面积、家具名称列表
#    使用面向对象思想，编码完成上述功能。

## 房子的类型
class House(object):
    #缺省参数 ,家具是空列表,就是空值
    def __init__(self,hour_type,total_area,fru_list=None):
        if fru_list is None:
            fru_list = [] #将fru_list 设置为空列表
        self.hour_type = hour_type
        self.totaol_area = total_area
        self.free_area = total_area * 0.6
        self.fru_list = fru_list

    def add_fru(self,x):
        # print('需要把家具添加到房子里面')
        if self.free_area < x.area:
            print('剩余面积不足，放不进去了')
        else:
            self.fru_list.append(x.name)
            self.free_area -= x.area
    def __str__(self):
        return  '户型={}，总面积={}，剩余面积={}，家具列表={}'.format(self.hour_type,self.totaol_area,self.free_area,self.fru_list)

# 家具的类
class Furniture(object):
    def __init__(self,name,area):
        self.name = name
        
        self.area = area

bed = Furniture('席木思',20)
chest = Furniture('衣柜',10)
talbe = Furniture('餐桌',1.5)
sofa = Furniture('沙发',2

                 )

#创建房间对象的时候，传入户型和总面积
house1 = House('两室一厅',56)
#把家具添加到房间里面（面向对象的关注点，是让谁做）
house1.add_fru(sofa)
house1.add_fru(bed)
house1.add_fru(chest)
house1.add_fru(talbe)
print(house1)  #默认打印内存地址 ,需要重新str方法，才能获取返回值


