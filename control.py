import HandTracking as ht
import Gesture as g
import pyautogui as pt
import cv2
import time
import numpy as np

      
class Runner():
    def __init__(self,
                pTime: int = 0,
                cTime: int = 0,
                screenSize: tuple[int,int] = pt.size(),
                plocx: int = 0,
                plocy: int = 0,
                clocx: int = 0,
                clocy: int = 0,
                smoothening: int = 5,
                camera_var: int = 0,
                width: int = 640,
                height: int = 480,
                frame: int = 100,
                framed: int = 150,
                frameu: int = 10,
                ):
        super().__init__()
        self.screenWidth, self.screenHeight = screenSize
        self.pTime = pTime
        self.cTime = cTime
        self.plocx = plocx
        self.plocy = plocy
        self.clocx = clocx
        self.clocy = clocy
        self.smoothening = smoothening
        self.camera_var = camera_var
        self.width = width
        self.height = height
        self.frame = frame
        self.framed = framed
        self.frameu = frameu
        
        self.previous = 0
        self.if_alt_hold=False
        self.scroll_mode = False
        self.drag_mode = False
        self.distance = 0
        
        # function to run the program
    def run(self):
        self.cap = cv2.VideoCapture(self.camera_var)
        self.detector = ht.handDetector()
        self.cap.set(3,self.width)
        self.cap.set(4,self.height)
        while True:
            try:
                success, img = self.cap.read()
                img = self.detector.findHands(img)
                lmlist, bbox = self.detector.findPosition(img)
                img_flip = cv2.flip(img,1)
                cv2.rectangle(img_flip,(self.frame,self.frameu),(self.width-self.frame,self.height-self.framed),(0,0,255),2)
                x = self.plocx
                y = self.plocy
                cTime = time.time()
                fps = 1 / (cTime - pTime)
                pTime = cTime
                
                if(lmlist):
                    # print(self.detector.fingersUp())
                    # print(g.recognise(img,self.detector))

                    i=g.recognise(img,self.detector)
                    # print(i)
                    self.eventlist.append(i)

                    # if i != 4 or i!=2 :
                    #     pt.keyUp('alt')
                    #     if_alt_hold = False

                    if i==1 :
                        x = np.interp(lmlist[8][1],(self.frame,self.width-self.frame),(0,self.screenWidth))
                        y = np.interp(lmlist[8][2],(self.frameu,self.height-self.framed),(0,self.screenHeight))
                        self.clocx = self.plocx + (x-plocx)/self.smoothening
                        self.clocy = self.plocy + (y-plocy)/self.smoothening
                        self.plocx, self.plocy = self.clocx, self.clocy
                        pt.moveTo(self.screenWidth - self.clocx,self.clocy)

                    if self.previous==8 and i==4 :
                        pt.click(1920 - self.clocx,clocy)
                    #     pt.PAUSE = 0.5

                    if self.previous==3 and (i==2 or i==4) :
                        pt.rightClick(1920 - self.clocx,clocy)

                    if self.previous==0 and i==4 :
                        pt.keyDown('alt')
                        if_alt_hold=True
                    
                    if self.previous==4 and i==2 and if_alt_hold:
                        pt.hotkey('tab')

                    if (self.previous==4 or self.previous==2) and (i!=4 and i!=2) :
                        pt.keyUp('alt')
                        if_alt_hold = False

                    if i==7 and self.previous==8 and (not drag_mode):
                        drag_mode = True
                        # pt.click()
                        pt.mouseDown(button='left')

                    if i==7 and drag_mode :
                        x = np.interp(lmlist[8][1],(self.frame,self.width-self.frame),(0,self.screenWidth))
                        y = np.interp(lmlist[8][2],(self.frameu,self.height-self.framed),(0,self.screenHeight))
                        self.clocx = plocx + (x-plocx)/self.smoothening
                        clocy = plocy + (y-plocy)/self.smoothening
                        pt.moveTo(1920 - self.clocx,clocy)
                        plocx, plocy = self.clocx, clocy

                    if self.previous==7 and i!=7 :
                        drag_mode = False
                        pt.mouseUp(button='left')
                        print("mouseup done")

                    # if i==7 :
                    #     x = np.interp(lmlist[8][1],(self.frame,self.width-self.frame),(0,self.screenWidth))
                    #     y = np.interp(lmlist[8][2],(self.frameu,self.height-self.framed),(0,self.screenHeight))
                    #     self.clocx = plocx + (x-plocx)/self.smoothening
                    #     clocy = plocy + (y-plocy)/self.smoothening
                    #     plocx, plocy = self.clocx, clocy
                    #     pt.dragTo(self.clocx,clocy)

                    if i==5 and (not scroll_mode):
                        scroll_mode = True
                        x = np.interp(lmlist[8][1],(self.frame,self.width-self.frame),(0,self.screenWidth))
                        y = np.interp(lmlist[8][2],(self.frameu,self.height-self.framed),(0,self.screenHeight))
                        plocx, plocy = x,y
                        self.clocx,clocy = plocx, plocy

                    if i==5 and scroll_mode :
                        x = np.interp(lmlist[8][1],(self.frame,self.width-self.frame),(0,self.screenWidth))
                        y = np.interp(lmlist[8][2],(self.frameu,self.height-self.framed),(0,self.screenHeight))
                        self.clocx = plocx + (x-plocx)/self.smoothening
                        clocy = plocy + (y-plocy)/self.smoothening
                        pt.scroll((int)(clocy-plocy)*2)
                        plocx, plocy = self.clocx, clocy

                    if self.previous==5 and i!=5 :
                        scroll_mode = False

                    if i==6:
                        x = np.interp(lmlist[8][1],(self.frame,self.width-self.frame),(0,self.screenWidth))
                        y = np.interp(lmlist[8][2],(self.frameu,self.height-self.framed),(0,self.screenHeight))
                        self.clocx = plocx + (x-plocx)/self.smoothening
                        clocy = plocy + (y-plocy)/self.smoothening

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
                        
                        plocx, plocy = self.clocx, clocy

                            
                if len(self.eventlist)>5 :
                    p = self.eventlist.pop(0)

                cv2.putText(img_flip, str(int(fps)), (10, 70), cv2.FONT_HERSHEY_PLAIN, 3,
                            (255, 0, 255), 3)
                
                cv2.imshow("Image", img_flip)
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break
            except :
                pt.moveTo(self.screenWidth/2, self.screenHeight/2)    
         
        

