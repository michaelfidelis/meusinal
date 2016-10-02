#!/usr/bin/python
# -*- coding: utf-8 -*-

import itertools

class Dicionario:

    def __init__(self, fila):
        self.dicionario = {}
        self.fila = fila
        self.dicionario['J'] = ['I', 'IX']

    def verifica(self):
        for chave, valor in self.dicionario.iteritems():
            if (len(self.fila) >= len(valor)):
                sequencia = list(itertools.islice(self.fila, len(self.fila) - len(valor), len(self.fila)))
                if (sequencia == valor):
                    for x in range(0, len(valor)):
                        self.fila.pop()
                    self.fila.append(chave)

