# -*- coding: utf-8 -*-
"""
Created on Sun Aug 18 08:04:56 2024

@author: TruongThiThanhUyen
"""
import math
a=float(input('nhập a='))
b=float(input('nhập b='))
c=float(input('nhập c='))
if a!=0:
    delta=b**2-4*a*c
    if delta<0:
        print('pt vô nghiệm')
    elif delta==0:
        x= -b/(2*a)
        print('pt có nghiệm kép x1=x2= ',x)
    else:
        x1=(-b-math.sqrt(delta)/(2*a))
        x2=(-b+math.sqrt(delta)/(2*a))
        print('pt có 2 nghiệm phân biệt')
        print('x1=',x1)
        print('x2=',x2)
else:
    print('không phải pt bậc 2')