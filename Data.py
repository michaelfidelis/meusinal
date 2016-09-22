#! /usr/bin/python
import cv2
import numpy as np
from threading import Thread

class Data(Thread):
    threshold = 0.75
    dataSet = {}
    image = None
    verify = False

    def __init__(self, letra):
        Thread.__init__(self)
        self.letra = letra
        self.analiseAtiva = True

    def setImagem(self, image):
        self.verify = True
        self.image = image


    def encerrarAnalise(self):
        self.analiseAtiva = False
        self.join()

    def run(self):
        while (self.analiseAtiva):
            if (self.verify):
                self.verify = False
                self.letra[0] = self.match()
            else:
                self.letra[0] = None

    def match(self):
        for chave in self.dataSet:
            res = cv2.matchTemplate(self.image, self.dataSet[chave], cv2.TM_CCOEFF_NORMED)
            loc = np.where( res >= self.threshold)
            for pt in zip(*loc[::-1]):
                return chave.split('_', 1)[0]