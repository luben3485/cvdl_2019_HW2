from PyQt5 import QtCore, QtGui, QtWidgets
from Ui_main import Ui_MainWindow
import cv2
import numpy as np
from matplotlib import pyplot as plt
import sys
import random

class GUI(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self,parent=None):
        super(GUI, self).__init__(parent=parent)
        self.setupUi(self)

        # push button
        self.pushButton.clicked.connect(self.disparity)
        self.pushButton_2.clicked.connect(self.template_match)
        self.pushButton_3.clicked.connect(self.keypoints)
        self.pushButton_4.clicked.connect(self.match_keypoints)
        self.kp1 = []
        self.kp2 = []
        self.des1 = None
        self.des2 = None
        self.good_match = []
    
    def disparity(self):
        imgL = cv2.imread('imL.png',0)
        imgR = cv2.imread('imR.png',0)

        stereo = cv2.StereoBM_create(numDisparities=64, blockSize=9)
        disparity = stereo.compute(imgL,imgR)
        plt.imshow(disparity,'gray')
        plt.show()

    def template_match(self):
        img = cv2.imread('ncc_img.jpg')
        img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        template = cv2.imread('ncc_template.jpg')
        w = template.shape[1]
        h = template.shape[0] #cv2.TM_CCORR_NORMED
        res = cv2.matchTemplate(img,template,cv2.TM_CCOEFF_NORMED)
        threshold = 0.98
        loc = np.where( res >= threshold)
        #min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
        #top_left = max_loc
        #bottom_right = (top_left[0] + w, top_left[1] + h)
        #cv2.rectangle(img,top_left, bottom_right,(0,0,0), 2)
        for pt in zip(*loc[::-1]):
            cv2.rectangle(img, pt, (pt[0] + w, pt[1] + h), (0,0,255), 2)
        
        plt.subplot(121),plt.imshow(res,cmap = 'gray')
        plt.title('Matching Result'), plt.xticks([]), plt.yticks([])
        plt.subplot(122),plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
        plt.title('Detected Point'), plt.xticks([]), plt.yticks([])
        plt.suptitle('Template Match')
        plt.show()

    def keypoints(self):
        img_1 = cv2.imread('Aerial1_origin.jpg', cv2.IMREAD_GRAYSCALE)
        img_2 = cv2.imread('Aerial2_origin.jpg', cv2.IMREAD_GRAYSCALE)
        sift = cv2.xfeatures2d.SIFT_create(edgeThreshold = 10,contrastThreshold = 0.004)

        kp1, des1 = sift.detectAndCompute(img_1, None)
        kp2, des2 = sift.detectAndCompute(img_2, None)

        bf = cv2.BFMatcher()
        matches = bf.knnMatch(des1, des2, k=2)
        matches = sorted(matches, key = lambda x:x[0].distance)
        
        for i in range(0,500):
            self.kp1.append(kp1[matches[i][0].queryIdx])
            self.kp2.append(kp2[matches[i][0].trainIdx])
        
        self.good_match = matches[:500]
        img_1=cv2.drawKeypoints(img_1,self.kp1,img_1)
        img_2=cv2.drawKeypoints(img_2,self.kp2,img_2)

        cv2.imwrite('Aerial1.jpg', img_1)
        cv2.imwrite('Aerial2.jpg', img_2)

        plt.subplot(121),plt.imshow(cv2.cvtColor(img_1, cv2.COLOR_BGR2RGB))
        plt.title('Aerial1.jpg'), plt.xticks([]), plt.yticks([])
        plt.subplot(122),plt.imshow(cv2.cvtColor(img_2, cv2.COLOR_BGR2RGB))
        plt.title('Aerial2.jpg'), plt.xticks([]), plt.yticks([])
        plt.suptitle('SIFT')
        plt.show()

        #points2f = cv2.KeyPoint_convert(self.kp1)
        #print(points2f)
        
        

    def match_keypoints(self):
        img_1 = cv2.imread('Aerial1_origin.jpg', cv2.IMREAD_GRAYSCALE)
        img_2 = cv2.imread('Aerial2_origin.jpg', cv2.IMREAD_GRAYSCALE)
        #print(self.kp1)
        #print(self.kp2)
        #print(self.good_match)
        img_out = cv2.drawMatchesKnn(img_1,self.kp1,img_2,self.kp2,self.good_match,None,flags=2)
        plt.imshow(img_out)
        plt.show()

        


if __name__ == '__main__':  
    app = QtWidgets.QApplication(sys.argv)
    gui = GUI()
    gui.show()
    sys.exit(app.exec_()) 