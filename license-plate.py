import numpy as np
import cv2
import imutils

import pytesseract
import argparse
import os

from matplotlib import pyplot as plt

image = imutils.resize(cv2.imread('LicensePlates/mini.jpg'), width=500)

#cv2.imshow("Imagem-Original", image)
#cv2.moveWindow('Imagem-Original',0,0)


imageGrayScale = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

#cv2.imshow("Imagem-GrayScale", imageGrayScale)
#cv2.moveWindow('Imagem-GrayScale',0,400)


imageNoise = cv2.bilateralFilter(imageGrayScale, 9, 75, 75)

#cv2.imshow("Imagem Sem Ruido", imageNoise)
#cv2.moveWindow('Imagem Sem Ruido',500,0)


imageEdged = cv2.Canny(imageNoise, 100, 200)

#cv2.imshow("Imagem Contornos", imageEdged)
#cv2.moveWindow('Imagem Contornos',500,400)

#Encontrar retangulos
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
print posMatricula
cv2.imshow("Imagem com matricula", image)


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

ret,binarymat = cv2.threshold(matGrayScale,50,255,cv2.THRESH_BINARY_INV)
cv2.imshow("binary", binarymat)

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


chars = []
npwhites = []
countwhites=0
min=0
max=0
for a in histH:
    if a==0 and max>min:
        chars.append(closing[0:height, min:max])
        npwhites.append(countwhites)
        countwhites=0
        min = max
    if a>0:
        max+=1
        countwhites+=a
    elif a==0:
        min+=1
        max+=1

#print chars
#print min
#print max
#histmat = closing[0:height, min:max]
cv2.imshow("char", chars[1])

perimeterchar = []
for char in chars :
    resized_image = cv2.resize(char, (100, 50))
    #calculating perimeter
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
        perimeter = perimeter+cv2.arcLength(c,True)
        perimeterchar.append(perimeter)


characters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
predictedchars=[]
for index, char in enumerate(chars) :
    predichar=('', 0)
    for c in characters :
        p = open('histcharacters/perimeter' + c + '.txt', "r")
        perimeter = p.read()
        print float(perimeter)/perimeterchar[index]

        w = open('histcharacters/nwhites' + c + '.txt', "r")
        whites = w.read()
        print float(whites)/npwhites[index]

        h = open('histcharacters/char' + c + '.txt', "r")
        hist = h.read().split(",");
        floathist = [int(i) for i in hist[:-1]]
#print len(set(hist)&set(hist[char])) / float(len(set(hist) | set(hist[char]))) * 100


regex_pt = "([A-B]{2}[A-B]{2}[0-9]{2})|([0-9]{2}[A-B]{2}[A-B]{2})|([A-B]{2}[0-9]{2}[A-B]{2})|"
regex_en = "[A-Z]{2}[0-9]{2}[A-Z]{3}"


cv2.waitKey(0)










