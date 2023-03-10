#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import tempfile

import cv2
import numpy as np
from PIL import Image
from PIL import Image, ImageFilter

IMAGE_SIZE = 1800
BINARY_THREHOLD = 180

size = None


def get_size_of_scaled_image(im):
    global size
    if size is None:
        length_x, width_y = im.size
        factor = max(1, int(IMAGE_SIZE / length_x))
        size = factor * length_x, factor * width_y
    return size


def process_image_for_ocr(file_path):
    temp_filename = set_image_dpi(file_path)
    im_new = remove_noise_and_smooth(temp_filename)
    return im_new


def set_image_dpi(file_path):
    im = Image.open(file_path)
    # size = (1800, 1800)
    size = get_size_of_scaled_image(im)
    im_resized = im.resize(size, Image.ANTIALIAS)
    temp_file = tempfile.NamedTemporaryFile(delete=False, suffix='.jpg')
    temp_filename = temp_file.name
    im_resized.save(temp_filename, dpi=(300, 300))
    return temp_filename


def image_smoothening(img):
    ret1, th1 = cv2.threshold(img, BINARY_THREHOLD, 255, cv2.THRESH_BINARY)
    ret2, th2 = cv2.threshold(th1, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    blur = cv2.GaussianBlur(th2, (1, 1), 0)
    ret3, th3 = cv2.threshold(blur, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    return th3


def remove_noise_and_smooth(file_name):
    img = cv2.imread(file_name)
    h, w, *_ = img.shape
    scale_percent = 100 # percent of original size
    width = int(img.shape[1] * scale_percent / 100)
    height = int(img.shape[0] * scale_percent / 100)
    dim = (width, height)

    # resize image
    img = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)

    print("width of the image:", w)
    print("height of the image:", h)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    if (h < 900) and (w < 1200):
        figure_size = 1 # the dimension of the x and y axis of the kernal.
    else: 
        figure_size = 20 # the dimension of the x and y axis of the kernal. 
        ksize = 15 # least value that appears to suppress all defects
        img = cv2.medianBlur(img, ksize=ksize)

    img = cv2.blur(img,(figure_size, figure_size))
    
    filtered = cv2.adaptiveThreshold(img.astype(np.uint8), 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 41, 3)
    kernel = np.ones((1, 1), np.uint8)
    opening = cv2.morphologyEx(filtered, cv2.MORPH_OPEN, kernel)
    closing = cv2.morphologyEx(opening, cv2.MORPH_CLOSE, kernel)
    img = image_smoothening(img)
    or_image = cv2.bitwise_or(img, closing)

    cv2.namedWindow('Detect Text - Preprocessed', cv2.WINDOW_NORMAL)
    cv2.resizeWindow('Detect Text - Preprocessed', 500, 500)
    cv2.imshow("Detect Text - Preprocessed", or_image)
    cv2.waitKey(0)
    return or_image