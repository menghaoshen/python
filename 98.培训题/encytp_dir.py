# 读取一个 dicom 影像，将其病人姓名，医院名脱敏处理。
import pydicom as pd
import hashlib
import os
import  shutil


# MD5函数 使用md5加密
def get_md5(info):
    md5 = hashlib.md5()
    md5.update(info.encode('utf8'))
    return md5.hexdigest()

#需要脱敏的字段
metas = [
    "PatientName",
    "InstitutionName",
]


path = 'F:/培训数据/2.1数据/'
for file in os.listdir(path):
    os.chdir('F:/test11')
    dcmdate = pd.dcmread(path + file)
    if 'InstitutionName' in dcmdate and 'PatientName' in dcmdate :
        dcmdate.InstitutionName = get_md5(dcmdate.InstitutionName)
        dcmdate.PatientName = get_md5(dcmdate.PatientName)
        dcmdate.save_as(file)
    elif 'PatientName' in dcmdate and 'InstitutionName' not in dcmdate :
        # 把名字加密和医院名字脱敏
        dcmdate.PatientName = get_md5(dcmdate.PatientName)
        # 更改数据集后，将所做的修改写回到文件
        dcmdate.save_as(file)
    elif 'InstitutionName' in dcmdate and 'PatientsName' not in dcmdate:
        dcmdate.InstitutionName = get_md5(dcmdate.InstitutionName)
        dcmdate.save_as(file)
    else:
        dcmdate.save_as(file)





