#!/usr/bin/env python
import cv2
import numpy as np
import sys
from Utils import Fila

from CData import CData
from IData import IData
from LData import LData
from VData import VData
from AData import AData

# =====================================================================================================================
# Principal
class Principal:
    def __init__(self):
        self.capture = cv2.VideoCapture(0)
        self.configuracao = [0];
        self.fila = Fila()

        self.cData = CData(self.configuracao)
        self.iData = IData(self.configuracao)
        self.lData = LData(self.configuracao)
        self.vData = VData(self.configuracao)
        self.aData = AData(self.configuracao)

        self.cData.start()
        self.iData.start()
        self.lData.start()
        self.vData.start()
        self.aData.start()

        while(self.capture.isOpened()):
            try:
                # Obtem a imagem da camera
                _, image = self.capture.read()

                # Gera uma sub imagem para processamento
                crop_image = self.obterSubImagem(image)

                # Obtem a area de interesse
                roi = self.obterROI(crop_image)

                # Altera o tamanho da imagem melhorar o processamento
                resizedROI = cv2.resize(roi, (120, 120))
                cv2.imshow('ROI', cv2.flip(resizedROI, 1))

                # Informa o frame atual para as threads
                self.cData.setImagem(resizedROI)
                self.iData.setImagem(resizedROI)
                self.lData.setImagem(resizedROI)
                self.vData.setImagem(resizedROI)
                self.aData.setImagem(resizedROI)

                # Adiciona a configuracao identificada na fila
                self.fila.adicionar(self.configuracao[0])

                # Exibe a imagem obtida pela camera
                flipped_image = cv2.flip(image, 1)
                cv2.putText(flipped_image, self.fila.getUltimoAdicionado(), (30, 100), cv2.FONT_HERSHEY_SIMPLEX, 3, (0, 0, 0), 2)
                cv2.imshow('Principal', flipped_image)

                interrupt = cv2.waitKey(10)
                if  interrupt & 0xFF == ord('q'):
                    print('Encerrando execucao...')
                    break

            except Exception as inst:
                print(inst)
                print('Encerrando execucao.')
                break
    # =================================================================================================================
    # Fim do processamento

        # Fecha a camera e as janelas
        self.capture.release()
        cv2.destroyAllWindows()

        # Ao sair do processamento encerra todas as threads
        self.cData.encerrarAnalise()
        self.iData.encerrarAnalise()
        self.lData.encerrarAnalise()
        self.vData.encerrarAnalise()
        self.aData.encerrarAnalise()

    # =================================================================================================================
    # Etapa 0 - Obtem sub imagem
    def obterSubImagem(self, image):
        cv2.rectangle(image,(250,250),(10,10),(0,255,0),2)
        return image[10:250, 10:250]

    # =================================================================================================================
    # Etapa 1 - Obtem a area de interesse
    def obterROI(self, image):
        kernel = np.ones((5, 5), np.uint8)
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        blur = cv2.GaussianBlur(gray,(5,5),0)
        _,thresh = cv2.threshold(blur,127,255,cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)
        opening = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel)
        closing = cv2.morphologyEx(opening, cv2.MORPH_CLOSE, kernel)
        return closing

if __name__ == '__main__':
    principal = Principal()
