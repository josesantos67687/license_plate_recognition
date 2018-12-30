import numpy as np
import cv2
import imutils

import pytesseract
import argparse
import os

from matplotlib import pyplot as plt

#alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
alphabet = 'A'
for letter in alphabet:
    letterimage = imutils.resize(cv2.imread('letters/letter' + letter + '.png'), width=200, height=200)
    ret,binaryimage = cv2.threshold(letterimage,50,255,cv2.THRESH_BINARY_INV)
    #cv2.imshow("Letter", binarymat)
    histH=[]
    for c in range(200):
        conta=0
        for l in range(200):
            conta+=binaryimage[l,c][2] == 255
        histH.append(conta)
    f = open('histLetters/letter' + letter + '.txt', "a")
    f.write(str(histH))

    alphabet = 'B'
for letter in alphabet:
    letterimage = imutils.resize(cv2.imread('letters/letter' + letter + '.png'), width=200, height=200)
    ret,binaryimage = cv2.threshold(letterimage,50,255,cv2.THRESH_BINARY_INV)
    #cv2.imshow("Letter", binarymat)
    histH=[]
    for c in range(200):
        conta=0
        for l in range(200):
            conta+=binaryimage[l,c][2] == 255
        histH.append(conta)
    f = open('histLetters/letter' + letter + '.txt', "a")
    f.write(str(histH))

    alphabet = 'C'
for letter in alphabet:
    letterimage = imutils.resize(cv2.imread('letters/letter' + letter + '.png'), width=200, height=200)
    ret,binaryimage = cv2.threshold(letterimage,50,255,cv2.THRESH_BINARY_INV)
    #cv2.imshow("Letter", binarymat)
    histH=[]
    for c in range(200):
        conta=0
        for l in range(200):
            conta+=binaryimage[l,c][2] == 255
        histH.append(conta)
    f = open('histLetters/letter' + letter + '.txt', "a")
    f.write(str(histH))

alphabet = 'D'
for letter in alphabet:
    letterimage = imutils.resize(cv2.imread('letters/letter' + letter + '.png'), width=200, height=200)
    ret,binaryimage = cv2.threshold(letterimage,50,255,cv2.THRESH_BINARY_INV)
    #cv2.imshow("Letter", binarymat)
    histH=[]
    for c in range(200):
        conta=0
        for l in range(200):
            conta+=binaryimage[l,c][2] == 255
        histH.append(conta)
    f = open('histLetters/letter' + letter + '.txt', "a")
    f.write(str(histH))

    alphabet = 'E'
for letter in alphabet:
    letterimage = imutils.resize(cv2.imread('letters/letter' + letter + '.png'), width=200, height=200)
    ret,binaryimage = cv2.threshold(letterimage,50,255,cv2.THRESH_BINARY_INV)
    #cv2.imshow("Letter", binarymat)
    histH=[]
    for c in range(200):
        conta=0
        for l in range(200):
            conta+=binaryimage[l,c][2] == 255
        histH.append(conta)
    f = open('histLetters/letter' + letter + '.txt', "a")
    f.write(str(histH))

    alphabet = 'F'
for letter in alphabet:
    letterimage = imutils.resize(cv2.imread('letters/letter' + letter + '.png'), width=200, height=200)
    ret,binaryimage = cv2.threshold(letterimage,50,255,cv2.THRESH_BINARY_INV)
    #cv2.imshow("Letter", binarymat)
    histH=[]
    for c in range(200):
        conta=0
        for l in range(200):
            conta+=binaryimage[l,c][2] == 255
        histH.append(conta)
    f = open('histLetters/letter' + letter + '.txt', "a")
    f.write(str(histH))

    alphabet = 'G'
for letter in alphabet:
    letterimage = imutils.resize(cv2.imread('letters/letter' + letter + '.png'), width=200, height=200)
    ret,binaryimage = cv2.threshold(letterimage,50,255,cv2.THRESH_BINARY_INV)
    #cv2.imshow("Letter", binarymat)
    histH=[]
    for c in range(200):
        conta=0
        for l in range(200):
            conta+=binaryimage[l,c][2] == 255
        histH.append(conta)
    f = open('histLetters/letter' + letter + '.txt', "a")
    f.write(str(histH))

    alphabet = 'H'
for letter in alphabet:
    letterimage = imutils.resize(cv2.imread('letters/letter' + letter + '.png'), width=200, height=200)
    ret,binaryimage = cv2.threshold(letterimage,50,255,cv2.THRESH_BINARY_INV)
    #cv2.imshow("Letter", binarymat)
    histH=[]
    for c in range(200):
        conta=0
        for l in range(200):
            conta+=binaryimage[l,c][2] == 255
        histH.append(conta)
    f = open('histLetters/letter' + letter + '.txt', "a")
    f.write(str(histH))

    alphabet = 'I'
