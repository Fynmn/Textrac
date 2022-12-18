import os

# def gen():
#     pathSpecified = os.chdir('./img_webcam')
#     # pathSpecified = os.getcwd()
#     listOfFileNames = os.listdir(pathSpecified) 

#     print(listOfFileNames)

# gen()


def generate_img_path():
    paths = []
    path_nums = []
    pathSpecified = os.getcwd()
    pathSpecified = os.chdir('.\\img_webcam')
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

# print(generate_img_path())

import cv2

filename = f'image{generate_img_path()-1}.jpg'
image = cv2.imread(filename)

print(filename)

# print(os.getcwd())