import cv2      # for reading and displaying image

def Binary_Threshold():
    imgs3 = []
    binary_list = []
    
    
    for i in range(3):
        imgs3.append(cv2.imread('image-{}.png'.format(i+1),0))   
        (thresh, bina) = cv2.threshold(imgs3[i], 127, 255, cv2.THRESH_BINARY)
        binary_list.append(bina)
        
        
        
    for i  in range(3):
        cv2.imshow('image',binary_list[i])
        cv2.waitKey(0)
        cv2.destroyAllWindows()    
        
        
    