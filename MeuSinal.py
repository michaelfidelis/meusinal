#!/usr/bin/env python
import cv2
import numpy as np
import sys

from CData import CData
from IData import IData
from LData import LData
from VData import VData
from AData import AData

# =====================================================================================================================
# Principal
def main():
    capture = cv2.VideoCapture(0)
    count = 500
    letra = [0];

    cData = CData(letra)
    iData = IData(letra)
    lData = LData(letra)
    vData = VData(letra)
    aData = AData(letra)

    cData.start()
    iData.start()
    lData.start()
    vData.start()
    aData.start()

    while(capture.isOpened()):
        _, image = capture.read()

        crop_image = obterSubImagem(image)

        roi = obterROI(crop_image)
        cv2.imshow('ROI', cv2.flip(roi, 1))

        cData.setImagem(roi)
        iData.setImagem(roi)
        lData.setImagem(roi)
        vData.setImagem(roi)
        aData.setImagem(roi)



        flipped_image = cv2.flip(image, 1)
        cv2.putText(flipped_image, 'Gesto ' + ('' if (letra[0] is None) else letra[0]), (10, 60), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 5, cv2.LINE_AA)
        cv2.imshow('Principal', flipped_image)

        interrupt = cv2.waitKey(10)

        if  interrupt & 0xFF == ord('q'):
            print 'Encerrando execucao...'
            break
        if  interrupt & 0xFF == ord('g'):
            nome = 'gerado/'+ str(letra) + '_' + str(count) + '.png'
            print nome
            cv2.imwrite(str(nome), roi)
            count += 1
        if  interrupt & 0xFF == ord('c'):
            text = raw_input('Digite uma configuracao: ')
            letra = text.upper()
            print 'Configuracao alterada para ' + str(letra)
            count = 500

    cData.join()
    iData.join()
    lData.join()
    vData.join()
    aData.join()
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
    return closing


if __name__ == '__main__':
    main()
