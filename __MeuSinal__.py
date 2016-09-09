#!/usr/bin/env python
import cv2
import numpy as np

def main():
    cap = cv2.VideoCapture(0)

    while(cap.isOpened()):
        _, image = cap.read()

        cv2.rectangle(image,(250,250),(10,10),(0,255,0),0)
        crop_image = image[10:250, 10:250]

        contornos = obterContornos(crop_image)
        cv2.imshow('Contornos', contornos)

        flipped_image = cv2.flip(image, 1)
        cv2.imshow('capture', flipped_image)
        k = cv2.waitKey(10)
        if k == 27:
            break

# Etapa 1 - Obtem a area de interesse
def obterROI(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray,(5,5),0)
    _,thresh = cv2.threshold(blur,70,255,cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)
    return thresh


# Etapa 2 - Obtem contornos da imagem de interesse
def obterContornos(image):
    roi = obterROI(image.copy())
    _, contours, hierarchy = cv2.findContours(roi, cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    drawing = np.zeros(image.shape, np.uint8)

    max_area=0

    for i in range(len(contours)):
            cnt = contours[i]
            area = cv2.contourArea(cnt)
            if(area>max_area):
                max_area=area
                ci=i
    cnt=contours[ci]
    hull = cv2.convexHull(cnt)
    moments = cv2.moments(cnt)
    if moments['m00']!=0:
                cx = int(moments['m10']/moments['m00']) # cx = M10/M00
                cy = int(moments['m01']/moments['m00']) # cy = M01/M00

    centr=(cx,cy)
    cv2.circle(drawing,centr,5,[0,0,255],2)
    cv2.drawContours(drawing,[cnt],0,(0,255,0),2)
    cv2.drawContours(drawing,[hull],0,(0,0,255),2)

    cnt = cv2.approxPolyDP(cnt,0.01*cv2.arcLength(cnt,True),True)
    hull = cv2.convexHull(cnt,returnPoints = False)

    if(1):
        defects = cv2.convexityDefects(cnt,hull)
        mind=0
        maxd=0
        for i in range(defects.shape[0]):
            s,e,f,d = defects[i,0]
            start = tuple(cnt[s][0])
            end = tuple(cnt[e][0])
            far = tuple(cnt[f][0])
            dist = cv2.pointPolygonTest(cnt,centr,True)
            #cv2.line(drawing,start,end,[0,255,0],2)

            cv2.circle(drawing, end,4,[255,255,255], 2)
            #cv2.circle(drawing, start, 4, [255, 255, 255], 2)
            cv2.circle(drawing, far, 4, [255, 0, 255], 2)
        i=0

    return drawing

if __name__ == '__main__':
    main()
