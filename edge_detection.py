import cv2      # for reading and displaying image

def Edge_detector():
    imgs4 = []
    bilateral = []
    edged_pic = []

    for i in range(3):
        imgs4.append(cv2.imread('image-{}.png'.format(i+1),0))   # read images in grayscale
        bilateral.append (cv2.bilateralFilter(imgs4[i], 13, 15, 15))
        edged_pic.append (cv2.Canny(bilateral[i], 30, 200))

    
    for i in range(3):
        cv2.imshow('image',edged_pic[i])
        cv2.waitKey(0)
        cv2.destroyAllWindows()









