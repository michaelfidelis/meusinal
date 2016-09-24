#! /usr/bin/python
import cv2

from Data import Data


class LData(Data):
    def __init__(self, letra):
        Data.__init__(self, letra)
        self.dataSet['L_0'] = cv2.imread('data/L_0.png', 0)
        self.dataSet['L_1'] = cv2.imread('data/L_1.png', 0)
        self.dataSet['L_10'] = cv2.imread('data/L_10.png', 0)
        self.dataSet['L_100'] = cv2.imread('data/L_100.png', 0)
        self.dataSet['L_101'] = cv2.imread('data/L_101.png', 0)
        self.dataSet['L_102'] = cv2.imread('data/L_102.png', 0)
        self.dataSet['L_103'] = cv2.imread('data/L_103.png', 0)
        self.dataSet['L_104'] = cv2.imread('data/L_104.png', 0)
        self.dataSet['L_105'] = cv2.imread('data/L_105.png', 0)
        self.dataSet['L_106'] = cv2.imread('data/L_106.png', 0)
        self.dataSet['L_107'] = cv2.imread('data/L_107.png', 0)
        self.dataSet['L_108'] = cv2.imread('data/L_108.png', 0)
        self.dataSet['L_109'] = cv2.imread('data/L_109.png', 0)
        self.dataSet['L_11'] = cv2.imread('data/L_11.png', 0)
        self.dataSet['L_110'] = cv2.imread('data/L_110.png', 0)
        self.dataSet['L_111'] = cv2.imread('data/L_111.png', 0)
        self.dataSet['L_112'] = cv2.imread('data/L_112.png', 0)
        self.dataSet['L_113'] = cv2.imread('data/L_113.png', 0)
        self.dataSet['L_114'] = cv2.imread('data/L_114.png', 0)
        self.dataSet['L_115'] = cv2.imread('data/L_115.png', 0)
        self.dataSet['L_116'] = cv2.imread('data/L_116.png', 0)
        self.dataSet['L_117'] = cv2.imread('data/L_117.png', 0)
        self.dataSet['L_118'] = cv2.imread('data/L_118.png', 0)
        self.dataSet['L_119'] = cv2.imread('data/L_119.png', 0)
        self.dataSet['L_12'] = cv2.imread('data/L_12.png', 0)
        self.dataSet['L_120'] = cv2.imread('data/L_120.png', 0)
        self.dataSet['L_121'] = cv2.imread('data/L_121.png', 0)
        self.dataSet['L_122'] = cv2.imread('data/L_122.png', 0)
        self.dataSet['L_123'] = cv2.imread('data/L_123.png', 0)
        self.dataSet['L_124'] = cv2.imread('data/L_124.png', 0)
        self.dataSet['L_125'] = cv2.imread('data/L_125.png', 0)
        self.dataSet['L_126'] = cv2.imread('data/L_126.png', 0)
        self.dataSet['L_127'] = cv2.imread('data/L_127.png', 0)
        self.dataSet['L_128'] = cv2.imread('data/L_128.png', 0)
        self.dataSet['L_129'] = cv2.imread('data/L_129.png', 0)
        self.dataSet['L_13'] = cv2.imread('data/L_13.png', 0)
        self.dataSet['L_130'] = cv2.imread('data/L_130.png', 0)
        self.dataSet['L_131'] = cv2.imread('data/L_131.png', 0)
        self.dataSet['L_132'] = cv2.imread('data/L_132.png', 0)
        self.dataSet['L_133'] = cv2.imread('data/L_133.png', 0)
        self.dataSet['L_134'] = cv2.imread('data/L_134.png', 0)
        self.dataSet['L_135'] = cv2.imread('data/L_135.png', 0)
        self.dataSet['L_136'] = cv2.imread('data/L_136.png', 0)
        self.dataSet['L_137'] = cv2.imread('data/L_137.png', 0)
        self.dataSet['L_138'] = cv2.imread('data/L_138.png', 0)
        self.dataSet['L_139'] = cv2.imread('data/L_139.png', 0)
        self.dataSet['L_14'] = cv2.imread('data/L_14.png', 0)
        self.dataSet['L_140'] = cv2.imread('data/L_140.png', 0)
        self.dataSet['L_141'] = cv2.imread('data/L_141.png', 0)
        self.dataSet['L_142'] = cv2.imread('data/L_142.png', 0)
        self.dataSet['L_143'] = cv2.imread('data/L_143.png', 0)
        self.dataSet['L_144'] = cv2.imread('data/L_144.png', 0)
        self.dataSet['L_145'] = cv2.imread('data/L_145.png', 0)
        self.dataSet['L_146'] = cv2.imread('data/L_146.png', 0)
        self.dataSet['L_147'] = cv2.imread('data/L_147.png', 0)
        self.dataSet['L_148'] = cv2.imread('data/L_148.png', 0)
        self.dataSet['L_149'] = cv2.imread('data/L_149.png', 0)
        self.dataSet['L_15'] = cv2.imread('data/L_15.png', 0)
        self.dataSet['L_150'] = cv2.imread('data/L_150.png', 0)
        self.dataSet['L_151'] = cv2.imread('data/L_151.png', 0)
        self.dataSet['L_152'] = cv2.imread('data/L_152.png', 0)
        self.dataSet['L_153'] = cv2.imread('data/L_153.png', 0)
        self.dataSet['L_154'] = cv2.imread('data/L_154.png', 0)
        self.dataSet['L_155'] = cv2.imread('data/L_155.png', 0)
        self.dataSet['L_156'] = cv2.imread('data/L_156.png', 0)
        self.dataSet['L_157'] = cv2.imread('data/L_157.png', 0)
        self.dataSet['L_158'] = cv2.imread('data/L_158.png', 0)
        self.dataSet['L_159'] = cv2.imread('data/L_159.png', 0)
        self.dataSet['L_16'] = cv2.imread('data/L_16.png', 0)
        self.dataSet['L_160'] = cv2.imread('data/L_160.png', 0)
        self.dataSet['L_161'] = cv2.imread('data/L_161.png', 0)
        self.dataSet['L_162'] = cv2.imread('data/L_162.png', 0)
        self.dataSet['L_163'] = cv2.imread('data/L_163.png', 0)
        self.dataSet['L_164'] = cv2.imread('data/L_164.png', 0)
        self.dataSet['L_165'] = cv2.imread('data/L_165.png', 0)
        self.dataSet['L_166'] = cv2.imread('data/L_166.png', 0)
        self.dataSet['L_167'] = cv2.imread('data/L_167.png', 0)
        self.dataSet['L_168'] = cv2.imread('data/L_168.png', 0)
        self.dataSet['L_169'] = cv2.imread('data/L_169.png', 0)
        self.dataSet['L_17'] = cv2.imread('data/L_17.png', 0)
        self.dataSet['L_170'] = cv2.imread('data/L_170.png', 0)
        self.dataSet['L_171'] = cv2.imread('data/L_171.png', 0)
        self.dataSet['L_172'] = cv2.imread('data/L_172.png', 0)
        self.dataSet['L_173'] = cv2.imread('data/L_173.png', 0)
        self.dataSet['L_174'] = cv2.imread('data/L_174.png', 0)
        self.dataSet['L_175'] = cv2.imread('data/L_175.png', 0)
        self.dataSet['L_176'] = cv2.imread('data/L_176.png', 0)
        self.dataSet['L_177'] = cv2.imread('data/L_177.png', 0)
        self.dataSet['L_178'] = cv2.imread('data/L_178.png', 0)
        self.dataSet['L_179'] = cv2.imread('data/L_179.png', 0)
        self.dataSet['L_18'] = cv2.imread('data/L_18.png', 0)
        self.dataSet['L_180'] = cv2.imread('data/L_180.png', 0)
        self.dataSet['L_181'] = cv2.imread('data/L_181.png', 0)
        self.dataSet['L_182'] = cv2.imread('data/L_182.png', 0)
        self.dataSet['L_183'] = cv2.imread('data/L_183.png', 0)
        self.dataSet['L_184'] = cv2.imread('data/L_184.png', 0)
        self.dataSet['L_185'] = cv2.imread('data/L_185.png', 0)
        self.dataSet['L_186'] = cv2.imread('data/L_186.png', 0)
        self.dataSet['L_187'] = cv2.imread('data/L_187.png', 0)
        self.dataSet['L_188'] = cv2.imread('data/L_188.png', 0)
        self.dataSet['L_189'] = cv2.imread('data/L_189.png', 0)
        self.dataSet['L_19'] = cv2.imread('data/L_19.png', 0)
        self.dataSet['L_190'] = cv2.imread('data/L_190.png', 0)
        self.dataSet['L_191'] = cv2.imread('data/L_191.png', 0)
        self.dataSet['L_192'] = cv2.imread('data/L_192.png', 0)
        self.dataSet['L_193'] = cv2.imread('data/L_193.png', 0)
        self.dataSet['L_194'] = cv2.imread('data/L_194.png', 0)
        self.dataSet['L_195'] = cv2.imread('data/L_195.png', 0)
        self.dataSet['L_196'] = cv2.imread('data/L_196.png', 0)
        self.dataSet['L_197'] = cv2.imread('data/L_197.png', 0)
        self.dataSet['L_198'] = cv2.imread('data/L_198.png', 0)
        self.dataSet['L_199'] = cv2.imread('data/L_199.png', 0)
        self.dataSet['L_2'] = cv2.imread('data/L_2.png', 0)
        self.dataSet['L_20'] = cv2.imread('data/L_20.png', 0)
        self.dataSet['L_200'] = cv2.imread('data/L_200.png', 0)
        self.dataSet['L_21'] = cv2.imread('data/L_21.png', 0)
        self.dataSet['L_22'] = cv2.imread('data/L_22.png', 0)
        self.dataSet['L_23'] = cv2.imread('data/L_23.png', 0)
        self.dataSet['L_24'] = cv2.imread('data/L_24.png', 0)
        self.dataSet['L_25'] = cv2.imread('data/L_25.png', 0)
        self.dataSet['L_26'] = cv2.imread('data/L_26.png', 0)
        self.dataSet['L_27'] = cv2.imread('data/L_27.png', 0)
        self.dataSet['L_28'] = cv2.imread('data/L_28.png', 0)
        self.dataSet['L_29'] = cv2.imread('data/L_29.png', 0)
        self.dataSet['L_3'] = cv2.imread('data/L_3.png', 0)
        self.dataSet['L_30'] = cv2.imread('data/L_30.png', 0)
        self.dataSet['L_31'] = cv2.imread('data/L_31.png', 0)
        self.dataSet['L_32'] = cv2.imread('data/L_32.png', 0)
        self.dataSet['L_33'] = cv2.imread('data/L_33.png', 0)
        self.dataSet['L_34'] = cv2.imread('data/L_34.png', 0)
        self.dataSet['L_35'] = cv2.imread('data/L_35.png', 0)
        self.dataSet['L_36'] = cv2.imread('data/L_36.png', 0)
        self.dataSet['L_37'] = cv2.imread('data/L_37.png', 0)
        self.dataSet['L_38'] = cv2.imread('data/L_38.png', 0)
        self.dataSet['L_39'] = cv2.imread('data/L_39.png', 0)
        self.dataSet['L_4'] = cv2.imread('data/L_4.png', 0)
        self.dataSet['L_40'] = cv2.imread('data/L_40.png', 0)
        self.dataSet['L_41'] = cv2.imread('data/L_41.png', 0)
        self.dataSet['L_42'] = cv2.imread('data/L_42.png', 0)
        self.dataSet['L_43'] = cv2.imread('data/L_43.png', 0)
        self.dataSet['L_44'] = cv2.imread('data/L_44.png', 0)
        self.dataSet['L_45'] = cv2.imread('data/L_45.png', 0)
        self.dataSet['L_46'] = cv2.imread('data/L_46.png', 0)
        self.dataSet['L_47'] = cv2.imread('data/L_47.png', 0)
        self.dataSet['L_48'] = cv2.imread('data/L_48.png', 0)
        self.dataSet['L_49'] = cv2.imread('data/L_49.png', 0)
        self.dataSet['L_5'] = cv2.imread('data/L_5.png', 0)
        self.dataSet['L_50'] = cv2.imread('data/L_50.png', 0)
        self.dataSet['L_51'] = cv2.imread('data/L_51.png', 0)
        self.dataSet['L_52'] = cv2.imread('data/L_52.png', 0)
        self.dataSet['L_53'] = cv2.imread('data/L_53.png', 0)
        self.dataSet['L_54'] = cv2.imread('data/L_54.png', 0)
        self.dataSet['L_55'] = cv2.imread('data/L_55.png', 0)
        self.dataSet['L_56'] = cv2.imread('data/L_56.png', 0)
        self.dataSet['L_57'] = cv2.imread('data/L_57.png', 0)
        self.dataSet['L_58'] = cv2.imread('data/L_58.png', 0)
        self.dataSet['L_59'] = cv2.imread('data/L_59.png', 0)
        self.dataSet['L_6'] = cv2.imread('data/L_6.png', 0)
        self.dataSet['L_60'] = cv2.imread('data/L_60.png', 0)
        self.dataSet['L_61'] = cv2.imread('data/L_61.png', 0)
        self.dataSet['L_62'] = cv2.imread('data/L_62.png', 0)
        self.dataSet['L_63'] = cv2.imread('data/L_63.png', 0)
        self.dataSet['L_64'] = cv2.imread('data/L_64.png', 0)
        self.dataSet['L_65'] = cv2.imread('data/L_65.png', 0)
        self.dataSet['L_66'] = cv2.imread('data/L_66.png', 0)
        self.dataSet['L_67'] = cv2.imread('data/L_67.png', 0)
        self.dataSet['L_68'] = cv2.imread('data/L_68.png', 0)
        self.dataSet['L_69'] = cv2.imread('data/L_69.png', 0)
        self.dataSet['L_7'] = cv2.imread('data/L_7.png', 0)
        self.dataSet['L_70'] = cv2.imread('data/L_70.png', 0)
        self.dataSet['L_71'] = cv2.imread('data/L_71.png', 0)
        self.dataSet['L_72'] = cv2.imread('data/L_72.png', 0)
        self.dataSet['L_73'] = cv2.imread('data/L_73.png', 0)
        self.dataSet['L_74'] = cv2.imread('data/L_74.png', 0)
        self.dataSet['L_75'] = cv2.imread('data/L_75.png', 0)
        self.dataSet['L_76'] = cv2.imread('data/L_76.png', 0)
        self.dataSet['L_77'] = cv2.imread('data/L_77.png', 0)
        self.dataSet['L_78'] = cv2.imread('data/L_78.png', 0)
        self.dataSet['L_79'] = cv2.imread('data/L_79.png', 0)
        self.dataSet['L_8'] = cv2.imread('data/L_8.png', 0)
        self.dataSet['L_80'] = cv2.imread('data/L_80.png', 0)
        self.dataSet['L_81'] = cv2.imread('data/L_81.png', 0)
        self.dataSet['L_82'] = cv2.imread('data/L_82.png', 0)
        self.dataSet['L_83'] = cv2.imread('data/L_83.png', 0)
        self.dataSet['L_84'] = cv2.imread('data/L_84.png', 0)
        self.dataSet['L_85'] = cv2.imread('data/L_85.png', 0)
        self.dataSet['L_86'] = cv2.imread('data/L_86.png', 0)
        self.dataSet['L_87'] = cv2.imread('data/L_87.png', 0)
        self.dataSet['L_88'] = cv2.imread('data/L_88.png', 0)
        self.dataSet['L_89'] = cv2.imread('data/L_89.png', 0)
        self.dataSet['L_9'] = cv2.imread('data/L_9.png', 0)
        self.dataSet['L_90'] = cv2.imread('data/L_90.png', 0)
        self.dataSet['L_91'] = cv2.imread('data/L_91.png', 0)
        self.dataSet['L_92'] = cv2.imread('data/L_92.png', 0)
        self.dataSet['L_93'] = cv2.imread('data/L_93.png', 0)
        self.dataSet['L_94'] = cv2.imread('data/L_94.png', 0)
        self.dataSet['L_95'] = cv2.imread('data/L_95.png', 0)
        self.dataSet['L_96'] = cv2.imread('data/L_96.png', 0)
        self.dataSet['L_97'] = cv2.imread('data/L_97.png', 0)
        self.dataSet['L_98'] = cv2.imread('data/L_98.png', 0)
        self.dataSet['L_99'] = cv2.imread('data/L_99.png', 0)
