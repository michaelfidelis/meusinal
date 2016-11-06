#!/usr/bin/python
# -*- coding: utf-8 -*-

from collections import deque
from Dicionario import Dicionario

import itertools
class Fila:

    def __init__(self):
        self.sinal = None
        self.fila = deque([], maxlen=5)
        self.dicionario = Dicionario(self.fila)

    def adicionar(self, sinal):
        if sinal is not None and self.sinal != sinal:
            self.fila.append(sinal)
            self.dicionario.verifica()
            self.sinal = self.fila[-1]
            print 'Adicionando: ' + str(sinal)

    def getUltimoAdicionado(self):
        return self.sinal

    def getFila(self):
        return self.fila

    def limparFila(self):
        self.fila.clear()

    def toString(self):
        filaTexto = ' '
        for config in self.fila:
            filaTexto += str(config) + ' '
        return filaTexto
