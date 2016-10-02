#!/usr/bin/python
import cv2
import numpy as np
from threading import Thread


class Analisador(Thread):

    def __init__(self, data, resultado, criterio = 0.8):
        Thread.__init__(self)
        self.resultado = resultado
        self.threadAtiva = True
        self.analiseAtiva = False
        self.data = data
        self.imagem = None
        self.criterio = criterio

    def setFrame(self, imagem):
        self.analiseAtiva = True
        self.imagem = imagem

    def encerrarAnalise(self):
        self.threadAtiva = False
        self.join()
        print "Parando analise de {0}".format(self.data.nome)

    def run(self):
        print "Iniciando analise de {0}".format(self.data.nome)

        while self.threadAtiva:
            #print "Analisando {0}".format(self.data.nome)
            if self.analiseAtiva:
                self.analiseAtiva = False
                resultado = self.match()
                if (resultado):
                    self.resultado[0] = resultado

    def match(self):
        for imagem in self.data.getImagens():
            res = cv2.matchTemplate(self.imagem, imagem, cv2.TM_CCOEFF_NORMED)
            loc = np.where(res >= self.criterio)
            if (len(zip(*loc[::-1])) > 0):
                return self.data.nome
