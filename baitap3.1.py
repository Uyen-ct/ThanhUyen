# -*- coding: utf-8 -*-
"""
Created on Sun Aug 18 09:00:00 2024

@author: TruongThiThanhUyen
"""
a=float(input('cạnh a='))
b=float(input('cạnh b='))
c=float(input('cạnh c='))
if a+b>c and a+c>b and b+c>a :
    print('a, b, c là 3 cạnh của tam giác')
else:
    print('a, b, c không là 3 cạnh của tam giác')