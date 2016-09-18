#! /usr/bin/python

class Configuracao(object):
    def __init__(self, nome):
        self.nome = nome

    def getNome(self):
        return self.nome

    def addModelo(self, modelo, caminho):
        self.modelos[str(modelo)] = cv2.imread(str(caminho), 0)

    def getModelos(self):
        return modelos.copy()

    def addComposicao(self, configuracao):
        self.composicoes.append(configuracao)

    def getComposicoes(self):
        return self.composicoes
