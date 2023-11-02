import HandTracking as ht
import Gesture as g
import pyautogui as pt
import cv2
import time
import numpy as np
import os

if __name__ == "__main__":
    smootheningFactor1 = os.environ.get('SF1')
    smootheningFactor2 = os.environ.get('SF2')
    cameraIndex = os.environ.get('CAMERA_INDEX')
    print(smootheningFactor1,smootheningFactor2,cameraIndex)
    pTime = 0
    cTime = 0
    screenWidth, screenHeight = pt.size()
    plocx, plocy = 0,0
    clocx, clocy = 0,0
    smoothening = 5
    cap = cv2.VideoCapture(0)
    detector = ht.handDetector()
    width = 640
    height = 480
    frame = 100
    framed = 150
    frameu = 10
    cap.set(3,width)
    cap.set(4,height)
    eventlist = []
    if_alt_hold=False
    scroll_mode = False
    drag_mode = False
    distance = 0
    while True:
        try:
            success, img = cap.read()
            img = detector.findHands(img)
            lmlist, bbox = detector.findPosition(img)
            img_flip = cv2.flip(img,1)
            cv2.rectangle(img_flip,(frame,frameu),(width-frame,height-framed),(0,0,255),2)
            x = plocx
            y = plocy
            cTime = time.time()
            fps = 1 / (cTime - pTime)
            pTime = cTime
            
            if(lmlist):
                # print(detector.fingersUp())
                # print(g.recognise(img,detector))

                i=g.recognise(img,detector)
                # print(i)
                eventlist.append(i)

                # if i != 4 or i!=2 :
                #     pt.keyUp('alt')
                #     if_alt_hold = False

                if i==1 :
                    x = np.interp(lmlist[8][1],(frame,width-frame),(0,screenWidth))
                    y = np.interp(lmlist[8][2],(frameu,height-framed),(0,screenHeight))
                    clocx = plocx + (x-plocx)/smoothening
                    clocy = plocy + (y-plocy)/smoothening
                    plocx, plocy = clocx, clocy
                    pt.moveTo(1920 - clocx,clocy)

                if eventlist[4]==8 and i==4 :
                    pt.click(1920 - clocx,clocy)
                #     pt.PAUSE = 0.5

                if eventlist[4]==3 and (i==2 or i==4) :
                    pt.rightClick(1920 - clocx,clocy)

                if eventlist[4]==0 and i==4 :
                    pt.keyDown('alt')
                    if_alt_hold=True
                
                if eventlist[4]==4 and i==2 and if_alt_hold:
                    pt.hotkey('tab')

                if (eventlist[4]==4 or eventlist[4]==2) and (i!=4 and i!=2) :
                    pt.keyUp('alt')
                    if_alt_hold = False

                if i==7 and eventlist[4]==8 and (not drag_mode):
                    drag_mode = True
                    # pt.click()
                    pt.mouseDown(button='left')

                if i==7 and drag_mode :
                    x = np.interp(lmlist[8][1],(frame,width-frame),(0,screenWidth))
                    y = np.interp(lmlist[8][2],(frameu,height-framed),(0,screenHeight))
                    clocx = plocx + (x-plocx)/smoothening
                    clocy = plocy + (y-plocy)/smoothening
                    pt.moveTo(1920 - clocx,clocy)
                    plocx, plocy = clocx, clocy

                if eventlist[4]==7 and i!=7 :
                    drag_mode = False
                    pt.mouseUp(button='left')
                    print("mouseup done")

                # if i==7 :
                #     x = np.interp(lmlist[8][1],(frame,width-frame),(0,screenWidth))
                #     y = np.interp(lmlist[8][2],(frameu,height-framed),(0,screenHeight))
                #     clocx = plocx + (x-plocx)/smoothening
                #     clocy = plocy + (y-plocy)/smoothening
                #     plocx, plocy = clocx, clocy
                #     pt.dragTo(clocx,clocy)

                if i==5 and (not scroll_mode):
                    scroll_mode = True
                    x = np.interp(lmlist[8][1],(frame,width-frame),(0,screenWidth))
                    y = np.interp(lmlist[8][2],(frameu,height-framed),(0,screenHeight))
                    plocx, plocy = x,y
                    clocx,clocy = plocx, plocy

                if i==5 and scroll_mode :
                    x = np.interp(lmlist[8][1],(frame,width-frame),(0,screenWidth))
                    y = np.interp(lmlist[8][2],(frameu,height-framed),(0,screenHeight))
                    clocx = plocx + (x-plocx)/smoothening
                    clocy = plocy + (y-plocy)/smoothening
                    pt.scroll((int)(clocy-plocy)*2)
                    plocx, plocy = clocx, clocy

                if eventlist[4]==5 and i!=5 :
                    scroll_mode = False

                if i==6:
                    x = np.interp(lmlist[8][1],(frame,width-frame),(0,screenWidth))
                    y = np.interp(lmlist[8][2],(frameu,height-framed),(0,screenHeight))
                    clocx = plocx + (x-plocx)/smoothening
                    clocy = plocy + (y-plocy)/smoothening

                    distance += (clocy-plocy)
                    # print(distance, end='            ')
                    if distance >= 10 :
                        while distance >= 10 :
                            pt.press('volumedown')
                            # print('++++++++++++++++++++++')
                            distance = distance-10
                        
                    elif distance <= -10 :
                        # pt.press('volumeup')
                        # distance = 0 - distance
                        while distance <= -10 :
                            pt.press('volumeup')
                            # print('----------------------')
                            distance += 10
                        # distance = 0 - distance

                    # print(distance)
                    
                    plocx, plocy = clocx, clocy

                        
            if len(eventlist)>5 :
                p = eventlist.pop(0)

            cv2.putText(img_flip, str(int(fps)), (10, 70), cv2.FONT_HERSHEY_PLAIN, 3,
                        (255, 0, 255), 3)
            
            cv2.imshow("Image", img_flip)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        except :
            pt.moveTo(screenWidth/2, screenHeight/2)    