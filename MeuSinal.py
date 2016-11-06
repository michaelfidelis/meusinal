#!/usr/bin/python
# -*- coding: utf-8 -*-

import cv2
import numpy as np
from Utils import Fila
import traceback
from Data import Data
from AnalisadorGeral import AnalisadorGeral

# =====================================================================================================================
# Principal
class Principal:
    def __init__(self):
        self.capture = cv2.VideoCapture(0)
        self.configuracao = ['']
        self.fila = Fila()
        self.analisador = AnalisadorGeral(self.configuracao)
        self.analisador.iniciarAnalise()

        while self.capture.isOpened():
            try:
                # Obtem a imagem da camera
                _, image = self.capture.read()

                # Gera uma sub imagem para processamento
                crop_image = self.obterSubImagem(image)

                # Obtem a area de interesse
                roi = self.obterROI(crop_image)

                # Altera o tamanho da imagem melhorar o processamento
                cv2.imshow('ROI', cv2.flip(roi, 1))

                #comContornos = self.obtemContornos(crop_image, roi)
                #cv2.imshow('Com contornos', cv2.flip(comContornos, 1))

                # Informa o frame atual para as threads
                self.analisador.setFrame(roi, self.fila.getUltimoAdicionado())
                # Adiciona a configuracao identificada na fila
                self.fila.adicionar(self.configuracao[0])
                self.configuracao[0] = None
                # Exibe a imagem obtida pela camera
                flipped_image = cv2.flip(image, 1)
                cv2.putText(flipped_image, self.fila.getUltimoAdicionado(), (30, 100), cv2.FONT_HERSHEY_SIMPLEX, 3, (0, 0, 0), 2)
                cv2.putText(flipped_image, self.fila.toString(), (30, 450), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)
                cv2.imshow('Principal', flipped_image)

                interrupt = cv2.waitKey(10)
                if interrupt & 0xFF == ord('q'):
                    print('Encerrando execucao...')
                    break

                if interrupt & 0xFF == ord('c'):
                    print('Limpando fila...')
                    self.fila.limparFila()

            except Exception as inst:
                print('Ocorreu um erro: ')
                print(inst)
                traceback.print_exc()
                break
    # =================================================================================================================
    # Fim do processamento

        # Fecha a camera e as janelas
        self.capture.release()
        cv2.destroyAllWindows()

        # Ao sair do processamento encerra todas as threads
        self.analisador.encerrarAnalise()

    # =================================================================================================================
    # Etapa 0 - Obtem sub imagem
    @staticmethod
    def obterSubImagem(image):
        cv2.rectangle(image, (250, 250), (10, 10), (0, 255, 0), 2)
        return image[10:250, 10:250]

    # =================================================================================================================
    # Etapa 1 - Obtem a area de interesse
    @staticmethod
    def obterROI(image):
        kernel = np.ones((5, 5), np.uint8)
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        blur = cv2.GaussianBlur(gray, (5, 5), 0)
        _, thresh = cv2.threshold(blur, 127, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
        opening = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel)
        closing = cv2.morphologyEx(opening, cv2.MORPH_CLOSE, kernel)
        return closing

    def obtemContornos(self, image, roi):
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
            cx = int(moments['m10']/moments['m00'])
            cy = int(moments['m01']/moments['m00'])
        centr=(cx,cy)

        cv2.circle(drawing,centr,5,[0,0,255],2)
        cv2.drawContours(drawing,[cnt],0,(0,255,0),2)
        cv2.drawContours(drawing,[hull],0,(0,0,255),2)
        #cnt = cv2.approxPolyDP(cnt,0.02*cv2.arcLength(cnt,True),True)
        #hull = cv2.convexHull(cnt,returnPoints = False)

        return drawing

if __name__ == '__main__':
    principal = Principal()
