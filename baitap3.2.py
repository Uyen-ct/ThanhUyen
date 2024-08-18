# -*- coding: utf-8 -*-
"""
Created on Sun Aug 18 09:51:07 2024

@author: TruongThiThanhUyen
"""

a=float(input('cạnh a='))
b=float(input('cạnh b='))
c=float(input('cạnh c='))
if a+b>c and a+c>b and b+c>a :
    print('là tam giác')
    if  a**2==b**2 + c**2 or b**2==a**2 + c**2 or c**2== a**2 + b**2:
         print('loại tam giác vuông')
    elif a==b and b==c:
        print('loại tam giác đều')
    elif a==b or b==c or c==a:
        print('loại tam giác cân')
    elif a**2>b**2 + c**2 or b**2>a**2 + c**2 or c**2>a**2+b**2:
        print('loại tam giác tù')
    else:
        print('loại 3tam giác nhọn')       
else:
    print('không là tam giác')