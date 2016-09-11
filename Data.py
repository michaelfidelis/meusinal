#! /usr/bin/python
import cv2
import numpy as np

class Data:
    threshold = 0.79
    configuracoes = {}

    configuracoes["MaoAberta_0"] = cv2.imread('data/maoaberta_0.png',0)
    configuracoes["MaoAberta_1"] = cv2.imread('data/maoaberta_1.png',0)
    configuracoes["MaoAberta_2"] = cv2.imread('data/maoaberta_2.png',0)
    configuracoes["MaoAberta_3"] = cv2.imread('data/maoaberta_3.png',0)
    configuracoes["MaoAberta_4"] = cv2.imread('data/maoaberta_4.png',0)
    configuracoes["MaoAberta_5"] = cv2.imread('data/maoaberta_5.png',0)
    configuracoes['A_0'] = cv2.imread('data/A_0.png', 0)
    configuracoes['A_1'] = cv2.imread('data/A_1.png', 0)
    configuracoes['A_2'] = cv2.imread('data/A_2.png', 0)
    configuracoes['A_3'] = cv2.imread('data/A_3.png', 0)
    configuracoes['B_0'] = cv2.imread('data/B_0.png', 0)
    configuracoes['B_1'] = cv2.imread('data/B_1.png', 0)
    configuracoes['B_2'] = cv2.imread('data/B_2.png', 0)
    configuracoes['B_3'] = cv2.imread('data/B_3.png', 0)
    configuracoes['C_0'] = cv2.imread('data/C_0.png', 0)
    configuracoes['C_1'] = cv2.imread('data/C_1.png', 0)
    configuracoes['C_2'] = cv2.imread('data/C_2.png', 0)
    configuracoes['C_3'] = cv2.imread('data/C_3.png', 0)
    configuracoes['C_4'] = cv2.imread('data/C_4.png', 0)
    configuracoes['C_5'] = cv2.imread('data/C_5.png', 0)
    configuracoes['C_6'] = cv2.imread('data/C_6.png', 0)
    configuracoes['C_7'] = cv2.imread('data/C_7.png', 0)
    configuracoes['C_8'] = cv2.imread('data/C_8.png', 0)
    configuracoes['C_9'] = cv2.imread('data/C_9.png', 0)
    configuracoes['D_0'] = cv2.imread('data/D_0.png', 0)
    configuracoes['D_1'] = cv2.imread('data/D_1.png', 0)
    configuracoes['D_2'] = cv2.imread('data/D_2.png', 0)
    configuracoes['D_3'] = cv2.imread('data/D_3.png', 0)
    configuracoes['D_4'] = cv2.imread('data/D_4.png', 0)
    configuracoes['D_5'] = cv2.imread('data/D_5.png', 0)
    configuracoes['D_6'] = cv2.imread('data/D_6.png', 0)
    configuracoes['E_0'] = cv2.imread('data/E_0.png', 0)
    configuracoes['E_1'] = cv2.imread('data/E_1.png', 0)
    configuracoes['E_2'] = cv2.imread('data/E_2.png', 0)
    configuracoes['E_3'] = cv2.imread('data/E_3.png', 0)
    configuracoes['F_0'] = cv2.imread('data/F_0.png', 0)
    configuracoes['F_1'] = cv2.imread('data/F_1.png', 0)
    configuracoes['F_2'] = cv2.imread('data/F_2.png', 0)
    configuracoes['G_0'] = cv2.imread('data/G_0.png', 0)
    configuracoes['G_1'] = cv2.imread('data/G_1.png', 0)
    configuracoes['G_2'] = cv2.imread('data/G_2.png', 0)
    configuracoes['G_3'] = cv2.imread('data/G_3.png', 0)
    configuracoes['H_0'] = cv2.imread('data/H_0.png', 0)
    configuracoes['H_1'] = cv2.imread('data/H_1.png', 0)
    configuracoes['H_2'] = cv2.imread('data/H_2.png', 0)
    configuracoes['H_3'] = cv2.imread('data/H_3.png', 0)
    configuracoes['I_0'] = cv2.imread('data/I_0.png', 0)
    configuracoes['I_1'] = cv2.imread('data/I_1.png', 0)
    configuracoes['I_2'] = cv2.imread('data/I_2.png', 0)
    configuracoes['I_3'] = cv2.imread('data/I_3.png', 0)
    configuracoes['K_0'] = cv2.imread('data/K_0.png', 0)
    configuracoes['K_1'] = cv2.imread('data/K_1.png', 0)
    configuracoes['K_2'] = cv2.imread('data/K_2.png', 0)
    configuracoes['K_3'] = cv2.imread('data/K_3.png', 0)
    configuracoes['K_4'] = cv2.imread('data/K_4.png', 0)
    configuracoes['L_0'] = cv2.imread('data/L_0.png', 0)
    configuracoes['L_1'] = cv2.imread('data/L_1.png', 0)
    configuracoes['L_2'] = cv2.imread('data/L_2.png', 0)
    configuracoes['L_3'] = cv2.imread('data/L_3.png', 0)


    def match(self, image):
        for chave in self.configuracoes:
            configuracao = self.configuracoes[chave]
            res = cv2.matchTemplate(image, configuracao, cv2.TM_CCOEFF_NORMED)
            loc = np.where( res >= self.threshold)
            for pt in zip(*loc[::-1]):
                print "Corresponde com ", chave.split('_', 1)[0]
