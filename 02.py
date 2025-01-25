import cv2

img=cv2.imread(r'.\images\nature.jpg',0)
status=cv2.imwrite(r'.\processed\MyNature.webp',img)
print(status)