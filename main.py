

import cv2
import pyautogui
import numpy as np
import random 

cap = cv2.VideoCapture(0)
if (cap.isOpened()== False): 
  print("Error opening video stream or file")
 
k = 0
while(cap.isOpened()):
  ret, frame = cap.read()
  if ret == True:
      imS = cv2.resize(frame, (800, 700))
      roi=imS[50:200, 600:600]
      r = cv2.rectangle(imS,(50,100),(400,400),(0,255,0),0) 
      cv2.imshow('original-image',r)
      cv2.imshow('rectagle',r)
      grayframe = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
      #cv2.imshow('Gray-image',grayframe)
      hsvframe = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
      #cv2.imshow('HSV-image',hsvframe)
      lower_color = np.array([160, 0, 240])
      upper_color = np.array([160, 0, 240])      
      rangeframe = cv2.inRange(frame,lower_color,upper_color)
      #blur = cv2.medianBlur(rangeframe, 5)
      #kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (8, 8))
      #hsv_d = cv2.dilate(blur, kernel)
      ret,thresh = cv2.threshold(grayframe,127,255,0)
      edge = cv2.Canny(thresh,35,150)
      cnts,_ = cv2.findContours(edge, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
      cv2.drawContours(frame,cnts,-1,(0,25,255),3)
      
      #cv2.imshow('range-image',blur)
      #cv2.imshow('range-image2',hsv_d)
      cv2.imshow('ran',frame)
      if len(cnts) == 0:
          continue
      elif len(cnts[0][0]) == 1:
          x = cnts[0][0][0][0]
          y = cnts[0][0][0][1]
          pyautogui.moveTo(x,y)
      # cnts = imutils.grab_contours(cnts)
      ''' x = np.argwhere(cnts == [0,25,255])
      
      print(cnts)
      x = cnts[0]
      if k > 5:
          if k > x[0][0]:
              a = random.randrange(120, 250) 
              b = random.randrange(300, 450)
              pyautogui.moveTo(a,b)
      k+=1'''
  if cv2.waitKey(1) & 0xFF == ord('q'):
      break

cap.release()
cv2.destroyAllWindows()
