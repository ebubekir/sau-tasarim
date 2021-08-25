import cv2
import imageio
import sys
import numpy as np

video_capture = cv2.VideoCapture(0)

ilk_frame = None

while True:
    _, frame = video_capture.read()

    # her frame icin gri renge cevirilir
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # kamera ilk calistiginda elde edilen ilk goruntu
    # ilk_frame degiskenine aktarilir.
    if ilk_frame is None:
        ilk_frame = gray
    else:
        pass
    
    # t zamanindaki goruntu ile onceki goruntu
    # arasindaki mutlak farki alinacak on plan 
    # tespiti yapilmaktadir.
    img = cv2.absdiff(ilk_frame, gray)
    # elde edilen on plandaki veri uzerinde esikleme
    # uygulanarak binary goruntu elde edilmektedir.
    _, f1 = cv2.threshold(img, 100, 255, cv2.THRESH_BINARY)
    ilk_frame = gray
    cv2.imshow('orijinal', gray)
    cv2.imshow('arka plan cikarim', f1)

    key = cv2.waitKey(1) & 0xFF
    if key == ord('q'):
        cv2.destroyAllWindows()
        break

