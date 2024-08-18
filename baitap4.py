# -*- coding: utf-8 -*-
"""
Created on Sun Aug 18 09:59:19 2024

@author: TruongThiThanhUyen
"""

a= float(input('quãng đường đi được(km):'))
if a<=1:
    x=20
    u=x*a
    print('số tiền(k)',x)
if a<=3:
    y=13
    u=a*y
    print('số tiền(k):',u) 
elif a>=4 and a<=8:
    z=12
    u=u+((a-3)*z)
    print('số tiền(k):',u)
else:
    t=10
    u=a*t
    print('số tiền(k):',u)
if u>100:
    print('số tiền(k):',u-(u*0.08))