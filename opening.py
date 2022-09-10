import cv2 
import numpy as np

# opening is dilation followed by erosion basically to help remove noise.
def opening():
    kernel = np.ones((5,5),np.uint8)
    imgs = []
    opening_list = []     
    
    
    for i in range(3):
        imgs.append(cv2.imread('image-{}.png'.format(i+1),0))   # read images in grayscale
        opening_list.append(cv2.morphologyEx(imgs[i],cv2.MORPH_OPEN,kernel,iterations = 1))
        
    for i in range(3):
        cv2.imshow('image',opening_list[i])
        cv2.waitKey(0)
        cv2.destroyAllWindows()

