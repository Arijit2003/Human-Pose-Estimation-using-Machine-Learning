import cv2
'''
In Python, the r before a string is used to 
indicate a raw string literal. It tells Python 
to treat backslashes (\) in the string as literal 
characters rather than as escape characters.
'''
img=cv2.imread(r'.\images\nature.jpg',1)#1-colored, 0-grayscale
# print(img)
img1=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
img2=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
img3=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
img4=cv2.cvtColor(img,cv2.COLOR_BGR2LAB)

cv2.imshow('Image',img)
cv2.imshow('Gray Image',img1)
cv2.imshow('RGB Image',img2)
cv2.imshow('HSV Image',img3)
cv2.imshow('LAB Image',img4)
cv2.waitKey(0)
cv2.destroyAllWindows()