for letter in alphabet:
    letterimage = imutils.resize(cv2.imread('letters/letter' + letter + '.png'), width=200, height=200)
    ret,binaryimage = cv2.threshold(letterimage,50,255,cv2.THRESH_BINARY_INV)
    #cv2.imshow("Letter", binarymat)
    histH=[]
    for c in range(200):
        conta=0
        for l in range(200):
            conta+=binaryimage[l,c][2] == 255
        histH.append(conta)
    f = open('histLetters/letter' + letter + '.txt', "a")
    f.write(str(histH))

    alphabet = 'J'
for letter in alphabet:
    letterimage = imutils.resize(cv2.imread('letters/letter' + letter + '.png'), width=200, height=200)
    ret,binaryimage = cv2.threshold(letterimage,50,255,cv2.THRESH_BINARY_INV)
    #cv2.imshow("Letter", binarymat)
    histH=[]
    for c in range(200):
        conta=0
        for l in range(200):
            conta+=binaryimage[l,c][2] == 255
        histH.append(conta)
    f = open('histLetters/letter' + letter + '.txt', "a")
    f.write(str(histH))

    alphabet = 'K'
for letter in alphabet:
    letterimage = imutils.resize(cv2.imread('letters/letter' + letter + '.png'), width=200, height=200)
    ret,binaryimage = cv2.threshold(letterimage,50,255,cv2.THRESH_BINARY_INV)
    #cv2.imshow("Letter", binarymat)
    histH=[]
    for c in range(200):
        conta=0
        for l in range(200):
            conta+=binaryimage[l,c][2] == 255
        histH.append(conta)
    f = open('histLetters/letter' + letter + '.txt', "a")
    f.write(str(histH))

    alphabet = 'L'
for letter in alphabet:
    letterimage = imutils.resize(cv2.imread('letters/letter' + letter + '.png'), width=200, height=200)
    ret,binaryimage = cv2.threshold(letterimage,50,255,cv2.THRESH_BINARY_INV)
    #cv2.imshow("Letter", binarymat)
    histH=[]
    for c in range(200):
        conta=0
        for l in range(200):
            conta+=binaryimage[l,c][2] == 255
        histH.append(conta)
    f = open('histLetters/letter' + letter + '.txt', "a")
    f.write(str(histH))

    alphabet = 'M'
for letter in alphabet:
    letterimage = imutils.resize(cv2.imread('letters/letter' + letter + '.png'), width=200, height=200)
    ret,binaryimage = cv2.threshold(letterimage,50,255,cv2.THRESH_BINARY_INV)
    #cv2.imshow("Letter", binarymat)
    histH=[]
    for c in range(200):
        conta=0
        for l in range(200):
            conta+=binaryimage[l,c][2] == 255
        histH.append(conta)
    f = open('histLetters/letter' + letter + '.txt', "a")
    f.write(str(histH))

    alphabet = 'N'
for letter in alphabet:
    letterimage = imutils.resize(cv2.imread('letters/letter' + letter + '.png'), width=200, height=200)
    ret,binaryimage = cv2.threshold(letterimage,50,255,cv2.THRESH_BINARY_INV)
    #cv2.imshow("Letter", binarymat)
    histH=[]
    for c in range(200):
        conta=0
        for l in range(200):
            conta+=binaryimage[l,c][2] == 255
        histH.append(conta)
    f = open('histLetters/letter' + letter + '.txt', "a")
    f.write(str(histH))

    alphabet = 'O'
for letter in alphabet:
    letterimage = imutils.resize(cv2.imread('letters/letter' + letter + '.png'), width=200, height=200)
    ret,binaryimage = cv2.threshold(letterimage,50,255,cv2.THRESH_BINARY_INV)
    #cv2.imshow("Letter", binarymat)
    histH=[]
    for c in range(200):
        conta=0
        for l in range(200):
            conta+=binaryimage[l,c][2] == 255
        histH.append(conta)
    f = open('histLetters/letter' + letter + '.txt', "a")
    f.write(str(histH))

    alphabet = 'P'
for letter in alphabet:
    letterimage = imutils.resize(cv2.imread('letters/letter' + letter + '.png'), width=200, height=200)
    ret,binaryimage = cv2.threshold(letterimage,50,255,cv2.THRESH_BINARY_INV)
    #cv2.imshow("Letter", binarymat)
    histH=[]
    for c in range(200):
        conta=0
        for l in range(200):
            conta+=binaryimage[l,c][2] == 255
        histH.append(conta)
    f = open('histLetters/letter' + letter + '.txt', "a")
    f.write(str(histH))

    alphabet = 'Q'
for letter in alphabet:
    letterimage = imutils.resize(cv2.imread('letters/letter' + letter + '.png'), width=200, height=200)
    ret,binaryimage = cv2.threshold(letterimage,50,255,cv2.THRESH_BINARY_INV)
    #cv2.imshow("Letter", binarymat)
    histH=[]
    for c in range(200):
        conta=0
        for l in range(200):
            conta+=binaryimage[l,c][2] == 255
        histH.append(conta)
    f = open('histLetters/letter' + letter + '.txt', "a")
    f.write(str(histH))

    alphabet = 'R'
