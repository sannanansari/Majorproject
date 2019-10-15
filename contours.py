# -*- coding: utf-8 -*-
"""
Created on Mon Oct 14 18:15:33 2019

@author: Sk Mobin
"""

# -*- coding: utf-8 -*-
"""
Created on Mon Oct 14 17:35:47 2019

@author: Sk Mobin
"""


import cv2
import pyautogui
import numpy as np
import random 

cap = cv2.VideoCapture('http://192.168.1.103:8080/videofeed')
if (cap.isOpened()== False): 
  print("Error opening video stream or file")
 
x,y = 0,0
while(cap.isOpened()):
  ret, frame = cap.read()
  if ret == True:
      #cv2.imshow('original-image',frame)
      #grayframe = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
      #cv2.imshow('Gray-image',grayframe)
      gray = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
      #cv2.imshow('HSV-image',hsvframe)
      #lower_color = np.array([160, 0, 240])
      #upper_color = np.array([160, 0, 240])      
      #rangeframe = cv2.inRange(frame,lower_color,upper_color)
      #blur = cv2.medianBlur(rangeframe, 5)
      #kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (8, 8))
      #hsv_d = cv2.dilate(blur, kernel)
      edge = cv2.Canny(gray,30,200)
      cnts,_ = cv2.findContours(edge, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
      cv2.drawContours(frame,cnts,-1,(160,0,140),3)
      #cv2.imshow('range-image',blur)
      #cv2.imshow('range-image2',hsv_d)
      cv2.imshow('ran',frame)
      print(cnts)
     # cnts = imutils.grab_contours(cnts)
      #x = np.argwhere(hsv_d == 255)
      #print(x)
      '''
      #movement
      a = cnt[0][0]
      b = cnt[0][1]
      if  a > x:
          pyautogui.moveTo(500,200)
      elif b > y:
          pyautogui.moveTo(200,720)
      elif a < x:
          pyautogui.moveTo(100,200)
      elif b < y:
          pyautogui.moveTo(200,200)
      else:
          pyautogui.moveTo(500,500)
      a = x
      b = y
          '''
  if cv2.waitKey(1) & 0xFF == ord('q'):
      break

cap.release()
cv2.destroyAllWindows()
