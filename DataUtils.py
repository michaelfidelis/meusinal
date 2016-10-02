#!/usr/bin/python
# -*- coding: utf-8 -*-

import cv2
import os
# =====================================================================================================================
# Data Utils
class DataUtils:

    def obterImagens(self, diretorio):
        print 'Obtendo imagens do diretorio: {0}'.format(str(diretorio))
        imagens = []
        quantidadeImagens = 0
        for arquivo in os.listdir(diretorio):
            if arquivo.endswith('.png'):
                caminhoArquivo = str(diretorio) + '/'+ str(arquivo)
                imagem = cv2.imread(caminhoArquivo, 0)
                imagens.append(imagem)
                quantidadeImagens += 1
        print 'Obtidas {0} imagens'.format(str(quantidadeImagens))
        return imagens

    def obterDiretorios(self):
        diretorios = []
        all_subdirs = [d for d in os.listdir(self.DIRETORIO)]
        for dirs in all_subdirs:
            dir = os.path.join(self.DIRETORIO, dirs)
            if os.path.isdir(dir):
                diretorios.append(dir)
                print 'Diretorio encontrado: {0}'.format(dir)
        return diretorios
