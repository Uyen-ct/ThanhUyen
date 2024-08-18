# -*- coding: utf-8 -*-
"""
Created on Sun Aug 18 07:46:44 2024

@author: TruongThiThanhUyen
"""
def giai_phuong_trinh_bac_1(a,b):
    if a==0:
        if b==0:
            print('phương trình vô số nghiệm.')
        else:
            print('phương trình vô nghiệm')
    else:
        x=-b/a
        print('nghiệm phương trình là:',x)
    
a=float(input('nhập a:'))
b=float(input('nhập b:'))
giai_phuong_trinh_bac_1(a,b)
        
        