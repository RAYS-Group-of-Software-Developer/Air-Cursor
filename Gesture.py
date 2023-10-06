import cv2
import HandTracking as ht
import time

def recognise(img,tracker):
    try:
        l = tracker.fingersUp()
        if all(l)==1 :
            return "open palm"
        if l[0]==0 and l[1]==1 and all(l[2:])==0 :
            return "only index"
        if all(l)==0 :
            return "fist"
    except:
        return "None"

if __name__ == "__main__":
    pTime = 0
    cTime = 0
    cap = cv2.VideoCapture(0)
    detector = ht.handDetector()
    while True:
        success, img = cap.read()
        img = detector.findHands(img)
        lmList, bbox = detector.findPosition(img)
        if len(lmList) != 0:
            print(lmList[4])
        
        if(detector.fingersUp()):
            print(detector.fingersUp())
            print(recognise(img,detector))

        cTime = time.time()
        fps = 1 / (cTime - pTime)
        pTime = cTime

        cv2.putText(img, str(int(fps)), (10, 70), cv2.FONT_HERSHEY_PLAIN, 3,
                    (255, 0, 255), 3)

        cv2.imshow("Image", img)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    