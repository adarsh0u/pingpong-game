import cv2
from cv2 import putText
import mediapipe as mp
import time
print(cv2.__version__)

width= 640
height= 360
barwidth= 100
barheigth= 20
barcolor= (0,255,0)

myhands= mp.solutions.hands.Hands(False,1,0.5,0.5)
mydraw= mp.solutions.drawing_utils

def datahands(frame):
    Handsdata=[]
    framergb= cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
    data= myhands.process(framergb)

    if data.multi_hand_landmarks != None:
        for eachhand_landmarks in data.multi_hand_landmarks:
           mylandmarks=[]
           for each_landmark in eachhand_landmarks.landmark:
             mylandmarks.append((int(each_landmark.x*width),int(each_landmark.y*height)))

           Handsdata.append(mylandmarks)
    return Handsdata

def mainfunc():
    xpos= int(width/2)
    ypos= int(height/2)
    delx=4
    dely=4
    radius=10
    color=(0,0,255)
    indx=8
    lives=5
    score=0
    topx=int(barwidth/2)
    font= cv2.FONT_HERSHEY_COMPLEX
    global cam
    cam=cv2.VideoCapture(0,cv2.CAP_DSHOW)
    cam.set(cv2.CAP_PROP_FRAME_WIDTH,width)  #select the width of the showing window.
    cam.set(cv2.CAP_PROP_FRAME_HEIGHT, height) #select the height of the showing window.
    cam.set(cv2.CAP_PROP_FPS, 30)  #sets the frame per second(FPS) of the window screen.
    cam.set(cv2.CAP_PROP_FOURCC,cv2.VideoWriter_fourcc(*'MJPG')) # MJPG is moving jpg    
    while True:
        if lives==0:
            lives=5
            score=0
            time.sleep(3)

        ignore, frame= cam.read()
        myHands= datahands(frame)
        for eachhand in myHands:
            topx=eachhand[indx][0]
            cv2.rectangle(frame,(int(topx-barwidth/2),0),(int(topx+barwidth/2),barheigth),barcolor,-1)
        cv2.putText(frame,str(score),(20,height-20),font,2,(0,0,0),2)
        cv2.putText(frame,str(lives),(width-70,height-20),font,2,(0,0,0),2)
        cv2.circle(frame,(xpos,ypos),radius,color,-1)
        leftedge= int(xpos-radius/2)
        rigthedge= int(xpos+radius/2)
        topedge= int(ypos-radius/2)
        bottomedge= int(ypos+radius/2)
        if leftedge<=0 or rigthedge>=width:
            delx=delx*(-1)

        if bottomedge>=height:
            dely= dely*(-1)

        if topedge<=barheigth:
            if xpos>= int(topx-barwidth/2) and xpos<= int(topx+barwidth/2):
                dely=dely*(-1)
                score=score+1

                if score%5 == 0:
                    delx=delx+4
                    dely=dely+4

            else:
                xpos= int(width/2)
                ypos= int(height/2)
                lives=lives-1
                
        xpos=xpos+delx
        ypos=ypos+dely
        if lives==0:
            delx=4
            dely=4
            putText(frame,'Score:'+str(score),(int(width/2-100),int(height/2)),font,2,(0,0,255),2)
            
        cv2.imshow('my window',frame)
        cv2.moveWindow('my window',0,0) 
        
        if cv2.waitKey(1) & 0xff== ord('q'):
            break    
    cam.release() 
    cv2.destroyAllWindows

def closeapp():
    cam.release()
    cv2.destroyAllWindows

     