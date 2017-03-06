import cv2;
import numpy as np;

#GLOBAL VARIABLES#
drawing = False;
ix, iy = -1, -1;
ex, ey = -1, -1;
roi_selected = False;
#END OF GLOBAL VARIABLES#

#start of draw fn def#
def draw_rectangle(event, x, y, flags, param):
    print ('inside draw_rectangle');
    global ix, iy, ex, ey, drawing;
    if event == cv2.EVENT_LBUTTONDOWN:
        print('cv2.EVENT_LBUTTONDOWN', (x, y));
        drawing = True;
        ix, iy = x, y;
    elif event == cv2.EVENT_MOUSEMOVE:
        print('cv2.EVENT_MOUSEMOVE');
        if drawing == True:
            cv2.rectangle(img, (ix, iy), (x, y), 255, -1);
    elif event == cv2.EVENT_LBUTTONUP:
        print('cv2.EVENT_LBUTTONUP', (x, y));
        drawing = False;
        ex, ey = x, y;
        cv2.rectangle(img, (ix, iy), (x, y), 255, -1);
#end of draw fn def#


#naming windows, give behavior of the window WINDOW_NORMAL => allow resizing
cv2.namedWindow('original', cv2.WINDOW_NORMAL);

#read image with specified color scale
original_img = cv2.imread('my_image.jpg', cv2.IMREAD_GRAYSCALE);
img = original_img.copy();
print('original image shape: ');
print(img.shape);

#sets mouse-events callback function
cv2.setMouseCallback('original', draw_rectangle);
print('mouse callback set');

#takes roi from user
while(1):
    print('inside while to mark roi');
    cv2.imshow('original', img);
    print('image shwoing successful');
    cv2.waitKey(1);
    print('roi_selected old: ', roi_selected);
    roi_selected = ix>0 and iy>0 and ex>0 and ey>0;
    print('roi_selected new: ', roi_selected);
    if roi_selected:
        break;

cv2.destroyWindow('original');

#roi has been marked, contiue to extract ROI image
cv2. namedWindow('processed', cv2.WINDOW_AUTOSIZE);

#extract ROI
startx, starty, endx, endy = ix, iy, ex, ey;
print('before swapping', (starty, endy), (startx, endx));
if ix>ex:
    startx, endx = ex, ix;
if iy>ey:
    starty, endy = ey, iy;
print('after swapping', (starty, endy), (startx, endx));

roi = original_img[starty:endy, startx:endx];
print('roi image shape: ');
print (roi.shape);

cv2.imshow('processed', roi);

cv2.waitKey(0);
cv2.destroyAllWindows();
