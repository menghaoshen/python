# 读取一个 dicom 影像，将其病人姓名，医院名脱敏处理。
import pydicom as pd
import hashlib
import os
import shutil

# 需要脱敏的字段
metas = [
    "PatientName",
    "InstitutionName",
]


# MD5函数 使用md5加密
def get_md5(info):
    md5 = hashlib.md5()
    md5.update(info.encode('utf8'))
    return md5.hexdigest()


def encrypt(src, dest):
    os.chdir(dest)  # 加密后的存放路径
    filepath = src
    for file in os.listdir(filepath):
        ds = pd.dcmread(filepath + file)
        for meta in metas:
            value = ds.get(meta)
            if value is not None: #有可能会遇到空值的情况，遇到空值，程序会崩溃
                md5 = get_md5(value)
                dict1 = {meta: md5}
            ds.update(dict1)
        ds.save_as(file)


if __name__ == '__main__':
    encrypt('F:/培训数据/2.1数据/', 'F:/test11/')


