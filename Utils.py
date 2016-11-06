#!/usr/bin/python
# -*- coding: utf-8 -*-

from collections import deque
from Dicionario import Dicionario

import itertools
class Fila:
    TAMANHO_FILA = 5

    def __init__(self):
        self.letra = None
        self.fila = deque([], maxlen=10)
        self.dicio = Dicionario(self.fila)

    def adicionar(self, letra):
        if letra is not None and self.letra != letra:
            self.fila.append(letra)
            self.dicio.verifica()
            self.letra = self.fila[-1]
            print 'Adicionando: ' + str(letra)

    def getUltimoAdicionado(self):
        return self.letra

    def getFila(self):
        return self.fila

    def limparFila(self):
        self.fila.clear()

    def toString(self):
        filaTexto = ' '
        for config in self.fila:
            filaTexto += str(config) + ' '
        return filaTexto
