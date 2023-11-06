import cv2
import HandTracking as ht
import time

class Gesture:
    def __init__(self) -> None:
        super().__init__()
    
    def recognise(img,tracker):
        length, img_r, ll = tracker.findDistance(4,8,img,False,0,0)
        lms, bbox = tracker.findPosition(img,0,True)
        ymin = bbox[1]
        ymax = bbox[3]
        try:
            l = tracker.fingersUp()
            par = (ymax-ymin)/length
            # print(l)
            # print(par)
            # print(bbox)
            #volume

            if par>10 and l[2]==1 and l[3]==1 and l[4]==1 :
                return 6
            # palm
            if l[0]==1 and l[1]==1 and l[2]==1 and l[3]==1 and l[4]==1 :
                return 0
            # index finger up only thumb closed
            if l[0]==0 and l[1]==1 and l[2]==0 and l[3]==0 and l[4]==0:
                return 1
            # index finger up and thumb open
            if l[0]==1 and l[1]==1 and l[2]==0 and l[3]==0 and l[4]==0:
                return 8
            # scroll
            if l[0]==0 and l[4]==0 and l[1]==1 and l[2]==1 and l[3]==1 :
                return 5
            # drag
            if l[0]==1 and l[1]==1 and l[4]==1 and l[2]==0 and l[3]==0 :
                return 7
            # volume
            # if tracker.lmList[8][2] > tracker.lmList[7][2] and tracker.lmList[12][2] > tracker.lmList[11][2] and tracker.lmList[16][2] > tracker.lmList[15][2] and tracker.lmList[8][2]<tracker.lmList[5][2] and tracker.lmList[12][2]<tracker.lmList[9][2] and tracker.lmList[16][2] < tracker.lmList[13][2] and l[4]==0 :
            #     return 5
            #fist
            if l[0]==0 and l[1]==0 and l[2]==0 and l[3]==0 and l[4]==0 :
                return 2
            #middle and index finger up
            if l[3]==0 and l[4]==0 and l[1]==1 and l[2]==1 :
                return 3
            #
            if l[0]==1 and l[1]==0 and l[2]==0 and l[3]==0 and l[4]==0 :
                return 4
            if l[0]==0 and l[1]==1 and l[2]==1 and l[3]==1 and l[4]==1 :
                return 9
            # drag
            # if lmlist[8][2] < lmlist[7][2] and lmlist[12][2] < lmlist[11][2] and l[3]==0 and l[4]==0:
            #     return 5
        except:
            return -1

if __name__ == "__main__":
    pTime = 0
    cTime = 0
    cap = cv2.VideoCapture(0)
    detector = ht.handDetector()
    while True:
        success, img = cap.read()
        img = detector.findHands(img)
        bbox = detector.findPosition(img)
        # if len(lmList) != 0:
            # print(lmList[4])
        
        # if(detector.fingersUp()):
            # print(detector.fingersUp())
            # print(recognise(img,detector),end=" ")
            # i=recognise(img,detector)

        cTime = time.time()
        fps = 1 / (cTime - pTime)
        pTime = cTime

        cv2.putText(img, str(int(fps)), (10, 70), cv2.FONT_HERSHEY_PLAIN, 3,
                    (255, 0, 255), 3)

        cv2.imshow("Image", img)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break


