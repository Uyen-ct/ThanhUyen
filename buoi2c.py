# -*- coding: utf-8 -*-
"""
Created on Sun Aug 18 07:27:02 2024

@author: TruongThiThanhUyen
"""
distance=float(input("Nhập độ dài đoạn đường đến trường (m )"))
if distance<300:
    print("Đường đến trường gần. Thôi! Đi bộ")
elif distance>1200:
    print("Đường đến trường gần. Thôi! Đi xe máy")
elif distance>=300 and distance<=700:
    print("Đường đến trường gần. Thôi! Đi xe đạp")
else:
    print("Không xác định được")