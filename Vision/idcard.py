import numpy as np
import cv2
import numpy as np
image = cv2.imread('idcard.jpg')
orig = image.copy()

r=800.0/image.shape[0]
dim = (int(image.shape[1]*r),800)
image = cv2.resize(image,dim,interpolation=cv2.INTER_AREA)

gray =cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
gray =cv2.GaussianBlur(gray,(3,3),0)
edged =cv2.Canny(gray,75,200)

print("STEP 1: Edge Detection")

#cv2.namedWindow('Image',cv2.WINDOW_NORMAL)
#cv2.namedWindow('Edged',cv2.WINDOW_NORMAL)

warped = cv2.adaptiveThreshold(gray,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,21, 10)
cv2.imshow("Image",image)
cv2.imshow("Edged",edged)
cv2.imshow("Warped",warped)


cv2.waitKey(0)
cv2.destroyAllWindows()