import numpy as np
import cv2

#Global Variable#
is_roi_selected = False;
is_roi_frame_read = False;

drawing = False;
ix, iy = -1, -1;
ex, ey = -1, -1;
#End of Global Variables#

#start of draw fn def#
def draw_rectangle(event, x, y, flags, param):
        global ix, iy, ex, ey, drawing;
        if event == cv2.EVENT_LBUTTONDOWN:
            drawing = True;
            ix, iy = x, y;
        elif event == cv2.EVENT_MOUSEMOVE:
            if drawing == True:
                cv2.rectangle(frame, (ix, iy), (x, y), 255, -1);
        elif event == cv2.EVENT_LBUTTONUP:
            drawing = False;
            ex, ey = x, y;
            cv2.rectangle(frame, (ix, iy), (x, y), 255, -1);
#end of draw fn def#

cap = cv2.VideoCapture(0);

#Auto Sized window to show roi selection frame. Will fit to the frame dimensions
cv2.namedWindow('roi_frame', cv2.WINDOW_AUTOSIZE);
cv2.setMouseCallback('roi_frame', draw_rectangle);

#Read first frame and show to select roi#
while(not is_roi_frame_read):
    is_roi_frame_read, frame = cap.read();
else:
    while(1):
        cv2.imshow('roi_frame', frame);
        cv2.waitKey(1);
        is_roi_selected = ix>0 and iy>0 and ex>0 and ey>0;
        if is_roi_selected:
            break;
    
    #extract ROI
    startx, starty, endx, endy = ix, iy, ex, ey;
    if ix>ex:
        startx, endx = ex, ix;
    if iy>ey:
        starty, endy = ey, iy;

cv2.destroyWindow('roi_frame');
#ROI selection finished#

print('x and y', iy, ey, ix, ex);
print('start and end', starty, endy, startx, endx);

#Resizable window to show cropped frames
cv2.namedWindow('cropped', cv2.WINDOW_NORMAL);

while(cap.isOpened()):
    # Capture frame-by-frame
    ret, frame = cap.read();

    # Our operations on the frame come here
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    #crop frame if ROI is seleceted
    if(is_roi_selected):
        cropped = gray[starty:endy, startx:endx];
    else:
        cropped = gray;

    # Display the resulting frame
    cv2.imshow('cropped', cropped)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    
# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
