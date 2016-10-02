#!/usr/bin/python
# -*- coding: utf-8 -*-

from DataUtils import DataUtils

class Data():

    nome = None
    def __init__(self, nome, diretorio):
        self.diretorio = diretorio
        self.nome = nome

        self.reader = DataUtils()
        self.imagens = self.reader.obterImagens(self.diretorio)

    def getImagens(self):
        return self.imagens;
