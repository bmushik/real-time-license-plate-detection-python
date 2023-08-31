import cv2
import numpy as np
import pytesseract
pytesseract.pytesseract.tesseract_cmd=r'C:\Program Files\Teseract-OCR\tesseract'
kamera=cv2.VideoCapture(0)
while True:
ret, goruntu=kamera.read()
goruntu = cv2.resize(goruntu, (600, 400)) 
gray = cv2.cvtColor(goruntu.cv2.COLOR_BGR2GRAY)
blur = cv2.GaussianBlur(gray, (3, 3), 0)
edged = cv2.Canny(blur, 15,200)
cnts, new = cv2.findContours(edged.copy(), cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
img1 = goruntu.copy()
contours = sorted(cnts, key=cv2.contourArea, reverse=True)[:7]
screenCnt = None
for c in contours:
    peri = cv2.arcLength(c, True)
    approx = cv2.approxPolyDP(c, 0.018 * peri, True)
    if len(approx) = 4:
        screenCnt = approx
        break
if screenCnt is None:
    detected = 0
else:
    detected = 1
    cv2.drawContours (img1, [screenCnt], -1, (0, 0, 255), 3)
    mask = np.zeros(gray.shape, np.uint8)
    new_image = cv2.drawContours(mask, [screenCnt], 0, 255, -1, )
    new_image = cv2.bitwise_and(img1, img1, mask=mask)
    (x, y) = np.where(mask == 255)
    (topx, topy) = (np.min(x), np.min(y))
    (bottomx, bottomy) = (np.max(x), np.max(y))
    Cropped = gray[topx:bottomx + 1, topy:bottomy + 2]
if detected ==1:
    cv2.imshow('Plaka', Cropped)
    print("Plaka okunuyor.")
    text=pytesseract.image_to_string(Cropped, config='--psm 11')
    print("Araç Sorgu Bilgileri:", text)
    devam = input("Okunan plaka doğru mu?")
    if devam == "Hayır.": print("İşlem baştan alınıyor.")
    elif devam=="Evet.": print("İşlem tamamlandı, q tuşu ile çıkış yapabilirsiniz.")
cv2.imshow("Kayit Ekrani", img1)
ch = cv2.waitKey(100)
if ch == ord('q'):
    break
