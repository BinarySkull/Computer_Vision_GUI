import cv2      # for reading and displaying image
import skimage.filters


def gaussian_filter():

    imgs2 = []
    blured_list = []
    
    for i in range(3):
        imgs2.append(cv2.imread('image-{}.png'.format(i+1),0))   # read images in grayscale
        blured_list.append (skimage.filters.gaussian(imgs2[i], sigma=1.0))
    
    for i in range(3):
        cv2.imshow('image',blured_list[i])
        cv2.waitKey(0)
        cv2.destroyAllWindows()


    




