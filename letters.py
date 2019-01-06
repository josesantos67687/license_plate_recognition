import numpy as np
import cv2
import imutils

import pytesseract
import argparse
import os

from matplotlib import pyplot as plt

alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
for letter in alphabet:
    letterimage = imutils.resize(cv2.imread('letters/letter' + letter + '.png'), width=200, height=200)
    ret,binaryimage = cv2.threshold(letterimage,50,255,cv2.THRESH_BINARY_INV)
    #cv2.imshow("Letter", letterimage)
    histH=[]
    cwhites=0
    height, width = binaryimage.shape[:2]
    for c in range(width):
        conta=0
        for l in range(height):
            conta+=binaryimage[l,c][2] == 255
            cwhites+=binaryimage[l,c][2] == 255
        histH.append(conta)
    f = open('histLetters/letter' + letter + '.txt', "a")
    w = open('histLetters/nwhites' + letter + '.txt', "a")
    f.write(str(histH))
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
        print(perimeter)
        p = open('histLetters/perimeter' + letter + '.txt', "a")
        p.write(str(perimeter))

cv2.waitKey(0)
