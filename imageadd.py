# -*- coding: utf-8 -*-
"""
Created on Sun Oct  6 16:25:04 2019

@author: Ansari
"""

import cv2


img1 = cv2.imread('ex3.jpg')
img2 = cv2.imread('ex2.jpg')
add = img1+img2
#cv2.imshow('add',add)
add1 = cv2.add(img1,img2)
#cv2.imshow('add-method',add1)
weighted = cv2.addWeighted(img1,1,img2,1,0)
#cv2.imshow('weighted',weighted)
cv2.imshow('image1',img1)
ret, th = cv2.threshold(img1,150,100,cv2.THRESH_BINARY_INV)
#cv2.imshow('theshold',th)
icon = cv2.imread('icon.ico')
cv2.imshow('icon',icon)
cv2.waitKey(0)
cv2.destroyAllWindows()