# if __name__ == "__main__":
#     pTime = 0
#     cTime = 0
#     screenWidth, screenHeight = pt.size()
#     print(screenWidth,screenHeight)
#     plocx, plocy = 0,0
#     self.clocx, clocy = 0,0
#     smoothening = 5
#     camera_var = 0
#     cap = cv2.VideoCapture(camera_var)
#     detector = ht.handDetector()
#     width = 740
#     height = 480
#     frame = 100
#     framed = 150
#     frameu = 10
#     cap.set(3,width)
#     cap.set(4,height)
#     eventlist = []
#     if_alt_hold=False
#     scroll_mode = False
#     drag_mode = False
#     distance = 0
#     while True:
#         try:
#             success, img = cap.read()
#             img = detector.findHands(img)
#             lmlist, bbox = detector.findPosition(img)
#             img_flip = cv2.flip(img,1)
#             cv2.rectangle(img_flip,(frame,frameu),(width-frame,height-framed),(0,0,255),2)
#             x = plocx
#             y = plocy
#             cTime = time.time()
#             fps = 1 / (cTime - pTime)
#             pTime = cTime
            
#             if(lmlist):
#                 # print(detector.fingersUp())
#                 # print(g.recognise(img,detector))

#                 i=g.recognise(img,detector)
#                 # print(i)
#                 eventlist.append(i)

#                 # if i != 4 or i!=2 :
#                 #     pt.keyUp('alt')
#                 #     if_alt_hold = False

#                 if i==1 :
#                     x = np.interp(lmlist[8][1],(frame,width-frame),(0,screenWidth))
#                     y = np.interp(lmlist[8][2],(frameu,height-framed),(0,screenHeight))
#                     self.clocx = plocx + (x-plocx)/smoothening
#                     clocy = plocy + (y-plocy)/smoothening
#                     plocx, plocy = self.clocx, clocy
#                     pt.moveTo(1920 - self.clocx,clocy)

#                 if previous==8 and i==4 :
#                     pt.click(1920 - self.clocx,clocy)
#                 #     pt.PAUSE = 0.5

