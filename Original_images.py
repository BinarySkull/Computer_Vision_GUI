import cv2      # for reading and displaying image
      
def original():
    imgs0 = []

    for i in range(3):
        imgs0.append(cv2.imread('image-{}.png'.format(i+1)))  
    
    for i in range(3):
        cv2.imshow('image',imgs0[i])
        cv2.waitKey(0)
        cv2.destroyAllWindows()


