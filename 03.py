import cv2

img=cv2.imread('.\\images\\keywords.png',1)
img=cv2.resize(img,(450,300))
dimentions=img.shape
height=dimentions[0]
width=dimentions[1]
channels=dimentions[2]
size=img.size

print('dimention:',dimentions)
print('height:',height)
print('width:',width)
print('channels:',channels)
print('size:',size)

b,g,r=cv2.split(img)
merged_bgr=cv2.merge((b,g,r))
merged_rgb=cv2.merge((r,g,b))

cv2.imshow("original_image",img)
cv2.imshow("b",b)
cv2.imshow("g",g)
cv2.imshow("r",r)
cv2.imshow("merged_bgr",merged_bgr)
cv2.imshow("merged_rgb",merged_rgb)




cv2.waitKey()
cv2.destroyAllWindows()