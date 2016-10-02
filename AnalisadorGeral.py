#!/usr/bin/python
# -*- coding: utf-8 -*-

from Data import Data
from Analisador import Analisador


class AnalisadorGeral:

    def __init__(self, resultado):
        self.analisadores = []

        self.dataC = Data('C', 'data/C')
        self.analiseC = Analisador(self.dataC, resultado)
        self.analisadores.append(self.analiseC)

        self.dataL = Data('L', 'data/L')
        self.analiseL = Analisador(self.dataL, resultado)
        self.analisadores.append(self.analiseL)

        self.dataV = Data('V', 'data/V')
        self.analiseV = Analisador(self.dataV, resultado)
        self.analisadores.append(self.analiseV)

        self.dataI = Data('I', 'data/I')
        self.analiseI = Analisador(self.dataI, resultado)
        self.analisadores.append(self.analiseI)

        self.dataA = Data('A', 'data/A')
        self.analiseA = Analisador(self.dataA, resultado, 0.9)
        self.analisadores.append(self.analiseA)

        self.dataIX = Data('IX', 'data/IX')
        self.analiseIX = Analisador(self.dataIX, resultado, gatilho = 'I')
        self.analisadores.append(self.analiseIX)

    def iniciarAnalise(self):
        for analise in self.analisadores:
            analise.start()

    def setFrame(self, frame, configuracaoAnterior):
        for analise in self.analisadores:
            analise.setFrame(frame, configuracaoAnterior)

    def encerrarAnalise(self):
        for analise in self.analisadores:
            analise.encerrarAnalise()


