#! /usr/bin/python
import cv2
import numpy as np
from Data import Data
from threading import Thread

class CData(Data):

    def __init__(self, letra):
        Data.__init__(self, letra)
        self.dataSet['C_0'] = cv2.imread('data/C_0.png',0)
        self.dataSet['C_1'] = cv2.imread('data/C_1.png',0)
        self.dataSet['C_10'] = cv2.imread('data/C_10.png',0)
        self.dataSet['C_100'] = cv2.imread('data/C_100.png',0)
        self.dataSet['C_101'] = cv2.imread('data/C_101.png',0)
        self.dataSet['C_102'] = cv2.imread('data/C_102.png',0)
        self.dataSet['C_103'] = cv2.imread('data/C_103.png',0)
        self.dataSet['C_104'] = cv2.imread('data/C_104.png',0)
        self.dataSet['C_105'] = cv2.imread('data/C_105.png',0)
        self.dataSet['C_106'] = cv2.imread('data/C_106.png',0)
        self.dataSet['C_107'] = cv2.imread('data/C_107.png',0)
        self.dataSet['C_108'] = cv2.imread('data/C_108.png',0)
        self.dataSet['C_109'] = cv2.imread('data/C_109.png',0)
        self.dataSet['C_11'] = cv2.imread('data/C_11.png',0)
        self.dataSet['C_110'] = cv2.imread('data/C_110.png',0)
        self.dataSet['C_111'] = cv2.imread('data/C_111.png',0)
        self.dataSet['C_112'] = cv2.imread('data/C_112.png',0)
        self.dataSet['C_113'] = cv2.imread('data/C_113.png',0)
        self.dataSet['C_114'] = cv2.imread('data/C_114.png',0)
        self.dataSet['C_115'] = cv2.imread('data/C_115.png',0)
        self.dataSet['C_116'] = cv2.imread('data/C_116.png',0)
        self.dataSet['C_117'] = cv2.imread('data/C_117.png',0)
        self.dataSet['C_118'] = cv2.imread('data/C_118.png',0)
        self.dataSet['C_119'] = cv2.imread('data/C_119.png',0)
        self.dataSet['C_12'] = cv2.imread('data/C_12.png',0)
        self.dataSet['C_120'] = cv2.imread('data/C_120.png',0)
        self.dataSet['C_121'] = cv2.imread('data/C_121.png',0)
        self.dataSet['C_122'] = cv2.imread('data/C_122.png',0)
        self.dataSet['C_123'] = cv2.imread('data/C_123.png',0)
        self.dataSet['C_124'] = cv2.imread('data/C_124.png',0)
        self.dataSet['C_125'] = cv2.imread('data/C_125.png',0)
        self.dataSet['C_126'] = cv2.imread('data/C_126.png',0)
        self.dataSet['C_127'] = cv2.imread('data/C_127.png',0)
        self.dataSet['C_128'] = cv2.imread('data/C_128.png',0)
        self.dataSet['C_129'] = cv2.imread('data/C_129.png',0)
        self.dataSet['C_13'] = cv2.imread('data/C_13.png',0)
        self.dataSet['C_130'] = cv2.imread('data/C_130.png',0)
        self.dataSet['C_131'] = cv2.imread('data/C_131.png',0)
        self.dataSet['C_132'] = cv2.imread('data/C_132.png',0)
        self.dataSet['C_133'] = cv2.imread('data/C_133.png',0)
        self.dataSet['C_134'] = cv2.imread('data/C_134.png',0)
        self.dataSet['C_135'] = cv2.imread('data/C_135.png',0)
        self.dataSet['C_136'] = cv2.imread('data/C_136.png',0)
        self.dataSet['C_137'] = cv2.imread('data/C_137.png',0)
        self.dataSet['C_138'] = cv2.imread('data/C_138.png',0)
        self.dataSet['C_139'] = cv2.imread('data/C_139.png',0)
        self.dataSet['C_14'] = cv2.imread('data/C_14.png',0)
        self.dataSet['C_140'] = cv2.imread('data/C_140.png',0)
        self.dataSet['C_141'] = cv2.imread('data/C_141.png',0)
        self.dataSet['C_142'] = cv2.imread('data/C_142.png',0)
        self.dataSet['C_143'] = cv2.imread('data/C_143.png',0)
        self.dataSet['C_144'] = cv2.imread('data/C_144.png',0)
        self.dataSet['C_145'] = cv2.imread('data/C_145.png',0)
        self.dataSet['C_146'] = cv2.imread('data/C_146.png',0)
        self.dataSet['C_147'] = cv2.imread('data/C_147.png',0)
        self.dataSet['C_148'] = cv2.imread('data/C_148.png',0)
        self.dataSet['C_149'] = cv2.imread('data/C_149.png',0)
        self.dataSet['C_15'] = cv2.imread('data/C_15.png',0)
        self.dataSet['C_150'] = cv2.imread('data/C_150.png',0)
        self.dataSet['C_151'] = cv2.imread('data/C_151.png',0)
        self.dataSet['C_152'] = cv2.imread('data/C_152.png',0)
        self.dataSet['C_153'] = cv2.imread('data/C_153.png',0)
        self.dataSet['C_154'] = cv2.imread('data/C_154.png',0)
        self.dataSet['C_155'] = cv2.imread('data/C_155.png',0)
        self.dataSet['C_156'] = cv2.imread('data/C_156.png',0)
        self.dataSet['C_157'] = cv2.imread('data/C_157.png',0)
        self.dataSet['C_158'] = cv2.imread('data/C_158.png',0)
        self.dataSet['C_159'] = cv2.imread('data/C_159.png',0)
        self.dataSet['C_16'] = cv2.imread('data/C_16.png',0)
        self.dataSet['C_160'] = cv2.imread('data/C_160.png',0)
        self.dataSet['C_161'] = cv2.imread('data/C_161.png',0)
        self.dataSet['C_162'] = cv2.imread('data/C_162.png',0)
        self.dataSet['C_163'] = cv2.imread('data/C_163.png',0)
        self.dataSet['C_164'] = cv2.imread('data/C_164.png',0)
        self.dataSet['C_17'] = cv2.imread('data/C_17.png',0)
        self.dataSet['C_18'] = cv2.imread('data/C_18.png',0)
        self.dataSet['C_19'] = cv2.imread('data/C_19.png',0)
        self.dataSet['C_2'] = cv2.imread('data/C_2.png',0)
        self.dataSet['C_20'] = cv2.imread('data/C_20.png',0)
        self.dataSet['C_21'] = cv2.imread('data/C_21.png',0)
        self.dataSet['C_22'] = cv2.imread('data/C_22.png',0)
        self.dataSet['C_23'] = cv2.imread('data/C_23.png',0)
        self.dataSet['C_24'] = cv2.imread('data/C_24.png',0)
        self.dataSet['C_25'] = cv2.imread('data/C_25.png',0)
        self.dataSet['C_26'] = cv2.imread('data/C_26.png',0)
        self.dataSet['C_27'] = cv2.imread('data/C_27.png',0)
        self.dataSet['C_28'] = cv2.imread('data/C_28.png',0)
        self.dataSet['C_29'] = cv2.imread('data/C_29.png',0)
        self.dataSet['C_3'] = cv2.imread('data/C_3.png',0)
        self.dataSet['C_30'] = cv2.imread('data/C_30.png',0)
        self.dataSet['C_31'] = cv2.imread('data/C_31.png',0)
        self.dataSet['C_32'] = cv2.imread('data/C_32.png',0)
        self.dataSet['C_33'] = cv2.imread('data/C_33.png',0)
        self.dataSet['C_34'] = cv2.imread('data/C_34.png',0)
        self.dataSet['C_35'] = cv2.imread('data/C_35.png',0)
        self.dataSet['C_36'] = cv2.imread('data/C_36.png',0)
        self.dataSet['C_37'] = cv2.imread('data/C_37.png',0)
        self.dataSet['C_38'] = cv2.imread('data/C_38.png',0)
        self.dataSet['C_39'] = cv2.imread('data/C_39.png',0)
        self.dataSet['C_4'] = cv2.imread('data/C_4.png',0)
        self.dataSet['C_40'] = cv2.imread('data/C_40.png',0)
        self.dataSet['C_41'] = cv2.imread('data/C_41.png',0)
        self.dataSet['C_42'] = cv2.imread('data/C_42.png',0)
        self.dataSet['C_43'] = cv2.imread('data/C_43.png',0)
        self.dataSet['C_44'] = cv2.imread('data/C_44.png',0)
        self.dataSet['C_45'] = cv2.imread('data/C_45.png',0)
        self.dataSet['C_46'] = cv2.imread('data/C_46.png',0)
        self.dataSet['C_47'] = cv2.imread('data/C_47.png',0)
        self.dataSet['C_48'] = cv2.imread('data/C_48.png',0)
        self.dataSet['C_49'] = cv2.imread('data/C_49.png',0)
        self.dataSet['C_5'] = cv2.imread('data/C_5.png',0)
        self.dataSet['C_50'] = cv2.imread('data/C_50.png',0)
        self.dataSet['C_51'] = cv2.imread('data/C_51.png',0)
        self.dataSet['C_52'] = cv2.imread('data/C_52.png',0)
        self.dataSet['C_53'] = cv2.imread('data/C_53.png',0)
        self.dataSet['C_54'] = cv2.imread('data/C_54.png',0)
        self.dataSet['C_55'] = cv2.imread('data/C_55.png',0)
        self.dataSet['C_56'] = cv2.imread('data/C_56.png',0)
        self.dataSet['C_57'] = cv2.imread('data/C_57.png',0)
        self.dataSet['C_58'] = cv2.imread('data/C_58.png',0)
        self.dataSet['C_59'] = cv2.imread('data/C_59.png',0)
        self.dataSet['C_6'] = cv2.imread('data/C_6.png',0)
        self.dataSet['C_60'] = cv2.imread('data/C_60.png',0)
        self.dataSet['C_61'] = cv2.imread('data/C_61.png',0)
        self.dataSet['C_62'] = cv2.imread('data/C_62.png',0)
        self.dataSet['C_63'] = cv2.imread('data/C_63.png',0)
        self.dataSet['C_64'] = cv2.imread('data/C_64.png',0)
        self.dataSet['C_65'] = cv2.imread('data/C_65.png',0)
        self.dataSet['C_66'] = cv2.imread('data/C_66.png',0)
        self.dataSet['C_67'] = cv2.imread('data/C_67.png',0)
        self.dataSet['C_68'] = cv2.imread('data/C_68.png',0)
        self.dataSet['C_69'] = cv2.imread('data/C_69.png',0)
        self.dataSet['C_7'] = cv2.imread('data/C_7.png',0)
        self.dataSet['C_70'] = cv2.imread('data/C_70.png',0)
        self.dataSet['C_71'] = cv2.imread('data/C_71.png',0)
        self.dataSet['C_72'] = cv2.imread('data/C_72.png',0)
        self.dataSet['C_73'] = cv2.imread('data/C_73.png',0)
        self.dataSet['C_74'] = cv2.imread('data/C_74.png',0)
        self.dataSet['C_75'] = cv2.imread('data/C_75.png',0)
        self.dataSet['C_76'] = cv2.imread('data/C_76.png',0)
        self.dataSet['C_77'] = cv2.imread('data/C_77.png',0)
        self.dataSet['C_78'] = cv2.imread('data/C_78.png',0)
        self.dataSet['C_79'] = cv2.imread('data/C_79.png',0)
        self.dataSet['C_8'] = cv2.imread('data/C_8.png',0)
        self.dataSet['C_80'] = cv2.imread('data/C_80.png',0)
        self.dataSet['C_81'] = cv2.imread('data/C_81.png',0)
        self.dataSet['C_82'] = cv2.imread('data/C_82.png',0)
        self.dataSet['C_83'] = cv2.imread('data/C_83.png',0)
        self.dataSet['C_84'] = cv2.imread('data/C_84.png',0)
        self.dataSet['C_85'] = cv2.imread('data/C_85.png',0)
        self.dataSet['C_86'] = cv2.imread('data/C_86.png',0)
        self.dataSet['C_87'] = cv2.imread('data/C_87.png',0)
        self.dataSet['C_88'] = cv2.imread('data/C_88.png',0)
        self.dataSet['C_89'] = cv2.imread('data/C_89.png',0)
        self.dataSet['C_9'] = cv2.imread('data/C_9.png',0)
        self.dataSet['C_90'] = cv2.imread('data/C_90.png',0)
        self.dataSet['C_91'] = cv2.imread('data/C_91.png',0)
        self.dataSet['C_92'] = cv2.imread('data/C_92.png',0)
        self.dataSet['C_93'] = cv2.imread('data/C_93.png',0)
        self.dataSet['C_94'] = cv2.imread('data/C_94.png',0)
        self.dataSet['C_95'] = cv2.imread('data/C_95.png',0)
        self.dataSet['C_96'] = cv2.imread('data/C_96.png',0)
        self.dataSet['C_97'] = cv2.imread('data/C_97.png',0)
        self.dataSet['C_98'] = cv2.imread('data/C_98.png',0)
        self.dataSet['C_99'] = cv2.imread('data/C_99.png',0)


