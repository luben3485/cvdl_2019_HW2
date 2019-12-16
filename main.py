from PyQt5 import QtCore, QtGui, QtWidgets
from Ui_main import Ui_MainWindow
import cv2
import numpy as np
from matplotlib import pyplot as plt
import sys

class GUI(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self,parent=None):
        super(GUI, self).__init__(parent=parent)
        self.setupUi(self)

        # push button
        self.pushButton.clicked.connect(self.disparity)
        self.pushButton_2.clicked.connect(self.template_match)
        #self.pushButton_3.clicked.connect()
        #self.pushButton_4.clicked.connect()

    def disparity(self):
        imgL = cv2.imread('imL.png',0)
        imgR = cv2.imread('imR.png',0)

        stereo = cv2.StereoBM_create(numDisparities=64, blockSize=9)
        disparity = stereo.compute(imgL,imgR)
        plt.imshow(disparity,'gray')
        plt.show()

    def template_match(self):
        img = cv2.imread('ncc_img.jpg')
        template = cv2.imread('ncc_template.jpg')
        w = template.shape[1]
        h = template.shape[0]
        res = cv2.matchTemplate(img,template,cv2.TM_CCOEFF_NORMED)
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
        top_left = min_loc
        bottom_right = (top_left[0] + w, top_left[1] + h)
        cv2.rectangle(img,top_left, bottom_right, 255, 2)
        plt.subplot(121),plt.imshow(res,cmap = 'gray')
        plt.title('Matching Result'), plt.xticks([]), plt.yticks([])
        plt.subplot(122),plt.imshow(img)
        plt.title('Detected Point'), plt.xticks([]), plt.yticks([])
        #plt.suptitle('')
    
        plt.show()


if __name__ == '__main__':  
    app = QtWidgets.QApplication(sys.argv)
    gui = GUI()
    gui.show()
    sys.exit(app.exec_()) 