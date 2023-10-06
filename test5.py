import pyautogui as pt
import HandTracking as ht
import cv2
import time

screenWidth, screenHeight = pt.size()
# screenHeight = screenHeight - 1
# screenWidth = screenWidth - 1

def main():
    pTime = 0
    cTime = 0
    cap = cv2.VideoCapture(0)
    cap.set(3,960)
    cap.set(4,540)
    detector = ht.handDetector()
    while True:
        success, img = cap.read()
        img = detector.findHands(img)
        lmList, bbox = detector.findPosition(img)
        # if len(lmList) != 0:
            # print(lmList[4])

        l = detector.fingersUp()
        if l:
            print(l)
            x = lmList[6][1]*screenWidth / 320
            y = lmList[6][2]*screenHeight / 180
            # pt.moveTo(x,y,duration=0.002)
            print(screenWidth,screenHeight)
            if x > 1920 :
                x=1900
            if y > 1200 :
                y=1180
            x = 1920 - x
            print(x,y)
            if l[1]==1 and l[0]==0 and all(l[2:])==0 :
                pt.moveTo(x,y)
            if all(l[1:3])==1 and all(l[3:])==0 and l[0]==0 :
                pt.click(x,y)
                pt.PAUSE = 0.5


        cTime = time.time()
        fps = 1 / (cTime - pTime)
        pTime = cTime

        cv2.putText(img, str(int(fps)), (10, 70), cv2.FONT_HERSHEY_PLAIN, 3,
                    (255, 0, 255), 3)

        cv2.imshow("Image", img)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

if __name__ == "__main__":
    main()
