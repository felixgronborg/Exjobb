import resize_image
import measure_exposure
import cv2
import glob
import numpy as np

# resize_image.resize_image(image_folder, size, extension)

scale = 0.25

######## FIND DARK IMAGES ########
im_folder = glob.glob('../images/%.2f/*.png' % scale) # Open image folder
thumb_folder = glob.glob('../images/Thumbnail/*.png') # Open thumbnail folder
im_list = [] # Make empty list of images
dark_list = [] # Make empty list of images that are too dark (under exposed)
for filename in im_folder: # Loop through image foldler
    image = cv2.imread(filename) # Open image
    thumb = cv2.imread(thumb_folder[im_folder.index(filename)]) # Open Thumbnail 
    print(filename, 'loaded')
    [avg, median] = measure_exposure.measure_exposure(image) # Get average and median lightness of image
    print(avg, median)
    if(avg < 85): # If the average is too low
        cv2.imshow('avg: %.2f, median: %d' % (avg, median), image) # Display image
        dark_list.append(image, avg, median) # Add image to list of dark images

cv2.waitKey(0) # Wait for keyboard input
cv2.destroyAllWindows() # Close all open windows on key input
##################################