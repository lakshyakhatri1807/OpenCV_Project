import cv2
import numpy as np
#Load image
image = cv2.imread('sample.jpg')


resize_image = cv2.resize(image,(300,300))

average_blur = cv2.blur(resize_image,(7,7))
gaussian_blur = cv2.GaussianBlur(resize_image,(7,7),0)
median_blur = cv2.medianBlur(resize_image,7)
bilateral_blur = cv2.bilateralFilter(resize_image,15,75,75)

def put_label(img, text, pos=(10, 25)):
    return cv2.putText(img, text, pos, cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0),2)

org_lbl = put_label(image.copy(), "Orginal Image")
resize_lbl = put_label(resize_image, "Resized Image")
average_lbl = put_label(average_blur, "Average Blur Image")
gaussian_lbl = put_label(gaussian_blur, "GAUSSIAN Blur")
median_lbl = put_label(median_blur, "Median Blur")
bilateral_lbl = put_label(bilateral_blur,"Bilateral Blur")
                       

                       




cv2.imshow('orginal image', resize_image)
cv2.imshow ('average image', average_blur)
cv2.imshow ('gaussian image', gaussian_blur)
cv2.imshow ('median image' , median_blur)
cv2.imshow ('bilateral image', bilateral_blur)
cv2.waitKey(0)
cv2.destroyAllWindows()