#                 if previous==3 and (i==2 or i==4) :
#                     pt.rightClick(1920 - self.clocx,clocy)

#                 if previous==0 and i==4 :
#                     pt.keyDown('alt')
#                     if_alt_hold=True
                
#                 if previous==4 and i==2 and if_alt_hold:
#                     pt.hotkey('tab')

#                 if (previous==4 or previous==2) and (i!=4 and i!=2) :
#                     pt.keyUp('alt')
#                     if_alt_hold = False

#                 if i==7 and previous==8 and (not drag_mode):
#                     drag_mode = True
#                     # pt.click()
#                     pt.mouseDown(button='left')

#                 if i==7 and drag_mode :
#                     x = np.interp(lmlist[8][1],(frame,width-frame),(0,screenWidth))
#                     y = np.interp(lmlist[8][2],(frameu,height-framed),(0,screenHeight))
#                     self.clocx = plocx + (x-plocx)/smoothening
#                     clocy = plocy + (y-plocy)/smoothening
#                     pt.moveTo(1920 - self.clocx,clocy)
#                     plocx, plocy = self.clocx, clocy

#                 if previous==7 and i!=7 :
#                     drag_mode = False
#                     pt.mouseUp(button='left')
#                     print("mouseup done")

#                 # if i==7 :
#                 #     x = np.interp(lmlist[8][1],(frame,width-frame),(0,screenWidth))
#                 #     y = np.interp(lmlist[8][2],(frameu,height-framed),(0,screenHeight))
#                 #     self.clocx = plocx + (x-plocx)/smoothening
#                 #     clocy = plocy + (y-plocy)/smoothening
#                 #     plocx, plocy = self.clocx, clocy
#                 #     pt.dragTo(self.clocx,clocy)

#                 if i==5 and (not scroll_mode):
#                     scroll_mode = True
#                     x = np.interp(lmlist[8][1],(frame,width-frame),(0,screenWidth))
#                     y = np.interp(lmlist[8][2],(frameu,height-framed),(0,screenHeight))
#                     plocx, plocy = x,y
#                     self.clocx,clocy = plocx, plocy

#                 if i==5 and scroll_mode :
#                     x = np.interp(lmlist[8][1],(frame,width-frame),(0,screenWidth))
#                     y = np.interp(lmlist[8][2],(frameu,height-framed),(0,screenHeight))
#                     self.clocx = plocx + (x-plocx)/smoothening
#                     clocy = plocy + (y-plocy)/smoothening
#                     pt.scroll((int)(clocy-plocy)*2)
#                     plocx, plocy = self.clocx, clocy

#                 if previous==5 and i!=5 :
#                     scroll_mode = False

#                 if i==6:
#                     x = np.interp(lmlist[8][1],(frame,width-frame),(0,screenWidth))
#                     y = np.interp(lmlist[8][2],(frameu,height-framed),(0,screenHeight))
#                     self.clocx = plocx + (x-plocx)/smoothening
#                     clocy = plocy + (y-plocy)/smoothening

#                     distance += (clocy-plocy)
#                     # print(distance, end='            ')
#                     if distance >= 10 :
#                         while distance >= 10 :
#                             pt.press('volumedown')
#                             # print('++++++++++++++++++++++')
#                             distance = distance-10
                        
#                     elif distance <= -10 :
#                         # pt.press('volumeup')
#                         # distance = 0 - distance
#                         while distance <= -10 :
#                             pt.press('volumeup')
#                             # print('----------------------')
#                             distance += 10
#                         # distance = 0 - distance

#                     # print(distance)
                    
#                     plocx, plocy = self.clocx, clocy

                        
#             if len(eventlist)>5 :
#                 p = eventlist.pop(0)

#             cv2.putText(img_flip, str(int(fps)), (10, 70), cv2.FONT_HERSHEY_PLAIN, 3,
#                         (255, 0, 255), 3)
            
#             cv2.imshow("Image", img_flip)
#             if cv2.waitKey(1) & 0xFF == ord('q'):
#                 break
#         except :
#             pt.moveTo(screenWidth/2, screenHeight/2)    
            
            
# run the program
if __name__ == "__main__":
    runner = Runner()
    runner.run()          
