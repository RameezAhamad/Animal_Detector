# -*- coding: utf-8 -*-
"""
Created on Fri Sep 27 11:59:02 2019

@author: Shaik Rameez
"""

import serial
import time
import json
import cv2
import smtplib
from ibm_watson import VisualRecognitionV3
port='COM4'
ard = serial.Serial(port,9600,timeout=5)

time.sleep(2)
x="found"
y="notfound"
visual_recognition = VisualRecognitionV3(
    '2018-03-19',
    iam_apikey='AOxWTRCsrNJYB9TIAawriHIv1L-UxHut2OlnCJ-eS54E')
cap=cv2.VideoCapture(0)
while 1:
    ret, img=cap.read()
    if (ret):
        cv2.imwrite('elephantrename.jpg',img)
        break
cap.release()
with open('elephantrename.jpg','rb') as images_file:
    classes = visual_recognition.classify(
        images_file,
        threshold='0.6',
        owners=["me"]).get_result()
    a=json.dumps(classes, indent=2)
    print (a)
    a=a.split('\n')
    count=0
    b=''
    c=''    
    try:
     for i in a:
      count+=1
      if(count==10):
       b=i.split(": ")
       b=b[1]
       b=b[1:-2]
       #print (b)
      if (count==11):
       #print (i)
       c=i.split(": ")
       c=float(c[1])
       #print (c)
       if (b=="madmen2" and c>=0.85):
           print("animal is detected")
           ard.write(x.encode('utf-8'))
           print(c)
           s = smtplib.SMTP('smtp.gmail.com', 587)
           s.starttls() 
           s.login("shaikrameezsra@gmail.com", "Rameez@5g9srh") 
           message = "omg!!! Tiger just entered here save us plz"
           s.sendmail("shaikrameezsra@gmail.com", "shaikrameezprince80158@gmail.com", message) 
           s.quit() 
       elif(b=="madman3" and c>=0.85):
           print("animal is detected")
           ard.write(x.encode('utf-8'))
           print(c)
           s = smtplib.SMTP('smtp.gmail.com', 587)
           s.starttls() 
           s.login("shaikrameezsra@gmail.com", "Rameez@5g9srh") 
           message = "omg!!! elephants entered into village and feilds help us "
           s.sendmail("shaikrameezsra@gmail.com", "shaikrameezprince80158@gmail.com", message) 
           s.quit() 
       else:
           print("not found")
           ard.write(y.encode('utf-8'))
    except:
     print("normal")
cv2.waitKey(0)
cv2.destroyAllWindows()
cap.release()









