import cv2
import numpy as np

# load images
golden = cv2.imread("golden_bottom.jpg")
test = cv2.imread("test_bottom.jpg")

# convert to grayscale
g_gray = cv2.cvtColor(golden, cv2.COLOR_BGR2GRAY)
t_gray = cv2.cvtColor(test, cv2.COLOR_BGR2GRAY)

# blur to reduce noise
g_blur = cv2.GaussianBlur(g_gray,(5,5),0)
t_blur = cv2.GaussianBlur(t_gray,(5,5),0)

# edge detection
g_edges = cv2.Canny(g_blur,50,150)
t_edges = cv2.Canny(t_blur,50,150)

# difference between golden and test
diff = cv2.absdiff(g_edges,t_edges)

# threshold
_,thresh = cv2.threshold(diff,30,255,cv2.THRESH_BINARY)

# clean noise
kernel = np.ones((3,3),np.uint8)
thresh = cv2.morphologyEx(thresh,cv2.MORPH_CLOSE,kernel)

# find contours
contours,_ = cv2.findContours(thresh,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)

for c in contours:
    area = cv2.contourArea(c)

    if area > 50:  # adjust sensitivity
        x,y,w,h = cv2.boundingRect(c)
        cv2.rectangle(test,(x,y),(x+w,y+h),(0,0,255),2)

# show result
cv2.imshow("Detected Defect",test)
cv2.imshow("Difference",thresh)

cv2.waitKey(0)
cv2.destroyAllWindows()
