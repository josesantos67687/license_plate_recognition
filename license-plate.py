import numpy as np
import cv2
import imutils
import re

import pytesseract
import argparse
import os

from matplotlib import pyplot as plt
#get license image
image = imutils.resize(cv2.imread('LicensePlates/mini.jpg'), width=500)

#gray scale image
imageGrayScale = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

#apply bilateral filter
imageNoise = cv2.bilateralFilter(imageGrayScale, 9, 75, 75)

imageEdged = cv2.Canny(imageNoise, 100, 200)

#find rectangels
(new, ret, principal) = cv2.findContours(imageEdged, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

ret=sorted(ret, key = cv2.contourArea, reverse = True)[:30]

posMatricula = None

for i in ret:
    epsilon = 0.03*cv2.arcLength(i,True)
    approx = cv2.approxPolyDP(i, epsilon, True)
    if len(approx) == 4:
        posMatricula = approx
        break


# Drawing the selected contour on the original image
cv2.drawContours(image, [posMatricula], -1, (255,255,255), 2)
print posMatricula
cv2.imshow("Imagem com matricula", image)


#calculate license dimension
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

matGrayScale = cv2.cvtColor(mat, cv2.COLOR_BGR2GRAY)

#inserve binary thresh
ret,binarymat = cv2.threshold(matGrayScale,80,255,cv2.THRESH_BINARY_INV)
cv2.imshow("binary", binarymat)



#closing
kernel = np.ones((3,3),np.uint8)
closing = cv2.morphologyEx(binarymat, cv2.MORPH_CLOSE, kernel)
cv2.imshow("closing", closing)

height, width = closing.shape[:2]
print height
print width
histH=[]
for c in range(width):
    conta=0
    for l in range(height):
        conta+=closing[l,c] == 255
    histH.append(conta)


#get chars and whites
chars = []
npwhites = []
countwhites=0
min=0
max=0
for a in histH:
    if a<4 and max>min:
        resized = cv2.resize(closing[0:height, min:max], (200, 400))
        chars.append(resized)
        npwhites.append(countwhites)
        countwhites=0
        min = max
    if a>4:
        max+=1
        countwhites+=a
    elif a<4:
        min+=1
        max+=1


#calculating skel of chars
for char in chars :
    size = np.size(binarymat)
    skel = np.zeros(binarymat.shape,np.uint8)

    element = cv2.getStructuringElement(cv2.MORPH_CROSS,(3,3))
    done = False

    while( not done):
        eroded = cv2.erode(binarymat,element)
        temp = cv2.dilate(eroded,element)
        temp = cv2.subtract(binarymat,temp)
        skel = cv2.bitwise_or(skel,temp)
        binarymat = eroded.copy()
        
        zeros = size - cv2.countNonZero(binarymat)
        if zeros==size:
            done = True


#calculating hist of chars
charhist = []
charshist=[]
for char in chars :
    for c in range(200):
        conta=0
        for l in range(400):
            conta+=char[l,c] == 255
        charhist.append(conta)
    charshist.append(charhist)
    charhist = []


#claculate perimeter of chars
perimeterchar = []
for char in chars :
    resized_image = cv2.resize(char, (200, 400))
    #calculating perimeter
    #ret,binaryimage = cv2.threshold(resized_image,50,255,cv2.THRESH_BINARY_INV)
    edged = cv2.Canny(resized_image, 0,10)
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
    perimeterchar.append(perimeter)


#calculations to find license
characters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
predictedchars=[]
predictedvalues=[]
for index, char in enumerate(chars) :
    predictedchar=''
    predictedvalue=0
    for c in characters :
        p = open('histcharacters/perimeter' + c + '.txt', "r")
        perimeter = p.read()
        if (float(perimeter)/perimeterchar[index]) <= 1 :
            perimeterpercentage = float(perimeter)/perimeterchar[index]
        else :
            perimeterpercentage = perimeterchar[index]/float(perimeter)
        
        w = open('histcharacters/nwhites' + c + '.txt', "r")
        whites = w.read()
        #print int(whites)/npwhites[index]

        h = open('histcharacters/char' + c + '.txt', "r")
        hist = h.read().split(",");
        inthist = [int(i) for i in hist[:-1]]
        histvalue = len(set(inthist)&set(charshist[index])) / float(len(set(inthist) | set(charshist[index])))

        currentvalue = histvalue + perimeterpercentage
        if predictedvalue<currentvalue/2 :
            predictedchar=c
            predictedvalue= currentvalue/2

    if(predictedvalue>0.3) :
        predictedchars.append(predictedchar)
        predictedvalues.append(predictedvalue)



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










