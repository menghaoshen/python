#  了解 dicom 文件信息，包括但不限于 patient,study,series 各种字段的关系
# 作业：
# 1、读取一个 dicom 影像，打印出 tag 信息，整理出每个 tag 的中文意义
# 2、读取一个 dicom 影像，并将其图像打印出来
# 3、读取整套 dicom 影像，打印出有多少个 series，每个 series 的层厚是多少
# 了解脱敏的基本原理和使用
# 作业：读取一个 dicom 影像，将其病人姓名，医院名脱敏处理。
# 2.3 写一个简单的脱敏脚本
# 作业：通过脚本将 2.1 数据中所有的病人姓名，医院名脱敏。
import pydicom as pd
from matplotlib import pyplot as plt
file = 'F:/培训数据/2.1数据/192.168.10.86~21~image24~2019~7~9~CT~2467392~8791442~376762398.dcm'
dcmdate = pd.dcmread(file)


ds = pd.dcmread(file)
for key in dcmdate.dir():
    if key == 'PixelData':
        continue


    value = getattr(dcmdate,key,'')
    print("%s:%s" %(key,value))

# 打印图像
# 读取一个 dicom 影像，并将其图像打印出来
plt.imshow(dcmdate.pixel_array)
plt.show()



