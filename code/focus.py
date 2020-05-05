import cv2
import numpy as numpy

img = cv2.imread("correct_colors.jpg")
img = cv2.imread("rorelseoskarpa_010.jpg")


scale_percent = 20 # percent of original size
width = int(img.shape[1] * scale_percent / 100)
height = int(img.shape[0] * scale_percent / 100)
dim = (width, height)

img_resized = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)


laplacian_var = cv2.Laplacian(img_resized, cv2.CV_64F).var()
if laplacian_var < 5:
    print("image blurry")

print(laplacian_var)

cv2.imshow("Img", img_resized)
cv2.imshow("Laplacian", laplacian_var)
cv2.waitKey(0)
cv2.destroyAllWindows()