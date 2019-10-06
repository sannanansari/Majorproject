# -*- coding: utf-8 -*-
"""
Created on Sat Oct  5 21:59:40 2019

@author: Ansari
"""

import numpy as np
import cv2
im = cv2.imread('hand.jpg')
#ret,thresh = cv2.threshold(im,127,255,0)
#cv2.imshow('threshold-image',thresh)
HSV = cv2.cvtColor(im,cv2.COLOR_BGR2HSV)
cv2.imshow('gray-image', im)
cv2.imshow('hsv-image',HSV)
subtract = cv2.subtract(im,HSV)
subtract = cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
th3 = cv2.adaptiveThreshold(subtract,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,11,2)
blur = cv2.GaussianBlur(th3,(5,5),0)
cv2.imshow('subract-image',th3)

imagem = cv2.bitwise_not(blur)
cv2.imshow('invert-image',imagem)
cv2.waitKey(0)
cv2.destroyAllWindows()



'''
kernel = np.ones((3,3),np.uint8)
    hsv = cv2.cvtColor(im, cv2.COLOR_BGR2HSV)
    lower_skin = np.array([0,20,70], dtype=np.uint8)
    upper_skin = np.array([20,255,255], dtype=np.uint8)
    mask = cv2.inRange(hsv, lower_skin, upper_skin)
    mask = cv2.dilate(mask,kernel,iterations = 4)
    mask = cv2.GaussianBlur(mask,(5,5),100) 
    cv2.imshow('mask',mask)
    contours,hierarchy= cv2.findContours(mask,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    cnt = max(contours, key = lambda x: cv2.contourArea(x))
    epsilon = 0.0005*cv2.arcLength(cnt,True)
    approx= cv2.approxPolyDP(cnt,epsilon,True)

    hull = cv2.convexHull(cnt)
    areahull = cv2.contourArea(hull)
    areacnt = cv2.contourArea(cnt)
      
    #find the percentage of area not covered by hand in convex hull
    arearatio=((areahull-areacnt)/areacnt)*100
    
     #find the defects in convex hull with respect to hand
    hull = cv2.convexHull(approx, returnPoints=False)
    defects = cv2.convexityDefects(approx, hull)
    #cv2.imshow('hull',hull)
 '''