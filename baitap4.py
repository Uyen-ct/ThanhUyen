# -*- coding: utf-8 -*-
"""
Created on Sun Aug 18 09:59:19 2024

@author: TruongThiThanhUyen
"""

a= float(input('quãng đường đi được(km):'))
if a<=1:
    x=20
    print('số tiền(k)',x)
if a<=3:
    y=13
    x=a*13
    print('số tiền(k):',x)
elif a>=4 and a<=8:
    z=12
    x=12*(a-3)+(3*13)
    print('số tiền(k):',x)
else:
    t=10
    x=10*(a-8)+(8*12)
    print('số tiền(k):',x)
if x>100:
    print('số tiền(k):',x-(x*0.08))