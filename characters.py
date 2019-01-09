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
    charimage = imutils.resize(cv2.imread('characters/' + char + '.jpg'), width=500)
    ret,binaryimage = cv2.threshold(charimage,50,255,cv2.THRESH_BINARY_INV)
    f = open('histcharacters/char' + char + '.txt', "a")
    cwhites=0
    height, width = binaryimage.shape[:2]
    for c in range(width):
        conta=0
        for l in range(height):
            conta+=binaryimage[l,c][2] == 255
            cwhites+=binaryimage[l,c][2] == 255
        #histH.append(conta)
        f.write(str(conta)+",")
    w = open('histcharacters/nwhites' + char + '.txt', "a")
    w.write(str(cwhites))
    #calculating perimeter
    edged = cv2.Canny(binaryimage, 0,10)
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (7, 7))
    closed = cv2.morphologyEx(edged, cv2.MORPH_CLOSE, kernel)
    #finding_contours
    image, contours, hierarchy = cv2.findContours(closed, cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
    perimeter=0
    for c in contours:
        peri = cv2.arcLength(c, True)
        approx = cv2.approxPolyDP(c, 0.02 * peri, True)
        cv2.drawContours(image, [approx], -1, (0, 255, 0), 2)
        perimeter = perimeter+cv2.arcLength(c,True)
        p = open('histcharacters/perimeter' + char + '.txt', "a")
        p.write(str(perimeter))

