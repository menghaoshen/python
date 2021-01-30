# 3、读取整套 dicom 影像，打印出有多少个 series，每个 series 的层厚是多少

import  os
import pydicom as pd
from matplotlib import pyplot as plt
path = 'F:/培训数据/2.1数据/'

total = 0
char_count = {}
for i in os.listdir(path):
    ds = pd.dcmread(path + i)
    uid = ds.SeriesInstanceUID
    for key in ds.dir():
        if key == 'SliceThickness':
            value = getattr(ds,key,'')
    if uid  in char_count:
        char_count[uid]= value
        # char_count[uid] += 1
    else:
        # char_count.update({uid: key})
        char_count[uid] = value
print('整套dicom影像有{}个series'.format(len(char_count)))
for k,v in char_count.items():
    print('{} 个 series 的层厚是{}'.format(k,v))




