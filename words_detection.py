import cv2
import pytesseract
import numpy as np
from PIL import ImageGrab
import time


pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'

try:
    print("\nPlease Drag Your File to the 'img_words' directory.")
    print("\nEnter your filename below. Please make sure that your file name is valid. (ex. 'number.jpg')")
    filename = input("> ")
    img = cv2.imread(f"./img_words/{filename}")
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
except:
    try:
        print("\n!!INVALID FILE NAME. KINDLY DOUBLE CHECK BEFORE ENTERING.")
        print("\nPlease Drag Your File to the 'img_words' directory.")
        print("\nEnter your filename below. Please make sure that your file name is valid. (ex. 'number.jpg')")
        filename = input("> ")
        img = cv2.imread(f"./img_words/{filename}")
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    except:
        print("\n!!INVALID FILE NAME. KINDLY DOUBLE CHECK BEFORE ENTERING.")
        print("\nPlease Drag Your File to the 'img_words' directory.")
        print("\nEnter your filename below. Please make sure that your file name is valid. (ex. 'number.jpg')")
        filename = input("> ")
        img = cv2.imread(f"./img_words/{filename}")
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

pytesseract


while True:
    boxes = pytesseract.image_to_data(img)
    text = []
    
    for a,b in enumerate(boxes.splitlines()):
            if a!=0:
                b = b.split()
                if len(b)==12:
                    text.append(b[11])
                    x,y,w,h = int(b[6]),int(b[7]),int(b[8]),int(b[9])
                    # cv2.rectangle(img, (x,y), (x+w, y+h), (50, 50, 255), 2)
                    cv2.putText(img,b[11],(x,y-5),cv2.FONT_HERSHEY_SIMPLEX,1,(50,50,255),2)
                    cv2.rectangle(img, (x,y), (x+w, y+h), (50, 50, 255), 2)

                    

    print(f'\nWe have detected that your text is: \n=====START OF TEXT=====\n{" ".join(text)}\n=====END OF TEXT=====\n')

    print("\nClick the window and PRESS 'X' to exit.\n")

    cv2.namedWindow('Words Detection', cv2.WINDOW_NORMAL)
    cv2.resizeWindow('Words Detection', 500, 500)
    cv2.imshow('Words Detection', img)

    if cv2.waitKey(0) & 0xFF==ord('x'):
        break
                
                