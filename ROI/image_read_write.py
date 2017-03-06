import cv2;
import numpy as np;

#naming windows, give behavior of the window WINDOW_NORMAL => allow resizing
cv2. namedWindow('original', cv2.WINDOW_NORMAL);
#cv2. namedWindow('processed', cv2.WINDOW_NORMAL);

#read image with specified color scale
img = cv2.imread('my_image.jpg', cv2.IMREAD_GRAYSCALE);

cv2.imshow('original', img);

#for 64-bit machines need to use & 0xFF with waitKey
k = cv2.waitKey(0) & 0xFF;
print ("print works");
if k == 27:
    print ("do not save");
    cv2.destroyAllWindows();
elif k == ord('s'):
    print ("save");
    cv2.imwrite('saved_image.jpg', img);
    cv2.destroyAllWindows();

