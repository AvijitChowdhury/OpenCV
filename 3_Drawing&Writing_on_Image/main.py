import numpy as np
import cv2
#opencv use BGR blue green red
img= cv2.imread('images.jpg',cv2.IMREAD_COLOR)

cv2.line(img,(0,0),(150,0),(255,255,0),15)
cv2.rectangle(img,(0,0),(150,150),(0,255,255),3,None,None)
cv2.circle(img,(100,63),30,(0,0,255),2,None,None)

# pts = np.array([[100,50],[200,300],[700,200],[500,100]], np.int32)
# pts = pts.reshape((-1,1,2))
# cv2.polylines(img, [pts], True, (0,255,255), 3)



pts = np.array([[100,50],[120,70],[160,90],[200,100]],np.int32)
# pts = pts.reshape((-1,1,2))
cv2.polylines(img,[pts],True,(255,255,0),None,None,None)

font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img,'OPENCV',(3,150),font,2,(0,255,0),10,cv2.LINE_AA)

cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()