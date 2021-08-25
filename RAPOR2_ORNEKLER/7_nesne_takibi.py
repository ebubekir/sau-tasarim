import cv2

cap = cv2.VideoCapture(0)

tracker = cv2.legacy.TrackerMOSSE_create()
success, img = cap.read()
bbox = cv2.selectROI('Izleniyor..', img, False)
tracker.init(img, bbox)

def draw_box(img, bbox):
    x,y,w,h = int(bbox[0]),int(bbox[1]),int(bbox[2]),int(bbox[3])
    cv2.rectangle(img, (x,y),((x+w), (y+h)), (255, 0, 255), 3,1)
    cv2.putText(img, 'Izleniyor..', (0, 55), cv2.FONT_HERSHEY_COMPLEX,0.75, (0, 255, 0), 2)

while True:
    timer = cv2.getTickCount()
    success, img = cap.read()

    success, bbox = tracker.update(img)

    if success:
        draw_box(img, bbox)
    else:
        cv2.putText(img, 'Kayboldu', (0, 55), cv2.FONT_HERSHEY_COMPLEX,0.75, (0, 0, 255), 2)

    fps = cv2.getTickFrequency()/(cv2.getTickCount()-timer)
    cv2.putText(img, str(int(fps)), (0, 25), cv2.FONT_HERSHEY_COMPLEX,0.75, (0, 0, 255), 2)

    cv2.imshow('Izleniyor..', img)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break