#!/usr/bin/python
# -*- coding: utf-8 -*-

from DataUtils import DataUtils

class Data():

    nome = None
    def __init__(self, nome, diretorio, nomeExibir = None):
        self.diretorio = diretorio
        self.nome = nome

        if nomeExibir is None:
            self.nomeExibir = nome
        else:
            self.nomeExibir = nomeExibir

        self.reader = DataUtils()
        self.imagens = self.reader.obterImagens(self.diretorio)

    def getImagens(self):
        return self.imagens;
