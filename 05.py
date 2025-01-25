import cv2

img=cv2.imread('.\\images\\einstein.jpg',1)
(h,w)=img.shape[:2]
center=(w/2,h/2)
angle90=90
angle180=180
angle270=270

scale=1.0

M=cv2.getRotationMatrix2D(center,angle90,scale)
rotated90=cv2.warpAffine(img,M,(h,w))


M=cv2.getRotationMatrix2D(center,angle180,scale)
rotated180=cv2.warpAffine(img,M,(h,w))


M=cv2.getRotationMatrix2D(center,angle270,scale)
rotated270=cv2.warpAffine(img,M,(h,w))


cv2.imshow('rotated90',rotated90)
cv2.imshow('rotated180',rotated180)
cv2.imshow('rotated270',rotated270)
cv2.waitKey()
cv2.destroyAllWindows()
