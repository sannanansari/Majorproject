# -*- coding: utf-8 -*-
"""
Created on Sun Oct  6 21:54:57 2019

@author: Ansari
"""

import cv2
import pyautogui
import numpy as np
import random 

cap = cv2.VideoCapture('http://192.168.1.103:8080/videofeed')
if (cap.isOpened()== False): 
  print("Error opening video stream or file")
 
k = 0
while(cap.isOpened()):
  ret, frame = cap.read()
  if ret == True:
      cv2.imshow('original-image',frame)
      grayframe = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
      #cv2.imshow('Gray-image',grayframe)
      hsvframe = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
      cv2.imshow('HSV-image',hsvframe)
      lower_color = np.array([108, 23, 82])
      upper_color = np.array([179, 255, 255])      
      rangeframe = cv2.inRange(frame,lower_color,upper_color)
      blur = cv2.medianBlur(rangeframe, 5)
      kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (8, 8))
      hsv_d = cv2.dilate(blur, kernel)
      cv2.imshow('range-image',blur)
      cv2.imshow('range-image2',hsv_d)
      x = np.argwhere(hsv_d == 255)
      print(x)
      if k > 5:
          if k > x[0][0]:
              a = random.randrange(120, 250)
              b = random.randrange(300, 450)
              pyautogui.moveTo(a,b)
      k+=1
  if cv2.waitKey(1) & 0xFF == ord('q'):
      break

cap.release()
cv2.destroyAllWindows()