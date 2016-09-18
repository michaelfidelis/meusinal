#! /usr/bin/python
import cv2
import numpy as np
from threading import Thread

class IData(Thread):
    threshold = 0.75
    image = None
    verify = False
    dataSet = {}

    def __init__(self):
        Thread.__init__(self)
        self.dataSet['I_0'] = cv2.imread('data/I_0.png',0)
        self.dataSet['I_1'] = cv2.imread('data/I_1.png',0)
        self.dataSet['I_10'] = cv2.imread('data/I_10.png',0)
        self.dataSet['I_11'] = cv2.imread('data/I_11.png',0)
        self.dataSet['I_12'] = cv2.imread('data/I_12.png',0)
        self.dataSet['I_13'] = cv2.imread('data/I_13.png',0)
        self.dataSet['I_14'] = cv2.imread('data/I_14.png',0)
        self.dataSet['I_15'] = cv2.imread('data/I_15.png',0)
        self.dataSet['I_16'] = cv2.imread('data/I_16.png',0)
        self.dataSet['I_17'] = cv2.imread('data/I_17.png',0)
        self.dataSet['I_18'] = cv2.imread('data/I_18.png',0)
        self.dataSet['I_19'] = cv2.imread('data/I_19.png',0)
        self.dataSet['I_2'] = cv2.imread('data/I_2.png',0)
        self.dataSet['I_20'] = cv2.imread('data/I_20.png',0)
        self.dataSet['I_21'] = cv2.imread('data/I_21.png',0)
        self.dataSet['I_22'] = cv2.imread('data/I_22.png',0)
        self.dataSet['I_23'] = cv2.imread('data/I_23.png',0)
        self.dataSet['I_24'] = cv2.imread('data/I_24.png',0)
        self.dataSet['I_25'] = cv2.imread('data/I_25.png',0)
        self.dataSet['I_26'] = cv2.imread('data/I_26.png',0)
        self.dataSet['I_27'] = cv2.imread('data/I_27.png',0)
        self.dataSet['I_28'] = cv2.imread('data/I_28.png',0)
        self.dataSet['I_29'] = cv2.imread('data/I_29.png',0)
        self.dataSet['I_3'] = cv2.imread('data/I_3.png',0)
        self.dataSet['I_30'] = cv2.imread('data/I_30.png',0)
        self.dataSet['I_31'] = cv2.imread('data/I_31.png',0)
        self.dataSet['I_32'] = cv2.imread('data/I_32.png',0)
        self.dataSet['I_33'] = cv2.imread('data/I_33.png',0)
        self.dataSet['I_34'] = cv2.imread('data/I_34.png',0)
        self.dataSet['I_35'] = cv2.imread('data/I_35.png',0)
        self.dataSet['I_36'] = cv2.imread('data/I_36.png',0)
        self.dataSet['I_37'] = cv2.imread('data/I_37.png',0)
        self.dataSet['I_38'] = cv2.imread('data/I_38.png',0)
        self.dataSet['I_39'] = cv2.imread('data/I_39.png',0)
        self.dataSet['I_4'] = cv2.imread('data/I_4.png',0)
        self.dataSet['I_40'] = cv2.imread('data/I_40.png',0)
        self.dataSet['I_41'] = cv2.imread('data/I_41.png',0)
        self.dataSet['I_42'] = cv2.imread('data/I_42.png',0)
        self.dataSet['I_43'] = cv2.imread('data/I_43.png',0)
        self.dataSet['I_44'] = cv2.imread('data/I_44.png',0)
        self.dataSet['I_45'] = cv2.imread('data/I_45.png',0)
        self.dataSet['I_46'] = cv2.imread('data/I_46.png',0)
        self.dataSet['I_47'] = cv2.imread('data/I_47.png',0)
        self.dataSet['I_48'] = cv2.imread('data/I_48.png',0)
        self.dataSet['I_49'] = cv2.imread('data/I_49.png',0)
        self.dataSet['I_5'] = cv2.imread('data/I_5.png',0)
        self.dataSet['I_50'] = cv2.imread('data/I_50.png',0)
        self.dataSet['I_51'] = cv2.imread('data/I_51.png',0)
        self.dataSet['I_52'] = cv2.imread('data/I_52.png',0)
        self.dataSet['I_53'] = cv2.imread('data/I_53.png',0)
        self.dataSet['I_54'] = cv2.imread('data/I_54.png',0)
        self.dataSet['I_55'] = cv2.imread('data/I_55.png',0)
        self.dataSet['I_56'] = cv2.imread('data/I_56.png',0)
        self.dataSet['I_57'] = cv2.imread('data/I_57.png',0)
        self.dataSet['I_58'] = cv2.imread('data/I_58.png',0)
        self.dataSet['I_59'] = cv2.imread('data/I_59.png',0)
        self.dataSet['I_6'] = cv2.imread('data/I_6.png',0)
        self.dataSet['I_60'] = cv2.imread('data/I_60.png',0)
        self.dataSet['I_61'] = cv2.imread('data/I_61.png',0)
        self.dataSet['I_62'] = cv2.imread('data/I_62.png',0)
        self.dataSet['I_63'] = cv2.imread('data/I_63.png',0)
        self.dataSet['I_64'] = cv2.imread('data/I_64.png',0)
        self.dataSet['I_65'] = cv2.imread('data/I_65.png',0)
        self.dataSet['I_66'] = cv2.imread('data/I_66.png',0)
        self.dataSet['I_67'] = cv2.imread('data/I_67.png',0)
        self.dataSet['I_68'] = cv2.imread('data/I_68.png',0)
        self.dataSet['I_69'] = cv2.imread('data/I_69.png',0)
        self.dataSet['I_7'] = cv2.imread('data/I_7.png',0)
        self.dataSet['I_70'] = cv2.imread('data/I_70.png',0)
        self.dataSet['I_71'] = cv2.imread('data/I_71.png',0)
        self.dataSet['I_72'] = cv2.imread('data/I_72.png',0)
        self.dataSet['I_73'] = cv2.imread('data/I_73.png',0)
        self.dataSet['I_74'] = cv2.imread('data/I_74.png',0)
        self.dataSet['I_75'] = cv2.imread('data/I_75.png',0)
        self.dataSet['I_76'] = cv2.imread('data/I_76.png',0)
        self.dataSet['I_77'] = cv2.imread('data/I_77.png',0)
        self.dataSet['I_78'] = cv2.imread('data/I_78.png',0)
        self.dataSet['I_79'] = cv2.imread('data/I_79.png',0)
        self.dataSet['I_8'] = cv2.imread('data/I_8.png',0)
        self.dataSet['I_80'] = cv2.imread('data/I_80.png',0)
        self.dataSet['I_81'] = cv2.imread('data/I_81.png',0)
        self.dataSet['I_82'] = cv2.imread('data/I_82.png',0)
        self.dataSet['I_83'] = cv2.imread('data/I_83.png',0)
        self.dataSet['I_84'] = cv2.imread('data/I_84.png',0)
        self.dataSet['I_9'] = cv2.imread('data/I_9.png',0)


    def setImagem(self, image):
        self.verify = True
        self.image = image


    def run(self):
        while True:
            if (self.verify):
                self.match()
                self.verify = False
            else:
                print ""

    def match(self):
        for chave in self.dataSet:
            res = cv2.matchTemplate(self.image, self.dataSet[chave], cv2.TM_CCOEFF_NORMED)
            loc = np.where( res >= self.threshold)
            for pt in zip(*loc[::-1]):
                print "Corresponde com ", chave.split('_', 1)[0]
