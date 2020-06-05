import resize_image
import measure_exposure
import check_colors
import over_exposure
import cv2
import glob
import numpy as np

# resize_image.resize_image(image_folder, size, extension)

scale = 0.25
im_folder = glob.glob('../images/%.2f/*.png' % scale) # Open image folder
thumb_folder = glob.glob('../images/Thumbnail/*.png') # Open thumbnail folder
im_list = [] # Make empty list of images
##################################
######## FIND DARK IMAGES ########
##################################
# dark_list = [] # Make empty list of images that are too dark (under exposed)
# for filename in im_folder: # Loop through image foldler
#     image = cv2.imread(filename) # Open image
#     thumb = cv2.imread(thumb_folder[im_folder.index(filename)]) # Open Thumbnail 
#     print(filename, 'loaded')
#     [avg, median] = measure_exposure.measure_exposure(image) # Get average and median lightness of image
#     if(avg < 85): # If the average is too low
#         cv2.imshow('Too dark with avg: %.2f, median: %d' % (avg, median), image) # Display image
#         cv2.waitKey(0) # Wait for keyboard input
#         cv2.destroyAllWindows() # Close all open windows on key input
#         dark_list.append(avg) # Add image to list of dark images
#     # else: 
#     #     cv2.imshow('Not too dark', image)

##################################
########## CHECK COLORS ##########
##################################
image_numbers = ['\\0.png', '\\1.png', '\\3.png', '\\4.png', '\\5.png', '\\11.png', '\\24.png']
for filename in im_folder:
    # if any(number in filename for number in image_numbers):
    if filename == '../images/0.25\\11.png':
        im_list.append(cv2.imread(filename))
        print(filename, 'loaded')
    if filename == '../images/0.25\\1.png':
        reference = cv2.imread(filename)
        print(filename, 'loaded as reference')

total_s = 0
bad_list = []
for im in im_list:
    _, colors = check_colors.check_colors(im)

    if (colors[2] - colors[1] > 10 and colors[2] - colors[0] > 10): # If red is prominant
        cv2.imshow('Red tint',im)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    elif (colors[1] - colors[2] > 10 and colors[1] - colors[0] > 10): # If green is prominant
        cv2.imshow('Green tint',im)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    elif (colors[0] - colors[2] > 10 and colors[0] - colors[1] > 10): # If blue is prominant
        cv2.imshow('Blue tint',im)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    elif (colors[2] - colors[1] > 10 and abs(colors[2] - colors[0] < 10)): # If red and blue is prominant
        cv2.imshow('Purple tint',im)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    elif (colors[2] - colors[0] > 10 and abs(colors[2] - colors[1] < 10)): # If red and green is prominant
        cv2.imshow('Yellow tint',im)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    elif (colors[1] - colors[2] > 10 and abs(colors[1] - colors[0] < 10)): # If green and blue is prominant
        cv2.imshow('Purple tint',im)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    else:
        cv2.imshow('Good white balance', im)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
##
# Correction attempt
##
# image = im_list[0].copy()

# avg_colors = (colors[0]+colors[1]+colors[2])/3
# b_corr = int(avg_colors - colors[0])
# g_corr = int(avg_colors - colors[1])
# r_corr = int(avg_colors - colors[2])

# print(b_corr, g_corr, r_corr)

# for i in range(image.shape[0]):
#     for j in range(image.shape[1]):
#         if(image[i,j,0] + b_corr*2 > 255):
#             image[i,j,0] = 255
#         elif(image[i,j,0] + b_corr*2 < 0):
#             image[i,j,0] = 0
#         else:
#             image[i,j,0] += b_corr*2
#         if(image[i,j,1] + g_corr*2 > 255):
#             image[i,j,1] = 255
#         elif(image[i,j,1] + g_corr*2 < 0):
#             image[i,j,1] = 0
#         else:
#             image[i,j,1] += g_corr*2
#         if(image[i,j,2] + r_corr*2 > 255):
#             image[i,j,2] = 255
#         elif(image[i,j,2] + r_corr*2 < 0):
#             image[i,j,2] = 0
#         else:
#             image[i,j,2] += r_corr*2
# cv2.imshow('Original image', im_list[0])
# cv2.waitKey(0)
# cv2.imshow('Corrected image', image)
# cv2.waitKey(0)
# cv2.imshow('Reference image', reference)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
##
#
##

################################## 
#### FIND OVER EXPOSED IMAGES ####
##################################
# i = 0
# for filename in im_folder:
#     if i==25:
#         image = cv2.imread(filename)
#         print(image.shape)
#     i += 1
    
# over_exposure.is_overexposed(image)