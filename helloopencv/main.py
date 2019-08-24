import sys
import cv2

img = cv2.imread("./imgs/penguins.jpg", 1)
resized_img = cv2.resize(img, (450, 500))


cv2.imshow("pengoons", resized_img)
cv2.waitKey(0)
#cv2.waitKey(2000)
cv2.destroyAllWindows(resized_img)
