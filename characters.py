import numpy as np
import cv2
import imutils

import pytesseract
import argparse
import os

from matplotlib import pyplot as plt

characters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
#characters = "3RLTE"
for char in characters:
    charimage1 = imutils.resize(cv2.imread('characters/' + char + '.jpg'), width=200)
    charimage = cv2.cvtColor(charimage1, cv2.COLOR_BGR2GRAY)
    ret,binaryimage = cv2.threshold(charimage,50,255,cv2.THRESH_BINARY_INV)
    f = open('histcharacters/char' + char + '.txt', "a")
    cwhites=0

    size = np.size(binaryimage)
    skel = np.zeros(binaryimage.shape,np.uint8)

    element = cv2.getStructuringElement(cv2.MORPH_CROSS,(3,3))
    done = False
     
    while( not done):
        eroded = cv2.erode(binaryimage,element)
        temp = cv2.dilate(eroded,element)
        temp = cv2.subtract(binaryimage,temp)
        skel = cv2.bitwise_or(skel,temp)
        binaryimage = eroded.copy()
     
        zeros = size - cv2.countNonZero(binaryimage)
        if zeros==size:
            done = True
     
    height, width = skel.shape[:2]
    for c in range(width):
        conta=0
        for l in range(height):
            conta+=skel[l,c] == 255
        #histH.append(conta)
        f.write(str(conta)+",")
    w = open('histcharacters/nwhites' + char + '.txt', "a")

    w.write(str(cv2.countNonZero(skel)))
    #calculating perimeter
    edged = cv2.Canny(skel, 0,10)
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (7, 7))
    closed = cv2.morphologyEx(edged, cv2.MORPH_CLOSE, kernel)
    #finding_contours
    image, contours, hierarchy = cv2.findContours(closed, cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
    perimeter=0
    for c in contours:
        peri = cv2.arcLength(c, True)
        approx = cv2.approxPolyDP(c, 0.02 * peri, True)
        cv2.drawContours(image, [approx], -1, (0, 255, 0), 2)
        perimeter = round(perimeter+cv2.arcLength(c,True),2)
    p = open('histcharacters/perimeter' + char + '.txt', "a")
    p.write(str(perimeter))
    p.close()

