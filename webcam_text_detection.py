import cv2
import pytesseract
import numpy as np
from PIL import ImageGrab
import os
import re
from remove_noise import process_image_for_ocr

pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'

pytesseract

## Text Detection in Real-time
camera_capture = cv2.VideoCapture(0)
camera_capture.set(3,640)
camera_capture.set(4,480)

## Text Detection in Screen Capture
# Return the number of the last image
def generate_img_path():
    paths = []
    path_nums = []
    pathSpecified = os.getcwd()
    listOfFileNames = os.listdir(pathSpecified) 

    for num, i in enumerate(listOfFileNames):
        if "image" in i:
            paths.append(i.split(".")[0])

    split_word = 'image'

    for num, i in enumerate(paths):
        res = i.split(split_word, 1)
        splitString = res[1]
        path_nums.append(int(splitString))

    return max(path_nums) + 1

print("\nClick the window and PRESS 'S' to save/screenshot the image from the webcam and exit.\n")

while True:
    _,img = camera_capture.read()
    # conf = r'--oem 2 --psm 3'

    hImg, wImg,_ = img.shape
    boxes = pytesseract.image_to_boxes(img)
    text = []

    for a,b in enumerate(boxes.splitlines()):
            text.append(b[0])
            
            if a!=0:
                b = b.split()
                if len(b)==12:
                    x,y,w,h = int(b[6]),int(b[7]),int(b[8]),int(b[9])
                    cv2.rectangle(img, (x,y), (x+w, y+h), (50, 50, 255), 2)
                    cv2.putText(img,b[11],(x,y-5),cv2.FONT_HERSHEY_SIMPLEX,1,(50,50,255),2)
                        
    cv2.imshow("Detect Text",img)

    print(f'\nWe have detected that your text is: {"".join(text)}\n')

    if cv2.waitKey(1) & 0xFF==ord('s'):
        cv2.imwrite(f'image{generate_img_path()}.jpg', img)
        break

camera_capture.release()
cv2.destroyAllWindows()


def make_string_alphanumeric(lines):
    s = re.sub(r'\W+', '', lines)
    return s.strip()


def read_image_from_file():
    ts_path = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'
    pytesseract.pytesseract.tesseract_cmd = ts_path

    filename = f'image{generate_img_path()-1}.jpg'
    
    cv2.imshow("Detect Text - Before", cv2.imread(filename))
    cv2.waitKey(0)

    # Pre-process image
    # image = process_image_for_ocr(filename)

    image = cv2.imread(filename)

    boxes = pytesseract.image_to_boxes(image)
    text = []

    for a,b in enumerate(boxes.splitlines()):
            text.append(b[0])
            
            if a!=0:
                b = b.split()
                if len(b)==12:
                    x,y,w,h = int(b[6]),int(b[7]),int(b[8]),int(b[9])
                    cv2.rectangle(img, (x,y), (x+w, y+h), (50, 50, 255), 2)
                    cv2.putText(img,b[11],(x,y-5),cv2.FONT_HERSHEY_SIMPLEX,1,(50,50,255),2)
    
    cv2.waitKey(0) 

    print(f'\nWe have detected that your text is: \n=====START OF TEXT=====\n{make_string_alphanumeric("".join(text))}\n=====END OF TEXT=====\n')

read_image_from_file()
