import cv2
import numpy as np
import matplotlib.pyplot as plt
import math

def measure_exposure(img):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    img_gray = img.copy() # Make a 3-Dimensional gray image
    for i in range(3):
        img_gray[:,:,i] = gray
    
    img = img_gray
    hls = cv2.cvtColor(img, cv2.COLOR_BGR2HLS) # Convert both color and gray to HSL

    light_list = np.zeros(256) # Make a list of light values

    for i in range(hls.shape[0]): # Invert the HLS lightness matrix
        for j in range(hls.shape[1]):
            light_list[hls[i,j,1]] = light_list[hls[i,j,1]] + 1
    
    total_lightness = 0
    no_pixels = 0
    
    for i in range(len(light_list)):
        total_lightness = total_lightness + (i * light_list[i])
        no_pixels = no_pixels + light_list[i]
    
    average_lightness = total_lightness/no_pixels
    
    list_of_lights = []

    for i in range(hls.shape[0]):
        for j in range(hls.shape[1]):
            list_of_lights.append(hls[i,j,1])
    
    median_lightness = list_of_lights[math.floor(len(list_of_lights)/2)]

    return [average_lightness, median_lightness]
