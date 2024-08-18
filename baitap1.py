# -*- coding: utf-8 -*-
"""
Created on Sun Aug 18 07:37:11 2024

@author: TruongThiThanhUyen
"""
distance=float(input('Nhập điểm trung bình (GPA):'))
if distance<3.5:
    print('Học lực Kém')
if distance>=3.5 and distance<5.0:
    print('Học lực Yếu')
if distance>=5.0 and distance<7.0:
    print('Học lực Trung bình')
if distance>=7.0 and distance<8.0:
    print('Học lực Khá')
if distance>=8.0 and distance<9.0:
    print('Học lực Giỏi')
if distance>=9.0 and distance<10:
    print('Học lực Xuát sắc')

