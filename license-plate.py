import numpy as np
import cv2
import imutils
import re

import pytesseract
import argparse
import os

from matplotlib import pyplot as plt

image = imutils.resize(cv2.imread('LicensePlates/mini.jpg'), width=500)

imageGrayScale = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

#noise-reducing algorithm
imageNoise = cv2.bilateralFilter(imageGrayScale, 9, 75, 75)

#edge detection algorithm
imageEdged = cv2.Canny(imageNoise, 100, 200)

#find rect
(new, ret, principal) = cv2.findContours(imageEdged, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

ret=sorted(ret, key = cv2.contourArea, reverse = True)[:30]

posMatricula = None

for i in ret:
    epsilon = 0.02*cv2.arcLength(i,True)
    approx = cv2.approxPolyDP(i, epsilon, True)
    if len(approx) == 4:
        posMatricula = approx
        break


# Drawing the selected contour on the original image
cv2.drawContours(image, [posMatricula], -1, (255,255,255), 2)
cv2.imshow("License Plate drawn", image)


# getting license plate from drawn countours
xmin = None
xmax = None
ymin = None
ymax = None

for [[x,y]] in posMatricula:
    if xmin > x or xmin == None:
        xmin = x
    elif xmax < x: xmax = x
    if ymin > y or ymin == None:
        ymin = y
    elif ymax < y: ymax = y

mat = image[ymin:ymax, xmin:xmax]
cv2.imshow("License Plate Contours", mat)

matGrayScale = cv2.cvtColor(mat, cv2.COLOR_BGR2GRAY)

#Apply inverse binary threshold
ret,binarymat = cv2.threshold(matGrayScale,50,255,cv2.THRESH_BINARY_INV)
cv2.imshow("binary", binarymat)

#Apply closing morphology expression
kernel = np.ones((3,3),np.uint8)
closing = cv2.morphologyEx(binarymat, cv2.MORPH_CLOSE, kernel)
cv2.imshow("closing", closing)

# calculate histogram of whole image
height, width = closing.shape[:2]
print height
print width
histH=[]
for c in range(width):
    conta=0
    for l in range(height):
        conta+=closing[l,c] == 255
    histH.append(conta)


#calculate characters by analysing the hist above
chars = []
min=0
max=0
for a in histH:
    if a==0 and max>min:
        chars.append(closing[0:height, min:max])
        min = max
    if a>0:
        max+=1
    elif a==0:
        min+=1
        max+=1


# calculate skel chars, number of whites and perimeter
charHs = []
charH = []
charW = []
charP = []
imgSkel = []

for char in chars:
    resized = cv2.resize(char, (200, 400))
    size = np.size(resized)
    skel = np.zeros(resized.shape,np.uint8)

    element = cv2.getStructuringElement(cv2.MORPH_CROSS,(3,3))
    done = False
     
    while( not done):
        eroded = cv2.erode(resized,element)
        temp = cv2.dilate(eroded,element)
        temp = cv2.subtract(resized,temp)
        skel = cv2.bitwise_or(skel,temp)
        resized = eroded.copy()
     
        zeros = size - cv2.countNonZero(resized)
        if zeros==size:
            done = True
    
    _, letraMat = cv2.threshold(skel, 10, 255, cv2.THRESH_BINARY)
    imgSkel.append(letraMat)
    
    for c in range(200):
        conta=0
        for l in range(400):
            conta+=letraMat[l,c] == 255
        charHs.append(conta)
    charH.append(charHs)
    charHs = []

    charW.append(cv2.countNonZero(letraMat))

    #calculating perimeter
    edged = cv2.Canny(letraMat, 0,10)
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
    charP.append(perimeter)


#compare chars with generated characters
characters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
predictedchars=[]

for index, i in enumerate(imgSkel):
    predictedchar=''
    predictedvalue=0
    cv2.imshow("License Plate Letter", imgSkel[index])
    cv2.waitKey(0)
    for c in characters:
        p = open('histcharacters/perimeter' + c + '.txt', "r")
        perimeter = p.read()
        if (float(perimeter)/charP[index]) <= 1 :
            perimeterpercentage = float(perimeter)/charP[index]
        else :
            perimeterpercentage = charP[index]/float(perimeter)


        w = open('histcharacters/nwhites' + c + '.txt', "r")
        whites = w.read()
        if int (whites)/charW[index] <= 1 :
            whites_percentage = int (whites)/charW[index]
        else :
            whites_percentage = charW[index]/int (whites)

        h = open('histcharacters/char' + c + '.txt', "r")
        hist = h.read().split(",");
        inthist = [int(i) for i in hist[:-1]]
        if len(set(inthist)&set(charH[index])) / float(len(set(inthist) | set(charH[index]))) <= 1 :
            histvalue = len(set(inthist)&set(charH[index])) / float(len(set(inthist) | set(charH[index])))
        else :
            histvalue = float(len(set(inthist) | set(charH[index]))) / len(set(inthist)&set(charH[index]))

        currentvalue = histvalue + perimeterpercentage + whites_percentage
        if predictedvalue<currentvalue/3 :
            predictedchar=c
            predictedvalue= currentvalue/3


    if(predictedvalue>0.5) :
        predictedchars.append(predictedchar)



p.close()
w.close()
h.close()
#license regex
license = ''.join(predictedchars)
print license

regex_pt = "([A-B]{2}[A-B]{2}[0-9]{2})|([0-9]{2}[A-B]{2}[A-B]{2})|([A-B]{2}[0-9]{2}[A-B]{2})"
regex_gb = "[A-Z]{2}[0-9]{2}[A-Z]{3}"

if re.match(regex_pt, license) :
    print "PT license: " + license
elif re.match(regex_gb, license) :
    print "GB license: " + license
else :
    print "No license found"


cv2.waitKey(0)

