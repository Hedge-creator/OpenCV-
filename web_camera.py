import cv2

cap = cv2.VideoCapture(0) #подключаемся к камеры, указываем индекс
cap.set(cv2.CAP_PROP_FPS, 30) # Частота кадров
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 600) # Ширина кадров 
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480) # Высота кадров
while True:
    ret, img = cap.read() #читаем с устройсва картинку
    cv2.imshow("web camera", img) #отображаем изображение в указанном окне
    if cv2.waitKey(10) == 27: # Клавиша Esc
        break
cap.release()
cv2.destroyAllWindows()
