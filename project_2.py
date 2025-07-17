import cv2
#Load image
image = cv2.imread('sample.jpg')

resize = cv2.resize(image,(300,300))
rotate = cv2.rotate(image,cv2.ROTATE_180)
image[100:300,200:400]
flip = cv2.flip(image,1)

cv2.imshow('p', flip)
cv2.imshow('Orignal Image', rotate)
cv2.imshow('resize image', resize)
cv2.imshow('rotate image', image )
cv2.waitKey(0)
cv2.destroyAllWindows()