# 4 通过 python 读写 excel
# 作业：
# 1、读取 csv 中的第 12 列，并统计检查部位有多少种。
# 2、将统计的检查部位存入到一个新 scv 中，保存格式如：
# 第一列部位 第二列数量
# [胸部,平扫] 301
# [胸部,平扫+增强] 109
import csv

position = []
position1 = []

with open('F:/培训数据/1.4数据/data805.csv', 'r', encoding='utf8', newline='') as csvfile:
    reader = csv.reader(csvfile)
    for i in reader:
        position.append(i[11])
    for i in position:
        if i not in position1:
            position1.append(i)
    print('检查部位一共有{}种'.format(len(position)))
    title = ['部位','数量']
    demon = open('./demon.csv', 'w', newline='', encoding='utf8')
    w = csv.writer(demon)
    w.writerow(title)
    for i in position1:
        nums = position.count(i)
        x = [i,nums]
        w.writerow(x)
