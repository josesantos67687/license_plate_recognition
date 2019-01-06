import numpy as np
import cv2
import imutils

import pytesseract
import argparse
import os

from matplotlib import pyplot as plt

alphabet = "E"
for letter in alphabet:
    letterimage = imutils.resize(cv2.imread('letters/letter' + letter + '.png'), width=200, height=200)
    ret,binaryimage = cv2.threshold(letterimage,50,255,cv2.THRESH_BINARY_INV)
    #cv2.imshow("Letter", letterimage)
    histH=[]
    cwhites=0
    for c in range(200):
        conta=0
        for l in range(200):
            conta+=binaryimage[l,c][2] == 255
            cwhites+=binaryimage[l,c][2] == 255
        histH.append(conta)
    f = open('histLetters/letter' + letter + '.txt', "a")
    w = open('histLetters/nwhites' + letter + '.txt', "a")
    f.write(str(histH))
    w.write(str(cwhites))

cv2.waitKey(0)
