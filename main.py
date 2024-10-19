import cv2
import os
from cvzone.HandTrackingModule import HandDetector
import numpy as np

width,height=1280,720
folderpath="presentation"

# capture
cap=cv2.VideoCapture(0)
cap.set(3,width)
cap.set(4,height)
pathimages=sorted(os.listdir(folderpath),key=len)
print(pathimages)

imgnumber=0
hs,ws=int(120*1),int(213*1)
gesturethreshold=500
buttonPressed=False
buttoncounter=0
buttondelay=10
annotations=[[]]
annotationnumber=0
annotationstart=False
#handdetector
detector=HandDetector(detectionCon=0.8,maxHands=1   )


while True:
    success,img=cap.read()
    img=cv2.flip(img,1)
    pathFullImage=os.path.join(folderpath,pathimages[imgnumber])
    imgcurrent=cv2.imread(pathFullImage)


    imgSmall=cv2.resize(img,(ws,hs))
    h,w,_=imgcurrent.shape
    imgcurrent[0:hs,w-ws:w]=imgSmall 
    
    hands,img=detector.findHands(img)
    cv2.line(img,(0,gesturethreshold),(width,gesturethreshold),(0,255,0),10)

    if hands and buttonPressed is False:
        hand=hands[0]
        fingers=detector.fingersUp(hand)
        cx,cy=hand['center']
        lmList=hand['lmList']
        xVal=int(np.interp(lmList[8][0],[width//2,w],[0,width]))
        yVal=int(np.interp(lmList[8][1],[150,height-150],[0,height]))
        indexFinger=xVal,yVal
        

        if cy<=gesturethreshold:
            if fingers==[1,0,0,0,0]:
                print("left")                
                if imgnumber>0:
                    buttonPressed=True
                    annotations=[[]]
                    annotationnumber=0
                    annotationstart=False
                    imgnumber-=1


            if fingers==[0,0,0,0,1]:
                print("right")               
                if imgnumber<len(pathimages)-1:
                    buttonPressed=True
                    annotations=[[]]
                    annotationnumber=0
                    annotationstart=False
                    imgnumber+=1 


        if fingers==[0,1,1,0,0]:
                cv2.circle(imgcurrent,indexFinger,12,(0,0,255),cv2.FILLED)

        if fingers==[0,1,0,0,0]:
                if annotationstart is False:
                     annotationstart=True
                     annotationnumber+=1
                     annotations.append([])
                cv2.circle(imgcurrent,indexFinger,12,(0,0,255),cv2.FILLED)
                annotations[annotationnumber].append(indexFinger)

        else: 
             annotationstart=False
        
        if fingers==[0,1,1,1,0]:
             if annotations:
                  if annotationnumber>=0:
                    annotations.pop(-1)
                    annotationnumber-=1
                    buttonPressed=True



        for i in range (len(annotations)):
            for j in range(len(annotations[i])):
                if j!=0:
                    cv2.line(imgcurrent,annotations[i][j-1],annotations[i][j],(0,0,200),12)    

        
    if buttonPressed:
        buttoncounter+=1
        if buttoncounter>buttondelay:
            buttoncounter=0
            buttonPressed=False

    cv2.imshow("Image",img)
    cv2.imshow("Slides",imgcurrent)
    
    key=cv2.waitKey(1)
    if key==ord('q'):
        break