for letter in alphabet:
    letterimage = imutils.resize(cv2.imread('letters/letter' + letter + '.png'), width=200, height=200)
    ret,binaryimage = cv2.threshold(letterimage,50,255,cv2.THRESH_BINARY_INV)
    #cv2.imshow("Letter", binarymat)
    histH=[]
    for c in range(200):
        conta=0
        for l in range(200):
            conta+=binaryimage[l,c][2] == 255
        histH.append(conta)
    f = open('histLetters/letter' + letter + '.txt', "a")
    f.write(str(histH))

    alphabet = 'S'
for letter in alphabet:
    letterimage = imutils.resize(cv2.imread('letters/letter' + letter + '.png'), width=200, height=200)
    ret,binaryimage = cv2.threshold(letterimage,50,255,cv2.THRESH_BINARY_INV)
    #cv2.imshow("Letter", binarymat)
    histH=[]
    for c in range(200):
        conta=0
        for l in range(200):
            conta+=binaryimage[l,c][2] == 255
        histH.append(conta)
    f = open('histLetters/letter' + letter + '.txt', "a")
    f.write(str(histH))

    alphabet = 'T'
for letter in alphabet:
    letterimage = imutils.resize(cv2.imread('letters/letter' + letter + '.png'), width=200, height=200)
    ret,binaryimage = cv2.threshold(letterimage,50,255,cv2.THRESH_BINARY_INV)
    #cv2.imshow("Letter", binarymat)
    histH=[]
    for c in range(200):
        conta=0
        for l in range(200):
            conta+=binaryimage[l,c][2] == 255
        histH.append(conta)
    f = open('histLetters/letter' + letter + '.txt', "a")
    f.write(str(histH))

    alphabet = 'U'
for letter in alphabet:
    letterimage = imutils.resize(cv2.imread('letters/letter' + letter + '.png'), width=200, height=200)
    ret,binaryimage = cv2.threshold(letterimage,50,255,cv2.THRESH_BINARY_INV)
    #cv2.imshow("Letter", binarymat)
    histH=[]
    for c in range(200):
        conta=0
        for l in range(200):
            conta+=binaryimage[l,c][2] == 255
        histH.append(conta)
    f = open('histLetters/letter' + letter + '.txt', "a")
    f.write(str(histH))

    alphabet = 'V'
for letter in alphabet:
    letterimage = imutils.resize(cv2.imread('letters/letter' + letter + '.png'), width=200, height=200)
    ret,binaryimage = cv2.threshold(letterimage,50,255,cv2.THRESH_BINARY_INV)
    #cv2.imshow("Letter", binarymat)
    histH=[]
    for c in range(200):
        conta=0
        for l in range(200):
            conta+=binaryimage[l,c][2] == 255
        histH.append(conta)
    f = open('histLetters/letter' + letter + '.txt', "a")
    f.write(str(histH))

    alphabet = 'W'
for letter in alphabet:
    letterimage = imutils.resize(cv2.imread('letters/letter' + letter + '.png'), width=200, height=200)
    ret,binaryimage = cv2.threshold(letterimage,50,255,cv2.THRESH_BINARY_INV)
    #cv2.imshow("Letter", binarymat)
    histH=[]
    for c in range(200):
        conta=0
        for l in range(200):
            conta+=binaryimage[l,c][2] == 255
        histH.append(conta)
    f = open('histLetters/letter' + letter + '.txt', "a")
    f.write(str(histH))

    alphabet = 'X'
for letter in alphabet:
    letterimage = imutils.resize(cv2.imread('letters/letter' + letter + '.png'), width=200, height=200)
    ret,binaryimage = cv2.threshold(letterimage,50,255,cv2.THRESH_BINARY_INV)
    #cv2.imshow("Letter", binarymat)
    histH=[]
    for c in range(200):
        conta=0
        for l in range(200):
            conta+=binaryimage[l,c][2] == 255
        histH.append(conta)
    f = open('histLetters/letter' + letter + '.txt', "a")
    f.write(str(histH))

    alphabet = 'Y'
for letter in alphabet:
    letterimage = imutils.resize(cv2.imread('letters/letter' + letter + '.png'), width=200, height=200)
    ret,binaryimage = cv2.threshold(letterimage,50,255,cv2.THRESH_BINARY_INV)
    #cv2.imshow("Letter", binarymat)
    histH=[]
    for c in range(200):
        conta=0
        for l in range(200):
            conta+=binaryimage[l,c][2] == 255
        histH.append(conta)
    f = open('histLetters/letter' + letter + '.txt', "a")
    f.write(str(histH))

    alphabet = 'Z'
for letter in alphabet:
    letterimage = imutils.resize(cv2.imread('letters/letter' + letter + '.png'), width=200, height=200)
    ret,binaryimage = cv2.threshold(letterimage,50,255,cv2.THRESH_BINARY_INV)
    #cv2.imshow("Letter", binarymat)
    histH=[]
    for c in range(200):
        conta=0
        for l in range(200):
            conta+=binaryimage[l,c][2] == 255
        histH.append(conta)
    f = open('histLetters/letter' + letter + '.txt', "a")
    f.write(str(histH))