

""" import cv2
import numpy as np
from pyzbar.pyzbar import decode
from numpy import *
import time

cap = cv2.VideoCapture(0)
cap.set(3,1920)
cap.set(4,1080)
                   
while (cap.isOpened()): 
    success,img=cap.read() 
    myouput = 'NO Autorizado'
    color=(0,0,255)
    bar_detected = ""
    for barcode in decode(img):
        mydata= barcode.data.decode('utf-8')   
        print(mydata) 
        new_lines = []
        if bar_detected == mydata:
                myouput = 'Autorizado'
                color=(0,255,0)             
        with open(r'data/credentials.txt', 'r') as f:
            for line in f.readlines():
                if mydata in line:
                    myouput = 'Autorizado'
                    color=(0,255,0)     
                    bar_detected = mydata           
                else:  
                    new_lines.append(line)
        with open(r'data/credentials.txt', 'w') as f:
            f.write("".join(new_lines))    


        pts = np.array([barcode.polygon],np.int32)
        pts = pts.reshape((-1,1,2))

        #se crea el cuadro de color segun el estado
        cv2.polylines(img, [pts], True, color, thickness=2  )
        
        pts2 = barcode.rect
        cv2.putText(img,myouput,(pts2[0],pts2[1]),cv2.FONT_HERSHEY_COMPLEX,0.9,color,3)

    cv2.imshow('Result',img)
    
    if cv2.waitKey(30) == ord('q'):
       break


cv2.destroyAllWindows() """

""" import cv2
import numpy as np
from pyzbar.pyzbar import decode
from numpy import *
import time

cap = cv2.VideoCapture(0)
cap.set(3,1920)
cap.set(4,1080)
                   
while (cap.isOpened()): 
    success,img=cap.read() 
    myouput = 'NO Autorizado'
    color=(0,0,255)
    for barcode in decode(img):
        mydata= barcode.data.decode('utf-8')    
        new_lines = []

        
        with open(r'data/credentials.txt', 'r') as f:
            for line in f.readlines():
                if mydata in line:
                    myouput = 'Autorizado'
                    color=(0,255,0)                
                else:  
                    new_lines.append(line)
        with open(r'data/credentials.txt', 'w') as f:
            f.write("".join(new_lines))    


        pts = np.array([barcode.polygon],np.int32)
        pts = pts.reshape((-1,1,2))

        #se crea el cuadro de color segun el estado
        cv2.polylines(img, [pts], True, color, thickness=2  )
        
        pts2 = barcode.rect
        cv2.putText(img,myouput,(pts2[0],pts2[1]),cv2.FONT_HERSHEY_COMPLEX,0.9,color,3)

    cv2.imshow('Result',img)
    
    if cv2.waitKey(30) == ord('q'):
       break """










""" 

import cv2
import numpy as np
from pyzbar.pyzbar import decode
from numpy import *
import time

cap = cv2.VideoCapture(0)
cap.set(3,1920)
cap.set(4,1080)
                   
with open(r'data/credentials.txt', 'r') as f:
    mydatalist=f.read()
   

print(mydatalist)

while (cap.isOpened()): 
    success,img=cap.read() 
    for barcode in decode(img):
        mydata= barcode.data.decode('utf-8')
        #print(mydata)

        new_lines = []
        myouput = 'NO Autorizado'
        color=(0,0,255)
        with open(r'data/credentials.txt', 'r') as f:
            for line in f.readlines():
                if mydata in line:
                    
                    myouput = 'Autorizado'
                    color=(0,255,0) 
                    cv2.waitKey(200)        
                else:  
                    new_lines.append(line)
        with open(r'data/credentials.txt', 'w') as f:
            f.write("".join(new_lines))     


        pts = np.array([barcode.polygon],np.int32)
        pts = pts.reshape((-1,1,2))

        #se crea el cuadro de color segun el estado
        cv2.polylines(img, [pts], True, color, thickness=2  )
        
        pts2 = barcode.rect
        cv2.putText(img,myouput,(pts2[0],pts2[1]),cv2.FONT_HERSHEY_COMPLEX,0.9,color,3)

    cv2.imshow('Result',img)
    
    if cv2.waitKey(30) == ord('q'):
       break

    #if cv2.waitKey(30) & 0xFF == 27:
     #       break 
       


"""

""" 
import cv2
import numpy as np
from pyzbar.pyzbar import decode
from numpy import *
import time

cap = cv2.VideoCapture(0)
cap.set(3,1920)
cap.set(4,1080)
                   
with open(r'data/credentials.txt', 'r') as f:
    mydatalist=f.read()
   

print(mydatalist)

while (cap.isOpened()): 
    success,img=cap.read() 
    for barcode in decode(img):
        mydata= barcode.data.decode('utf-8')
        #print(mydata)

        new_document = []
        with open(r'data/credentials.txt', 'r') as f:
            for line in f.readlines():
                if mydata in line:
                    myouput = 'Autorizado'
                    color=(0,255,0)                
                else:  
                    myouput = 'NO Autorizado'
                    color=(0,0,255)
                    new_document.append(line)
        with open(r'data/credentials.txt', 'w') as f:
            f.write("".join(new_document)) 
            myouput = 'ya paso'   


        pts = np.array([barcode.polygon],np.int32)
        pts = pts.reshape((-1,1,2))

        #se crea el cuadro de color segun el estado
        cv2.polylines(img, [pts], True, color, thickness=2  )
        
        pts2 = barcode.rect
        cv2.putText(img,myouput,(pts2[0],pts2[1]),cv2.FONT_HERSHEY_COMPLEX,0.9,color,3)

    cv2.imshow('Result',img)
    
    if cv2.waitKey(30) == ord('q'):
       break

    #if cv2.waitKey(30) & 0xFF == 27:
     #       break 
       
 """