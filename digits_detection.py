import cv2
import pytesseract
import numpy as np
from PIL import ImageGrab
import time


pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'

try:
    print("\nPlease Drag Your File to the 'img_digits' directory.")
    print("\nEnter your filename below. Please make sure that your file name is valid. (ex. 'number.jpg')")
    filename = input("> ")
    img = cv2.imread(f"./img_digits/{filename}")
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
except:
    try:
        print("\n!!INVALID FILE NAME. KINDLY DOUBLE CHECK BEFORE ENTERING.")
        print("\nPlease Drag Your File to the 'img_digits' directory.")
        print("\nEnter your filename below. Please make sure that your file name is valid. (ex. 'number.jpg')")
        filename = input("> ")
        img = cv2.imread(f"./img_digits/{filename}")
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    except:
        print("\n!!INVALID FILE NAME. KINDLY DOUBLE CHECK BEFORE ENTERING.")
        print("\nPlease Drag Your File to the 'img_digits' directory.")
        print("\nEnter your filename below. Please make sure that your file name is valid. (ex. 'number.jpg')")
        filename = input("> ")
        img = cv2.imread(f"./img_digits/{filename}")
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        


pytesseract

while True:
    hImg, wImg,_ = img.shape
    conf = r'--oem 3 --psm 6 outputbase digits'
    boxes = pytesseract.image_to_boxes(img,config=conf)

    num = []

    for b in boxes.splitlines():
        b = b.split(' ')
        # print(b)
        num.append(b[0])
        x, y, w, h = int(b[1]), int(b[2]), int(b[3]), int(b[4])
        cv2.rectangle(img, (x,hImg- y), (w,hImg- h), (50, 50, 255), 2)
        cv2.putText(img, f'{b[0]}',(x,hImg- y+25),cv2.FONT_HERSHEY_SIMPLEX,1,(50,50,255),2)


    print(f'\nWe have detected that your number is: {"".join(num)}\n')

    print("\nClick the window and PRESS 'X' to exit.\n")

    cv2.namedWindow('Digit Detection', cv2.WINDOW_NORMAL)
    cv2.resizeWindow('Digit Detection', 500, 500)
    cv2.imshow('Digit Detection', img)

    if cv2.waitKey(0) & 0xFF==ord('x'):
        break

