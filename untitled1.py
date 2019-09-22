# -*- coding: utf-8 -*-
"""
Created on Sun Sep 15 22:54:11 2019

@author: Ansari
"""

import cv2
import numpy as pp
 
# Create a VideoCapture object and read from input file
# If the input is the camera, pass 0 instead of the video file name
cap = cv2.VideoCapture('http://192.168.1.109:8080/videofeed')
 
# Check if camera opened successfully
if (cap.isOpened()== False): 
  print("Error opening video stream or file")
 
# Read until video is completed
while(cap.isOpened()):
  # Capture frame-by-frame
  ret, frame = cap.read()
  if ret == True:
 
    # Display the resulting frame
    cv2.rectangle(frame, (80, 85), (305, 400), (255,0,0), 2)
    cv2.imshow('Frame',frame)
    imS=cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    l = pp.array([0, 50, 80], dtype = "uint8")
    u = pp.array([23, 255, 255], dtype = "uint8")
    skinDetect = cv2.inRange(imS, l, u)
    cv2.imshow('ski',skinDetect)
    img_blur = cv2.bilateralFilter(frame, d = 7,sigmaSpace = 75, sigmaColor =75)
    # Convert to grayscale 
    img_gray = cv2.cvtColor(img_blur, cv2.COLOR_RGB2GRAY)
    # Apply the thresholding
    a = img_gray.max()  
    _, thresh = cv2.threshold(img_gray, a/2+60, a,cv2.THRESH_BINARY_INV)
    image, contours = cv2.findContours(image = thresh, mode = cv2.RETR_TREE, method = cv2.CHAIN_APPROX_SIMPLE)
    
    #cv2.imshow('fame2',thresh)
 
    # Press Q on keyboard to  exit
    if cv2.waitKey(1) & 0xFF == ord('q'):
      break
 
  # Break the loop
  else: 
    break
 
# When everything done, release the video capture object
cap.release()
 
# Closes all the frames
cv2.destroyAllWindows()