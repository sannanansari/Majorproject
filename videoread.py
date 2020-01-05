"""
Created on Sat Sep  7 11:42:20 2019

@author: Ansari
"""
import cv2
import numpy as pp
vidcap = cv2.VideoCapture('http://192.168.1.104:8080/videofeed')
success,image = vidcap.read()
print(success)
count = 0
while success:
  cv2.imwrite("frame%d.jpg" % count, image)     # save frame as JPEG file      
  success,image = vidcap.read()
  print('Read a new frame: ', success)
  count += 1
  cv2.imshow('frame',image)
  if count%10==0:
      #cv2.imshow('frame123',image)
      imS = cv2.resize(image, (800, 700))
      roi=imS[50:200, 600:600]
      r = cv2.rectangle(imS,(50,200),(700,700),(0,255,0),0) 
      imS=cv2.cvtColor(imS, cv2.COLOR_BGR2HSV)
      #cv2.imshow('frame',imS)
      l = pp.array([0, 50, 80], dtype = "uint8")
      u = pp.array([23, 255, 255], dtype = "uint8")
      skinDetect = cv2.inRange(imS, l, u)
      #print(l,u,skinDetect[0])
      skinDetect = cv2.GaussianBlur(skinDetect,(5,5),100)
      #cv2.imshow('Masked Image',skinDetect)
      #cv2.imshow('frame',imS)
      frame =  cv2.bitwise_and(imS,imS, mask= skinDetect)
      cv2.imshow('frame',frame)
      #break
      if cv2.waitKey(1) & 0xFF == ord('q'):
          break
cv2.destroyAllWindows()
