from pydicom import dcmread
filepath = "F:/培训数据/2.1数据/192.168.10.86~21~image24~2019~7~9~CT~2467392~8791442~376762398.dcm"
ds = dcmread(filepath)
metas = [
    "PatientID",
    "PatientName",
    "PatientBirthDate",
    "PatientSex",
    "StudyDescription",
    "BodyPartExamined",
    "InstitutionName",
]
for meta in metas:
    print(ds.data_element(meta))
