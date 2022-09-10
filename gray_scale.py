import cv2      # for reading and displaying image
      
def gray_scale():
    imgs = []
    
    for i in range(3):
        imgs.append(cv2.imread('image-{}.png'.format(i+1),0))   # read images in grayscale
        
    for i in range(3):
        cv2.imshow('image',imgs[i])
        cv2.waitKey(0)
        cv2.destroyAllWindows()


