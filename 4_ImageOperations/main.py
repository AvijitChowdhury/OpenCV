import cv2
import numpy as np

img = cv2.imread('tiger.jpg',cv2.IMREAD_COLOR)

px = img[55,55]
 # img[55,55]=[255,255,255]
px = img[100:150,100:150]


#we can also modify this roi range of region
img[100:150,100:150] = [255,255,255]
print(px)

#certain charecteristice of image
print(img.shape)
print(img.size)
print(img.dtype)

#some operations
watch_face= img[37:111,107:194]
img[0:74,0:87] = watch_face

cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()