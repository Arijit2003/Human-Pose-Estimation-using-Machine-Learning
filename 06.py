import cv2

img=cv2.imread('.\\images\\nature.jpg',1)
cv2.circle(img,(80,80),55,(0,255,0),-1)
cv2.imshow('image',img)
cv2.waitKey()
cv2.destroyAllWindows()

img=cv2.imread('.\\images\\nature.jpg',1)
cv2.rectangle(img,(15,25),(200,150),(0,255,0),5)
cv2.imshow('image',img)
cv2.waitKey()
cv2.destroyAllWindows()

img=cv2.imread('.\\images\\nature.jpg',1)
cv2.line(img,(80,80),(500,500),(0,255,0),5)
cv2.imshow('image',img)
cv2.waitKey()
cv2.destroyAllWindows()

img=cv2.imread('.\\images\\nature.jpg',1)
cv2.ellipse(img,(200,200),(80,20),10,0,360,(0,255,0),-5)
cv2.imshow('image',img)
cv2.waitKey()
cv2.destroyAllWindows()