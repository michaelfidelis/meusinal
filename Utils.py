#!/usr/bin/python
from collections import deque

class Fila:
    TAMANHO_FILA = 10

    def __init__(self):
        self.letra = None
        self.fila = deque([])

    def adicionar(self, letra):
        if letra is not None and self.letra != letra:
            self.fila.append(letra)
            self.letra = letra
            print 'Adicionando: ' + str(letra)
            if len(self.fila) > self.TAMANHO_FILA:
                #print 'Removendo  : ' + str(self.fila[0])
                self.fila.popleft()

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
