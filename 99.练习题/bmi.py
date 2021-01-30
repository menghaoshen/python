height = 1.75
weight = 80.5
bmi = weight/(height ** 2)
if bmi < 18.5:
    print('过轻:%.1f'%bmi)
elif bmi >=18.5 and bmi < 25:
    print('正常: %.1f'%bmi)
elif bmi>=25 and bmi < 28:
    print('过重：%.1f'%bmi)
elif bmi>=28 and bmi < 32:
    print('肥胖：%.1f'%bmi)    
else:
    print('严重肥胖:%.f'%bmi)