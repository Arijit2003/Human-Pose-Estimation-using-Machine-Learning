import cv2

img=cv2.imread('.\\images\\keywords.png')#by default the flag is 1
img=cv2.resize(img,(450,300), interpolation=cv2.INTER_AREA)
cv2.imshow('resized image',img)
cv2.waitKey()
cv2.destroyAllWindows()