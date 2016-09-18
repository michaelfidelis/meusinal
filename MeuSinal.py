#!/usr/bin/env python
import cv2
import numpy as np
from IData import IData
from CData import CData

# =====================================================================================================================
# Principal
def main():
    capture = cv2.VideoCapture(0)
    count = 0
    letra = ''

    iData = IData()
    iData.start()

    cData = CData()
    cData.start()


    while(capture.isOpened()):
        _, image = capture.read()

        crop_image = obterSubImagem(image)

        roi = obterROI(crop_image)
        cv2.imshow('ROI', cv2.flip(roi, 1))

        cData.setImagem(roi)
        iData.setImagem(roi)


        #comContornos = obtemContornos(crop_image, roi)
        #cv2.imshow('Com Contornos', cv2.flip(comContornos, 1))

        flipped_image = cv2.flip(image, 1)
        cv2.imshow('capture', flipped_image)

        interrupt = cv2.waitKey(10)
        if  interrupt & 0xFF == ord('q'):
            print "Encerrando execucao..."
            break

        if  interrupt & 0xFF == ord('a'):
            data.verify = True
            data.image = roi

        if  interrupt & 0xFF == ord('g'):
            nome = 'gerado/'+ str(letra) + '_' + str(count) + '.png'
            print nome
            cv2.imwrite(str(nome), roi)
            count += 1
        if  interrupt & 0xFF == ord('c'):
            text = raw_input('Digite uma configuracao: ')
            letra = text.upper()
            print 'Configuracao alterada para ' + str(letra)
            count = 0

    iData.join()
    cData.join()
    capture.release()

    cv2.destroyAllWindows()

# =====================================================================================================================
# Etapa 0 - Obtem sub imagem
def obterSubImagem(image):
    cv2.rectangle(image,(250,250),(10,10),(0,255,0),0)
    return image[10:250, 10:250]

# =====================================================================================================================
# Etapa 1 - Obtem a area de interesse
def obterROI(image):
    kernel = np.ones((5, 5), np.uint8)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray,(5,5),0)
    _,thresh = cv2.threshold(blur,127,255,cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)
    opening = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel)
    closing = cv2.morphologyEx(opening, cv2.MORPH_CLOSE, kernel)

    return closing #cv2.medianBlur(thresh, 5)

# =====================================================================================================================
# Etapa 3 - Obtem contornos
def obtemContornos(image, roi):
    maxArea = 0
    drawing = np.zeros(image.shape, np.uint8)
    _, contours, hierarchy = cv2.findContours(roi.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    for i in range(len(contours)):
            cnt = contours[i]
            area = cv2.contourArea(cnt)
            if(area > maxArea):
                maxArea = area
                ci=i
    cnt = contours[ci]
    hull = cv2.convexHull(cnt)
    moments = cv2.moments(cnt)
    if moments['m00']!=0:
        cx = int(moments['m10']/moments['m00']) # cx = M10/M00
        cy = int(moments['m01']/moments['m00']) # cy = M01/M00
    centr=(cx,cy)

    cv2.circle(drawing,centr,5,[0,0,255],2)
    cv2.drawContours(drawing,[cnt],0,(0,255,0),2)
    cv2.drawContours(drawing,[hull],0,(0,0,255),2)
    cnt = cv2.approxPolyDP(cnt,0.02*cv2.arcLength(cnt,True),True)
    hull = cv2.convexHull(cnt,returnPoints = False)

    if(1):
        defects = cv2.convexityDefects(cnt,hull)
        mind=0
        maxd=0
        if (defects is not None):
            for i in range(defects.shape[0]):
                s,e,f,d = defects[i,0]
                start = tuple(cnt[s][0])
                end = tuple(cnt[e][0])
                far = tuple(cnt[f][0])
                dist = cv2.pointPolygonTest(cnt,centr,True)
                #cv2.circle(drawing, far, 5, [0,0,255], -1)
                cv2.circle(drawing, end, 5, [0,0,255], -1)
                cv2.circle(drawing, start, 5, [0,0,255], -2)

        i=0
    return drawing

if __name__ == '__main__':
    main()
