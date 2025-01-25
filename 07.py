import cv2

img=cv2.imread('.\\images\\einstein.jpg')
cv2.putText(img,"Sir Albert Einstein",(0,450),cv2.FONT_HERSHEY_SIMPLEX,1,(0,255,250),3)
cv2.imshow("image",img)
cv2.waitKey()
cv2.destroyAllWindows()