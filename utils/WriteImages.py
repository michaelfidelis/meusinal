#!/usr/bin/env python
import cv2
import numpy as np

# =====================================================================================================================
# Principal
class Principal:
    def __init__(self):
        self.capture = cv2.VideoCapture(0)
        self.configuracao = None
        self.count = 0

        while self.capture.isOpened():
            try:
                # Obtem a imagem da camera
                _, image = self.capture.read()

                # Gera uma sub imagem para processamento
                crop_image = self.obterSubImagem(image)

                # Obtem a area de interesse
                roi = self.obterROI(crop_image)

                cv2.imshow('ROI', cv2.flip(roi, 1))

                # Exibe a imagem obtida pela camera
                flipped_image = cv2.flip(image, 1)
                cv2.imshow('Principal', flipped_image)

                interrupt = cv2.waitKey(10)
                if interrupt & 0xFF == ord('q'):
                    print('Encerrando execucao...')
                    break

                if interrupt & 0xFF == ord('g'):
                    nome = 'gerado/' + str(self.configuracao) + '_' + str(self.count) + '.png'
                    print(nome)
                    cv2.imwrite(str(nome), roi)
                    self.count += 1

                if interrupt & 0xFF == ord('c'):
                    text = raw_input('Digite uma configuracao: ')
                    self.configuracao = text.upper()
                    print('Configuracao alterada para ' + str(self.configuracao))
                    self.count = 0

            except Exception as inst:
                print(inst)
                print('Encerrando execucao.')
                break
    # =================================================================================================================
    # Fim do processamento

        # Fecha a camera e as janelas
        self.capture.release()
        cv2.destroyAllWindows()

    # =================================================================================================================
    # Etapa 0 - Obtem sub imagem
    @staticmethod
    def obterSubImagem(image):
        cv2.rectangle(image, (250, 250), (10, 10), (0, 255, 0), 2)
        return image[10:250, 10:250]

    # =================================================================================================================
    # Etapa 1 - Obtem a area de interesse
    @staticmethod
    def obterROI(image):
        kernel = np.ones((5, 5), np.uint8)
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        blur = cv2.GaussianBlur(gray, (5, 5), 0)
        _, thresh = cv2.threshold(blur, 127, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
        opening = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel)
        closing = cv2.morphologyEx(opening, cv2.MORPH_CLOSE, kernel)
        return closing


if __name__ == '__main__':
    principal = Principal()
