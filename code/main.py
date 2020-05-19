import resize_image
import measure_exposure
import cv2
import glob
import numpy as np

# resize_image.resize_image(image_folder, size, extension)

scale = 0.25

im_folder = glob.glob('../images/%.2f/*.png' % scale)
thumb_folder = glob.glob('../images/Thumbnail/*.png')
im_list = []
for filename in im_folder:
    image = cv2.imread(filename)
    thumb = cv2.imread(thumb_folder[im_folder.index(filename)])
    print(filename, 'loaded')
    [avg, median] = measure_exposure.measure_exposure(image)
    print(avg, median)
    if(avg < 85):
        cv2.imshow('avg: %.2f, median: %d' % (avg, median), image)
        print("DARK IMAGE PLS FIX NOW IMMEDIATELY YES THANKS")

cv2.waitKey(0)
cv2.destroyAllWindows()