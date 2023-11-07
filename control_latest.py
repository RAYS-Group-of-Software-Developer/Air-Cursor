import HandTracking as ht
import Gesture as g
import pyautogui as pt
import cv2
import time
import numpy as np
import autopy

if __name__ == "__main__":
    pTime = 0
    cTime = 0
    # screenWidth, screenHeight = pt.size()
    screenWidth, screenHeight = autopy.screen.size()
    plocx, plocy = screenWidth / 2, screenHeight / 2
    clocx, clocy = screenWidth / 2, screenHeight / 2

    file_path = "./config.txt"
    with open(file_path, 'r') as f:
        _smoothness_factor_1 = float(f.readline())
        _smoothness_factor_2 = float(f.readline())
        _camera_index = int(f.readline())

    print(_smoothness_factor_1, _smoothness_factor_2, _camera_index)

    smoothening_cursor_move = _smoothness_factor_1
    smoothening_scroll = _smoothness_factor_2

    smoothening_vol = 1
    cap = cv2.VideoCapture(0)
    detector = ht.handDetector()
    width = 640
    height = 480
    frame = 100
    framed = 150
    frameu = 10
    cap.set(3, width)
    cap.set(4, height)
    # eventlist = []
    prev_event = 0
    alt_hold = False
    scroll_mode = False
    drag_mode = False
    volume_mode = False
    distance = 0

    while True:
        try:
            success, img = cap.read()
            img = detector.findHands(img)
            lmlist, bbox = detector.findPosition(img)
            img_flip = cv2.flip(img, 1)
            cv2.rectangle(img_flip, (frame, frameu), (width - frame, height - framed), (0, 0, 255), 2)
            x = plocx
            y = plocy

            if len(lmlist) != 0:
                x1, y1 = lmlist[8][1:]
                i = g.recognise(img, detector)
                # eventlist.append(i)

                # -------------------------------------------For cursor move-------------------------------
                if i == 1:
                    x = np.interp(x1, (frame, width - frame), (0, screenWidth))
                    y = np.interp(y1, (frameu, height - framed), (0, screenHeight))
                    clocx = plocx + (x - plocx) / smoothening_cursor_move
                    clocy = plocy + (y - plocy) / smoothening_cursor_move
                    # pt.moveTo(screenWidth - clocx,clocy)
                    autopy.mouse.move(screenWidth - clocx, clocy)
                    plocx, plocy = clocx, clocy



                # -------------------------------------------For left click-------------------------------
                if prev_event == 8 and i == 4:
                    # pt.click(screenWidth - clocx, clocy)
                    autopy.mouse.click(autopy.mouse.Button.LEFT)


                # -------------------------------------------For right click------------------------------
                if prev_event == 3 and (i == 2 or i == 4):
                    # pt.rightClick(screenWidth - clocx,clocy)
                    autopy.mouse.click(autopy.mouse.Button.RIGHT)


                # -------------------------------------------For tab change-------------------------------
                if prev_event == 0 and i == 4:
                    # pt.keyDown('alt')
                    autopy.key.toggle(autopy.key.Code.ALT, True)
                    alt_hold = True

                if prev_event == 4 and i == 2 and alt_hold:
                    # pt.hotkey('tab')
                    autopy.key.tap(autopy.key.Code.TAB)

                if (prev_event == 4 or prev_event == 2) and (i != 4 and i != 2):
                    autopy.key.toggle(autopy.key.Code.ALT, False)
                    alt_hold = False


                # -------------------------------------------For holding with dragging-------------------------------
                if i == 7 and prev_event == 8 and (not drag_mode):
                    drag_mode = True
                    pt.mouseDown(button='left')
                    # autopy.mouse.toggle(True, autopy.mouse.Button.LEFT)

                if i == 7 and drag_mode:
                    x = np.interp(x1, (frame, width - frame), (0, screenWidth))
                    y = np.interp(y1, (frameu, height - framed), (0, screenHeight))
                    clocx = plocx + (x - plocx) / smoothening_cursor_move
                    clocy = plocy + (y - plocy) / smoothening_cursor_move
                    # pt.moveTo(screenWidth - clocx, clocy)
                    autopy.mouse.move(screenWidth - clocx, clocy)
                    plocx, plocy = clocx, clocy

                if prev_event == 7 and i != 7:
                    drag_mode = False
                    pt.mouseUp(button='left')
                    # autopy.mouse.toggle(False, autopy.mouse.Button.LEFT)


                # -----------------------------------------For scrolling-------------------------------
                if i == 5:
                    x = np.interp(x1, (frame, width - frame), (0, screenWidth))
                    y = np.interp(y1, (frameu, height - framed), (0, screenHeight))

                    if scroll_mode:
                        # clocx = plocx + (x - plocx) / smoothening_scroll
                        # clocy = plocy + (y - plocy) / smoothening_scroll
                        clocy = y
                        clocx = x
                        if(clocy - plocy>10 or clocy - plocy<-10):
                            pt.scroll(int(clocy - plocy) * 2)

                            # print(int(clocy - plocy) * 2)
                        # autopy.mouse.scroll(int((clocy-plocy)*2))
                        plocx, plocy = clocx, clocy

                    else:
                        scroll_mode = True
                        clocx, clocy = plocx, plocy = x, y

                if prev_event == 5 and i != 5:
                    scroll_mode = False


                # ----------------------------------------For volume level-------------------------------

                # if i == 6 and (not volume_mode):
                #     volume_mode = True
                #
                # if i == 6 and volume_mode:
                #     x = np.interp(x1, (frame, width - frame), (0, screenWidth))
                #     y = np.interp(y1, (frameu, height - framed), (0, screenHeight))
                #     clocx = plocx + (x - plocx) / smoothening_vol
                #     clocy = plocy + (y - plocy) / smoothening_vol
                #
                #     if clocy > plocy:
                #         # for c in range(int(clocy-plocy)*2):
                #         pt.press('volumedown')
                #     elif clocy < plocy:
                #         # for g in range(int(plocy-clocy)*2):
                #         pt.press('volumeup')
                #
                #     plocx, plocy = clocx, clocy
                #
                # if prev_event == 6 and i != 6:
                #     volume_mode = False

                if prev_event == 6 and i == 6:
                    x = np.interp(x1, (frame, width - frame), (0, screenWidth))
                    y = np.interp(y1, (frameu, height - framed), (0, screenHeight))
                    clocx = plocx + (x - plocx) / smoothening_vol
                    clocy = plocy + (y - plocy) / smoothening_vol

                    # if clocy <= 2 * height / 3:
                    #     pt.press('volumeup')
                    # elif clocy > 2 * height / 3:
                    #     pt.press('volumedown')
                    if clocy <=  height:
                        pt.press('volumeup')
                        pt.press('volumeup')
                    elif clocy > height :
                        pt.press('volumedown')

                    plocx, plocy = clocx, clocy

                # if i == 6:
                #     x = np.interp(x1,(frame,width-frame),(0,screenWidth))
                #     y = np.interp(y1,(frameu,height-framed),(0,screenHeight))
                #     clocx = plocx + (x-plocx)/smoothening
                #     clocy = plocy + (y-plocy)/smoothening
                #
                #     distance += (clocy-plocy)
                #     if distance >= 10:
                #         # while distance >= 10:
                #         pt.press('volumedown')
                #         distance = 0
                #
                #     elif distance <= -5:
                #         # while distance <= -10:
                #         pt.press('volumeup')
                #         # pt.press('volumeup')
                #         distance = 0
                #
                #     plocx, plocy = clocx, clocy

                # ---------------------------------------Storing last gesture-------------------------------
                prev_event = i


            else:
                prev_event = 0
                if drag_mode:
                    pt.mouseUp(button='left')
                if alt_hold:
                    autopy.key.toggle(autopy.key.Code.ALT, False)

            # ---------------------------------------Utility----------------------------------

            cTime = time.time()
            fps = 1 / (cTime - pTime)
            pTime = cTime
            cv2.putText(img_flip, "FPS : "+str(int(fps)), (10, 70), cv2.FONT_HERSHEY_PLAIN, 3,
                        (255, 0, 255), 3)
            # cv2.putText(img_flip, str(int(prev_event)), (20, 120), cv2.FONT_HERSHEY_PLAIN, 3, (200, 0, 0), 3)

            cv2.imshow("Camera feed", img_flip)

            # ----------------------------------To stop the program-------------------------------------

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

            # -------------------------------------In case any exception occurs-------------------------------

        except:
            pt.moveTo(screenWidth / 2, screenHeight / 2)
