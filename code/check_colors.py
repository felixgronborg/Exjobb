import numpy as np
import cv2

def check_colors(image):
    # gray = np.zeros(image.shape)
    # no_gray_pixels = 0
    # b = np.zeros(image.shape[0]*image.shape[1])
    # g = np.zeros(image.shape[0]*image.shape[1])
    # r = np.zeros(image.shape[0]*image.shape[1])
    # for i in range (image.shape[0]):
    #     for j in range (image.shape[1]): 
    #         b[i*j]=image[i,j,0]
    #         g[i*j]=image[i,j,1]
    #         r[i*j]=image[i,j,2]
    #         if b[i*j] == g[i*j] and b[i*j] == r[i*j]:
    #             gray[i,j] = image[i,j]/255
    #             no_gray_pixels += 1
    # cv2.imshow('', gray)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV) #Convert to HSV
    # low_h_hsv = np.zeros(hsv.shape) 
    total_s = float(0)
    its = 0
    good_coords = []
    for i in range(hsv.shape[0]): # Loop over every pixel
        for j in range(hsv.shape[1]):
            its += 1
            total_s += hsv[i,j,1] # Add pixel's S (saturation) value to total
    average_s = float(total_s/its) # Calculate average saturation of photo
    for i in range(hsv.shape[0]): # Loop over every pixel again
        for j in range(hsv.shape[1]):
            if(hsv[i,j,1] > average_s/1.5): # If the pixel's S value is higher than the threshold
                hsv[i,j,2] = 0 # Set the V-value to 0 (make pixel black)
            else:
                coord = [i,j]
                good_coords.append(coord) # Else append pixel's coords to list of coords with low S

    bgr = cv2.cvtColor(hsv, cv2.COLOR_HSV2BGR) # Convert back to BGR (reverse rgb)
    b = 0
    g = 0
    r = 0
    for coords in good_coords: # Loop over all low S pixels
        b += bgr[coords[0], coords[1], 0] # Add blue value of pixel
        g += bgr[coords[0], coords[1], 1] # Add green value of pixel
        r += bgr[coords[0], coords[1], 2] # Add red value of pixel

    sample = []

    b_avg = b / len(good_coords) # Average colors
    g_avg = g / len(good_coords)
    r_avg = r / len(good_coords)

    sample.append(b_avg) # Make a sample of combined RGB values
    sample.append(g_avg)
    sample.append(r_avg)

    cv2.imshow('saturation below %d' % average_s, bgr) 
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    return average_s, sample
    # return no_gray_pixels