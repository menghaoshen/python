# 读取一个 dicom 影像，将其病人姓名，医院名脱敏处理。
import pydicom as pd
import hashlib


# MD5函数
def get_md5(info):
    md5 = hashlib.md5()
    md5.update(info.encode('utf8'))
    return md5.hexdigest()


file = 'F:/培训数据/2.1数据/192.168.10.86~21~image24~2019~7~9~CT~2467392~8791442~376762398.dcm'
dcmdate = pd.dcmread(file)
print(dcmdate.InstitutionName)
print(dcmdate.PatientName)

# 把名字加密和医院名字脱敏
dcmdate.PatientName = get_md5(dcmdate.PatientName)
dcmdate.InstitutionName = get_md5(dcmdate.InstitutionName)
# 更改数据集后，最后一步是将所做的修改写回到文件
dcmdate.save_as('F:/out2.dcm')
