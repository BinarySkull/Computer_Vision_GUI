import cv2
import numpy as np

def erosion():
        
    kernel = np.ones((5,5),np.uint8)
    imgs0 = []
    erosion_list = []
    
    for i in range(3):
        imgs0.append(cv2.imread('image-{}.png'.format(i+1),0))   # read images in grayscale
        erosion_list.append(cv2.erode(imgs0[i],kernel,iterations = 1))
     
    for i in range(3):
        cv2.imshow('image',erosion_list[i])
        cv2.waitKey(0)
        cv2.destroyAllWindows()