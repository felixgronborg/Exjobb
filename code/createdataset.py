import matplotlib.pyplot as plt
import glob
import pandas as pd

# from skimage import data, color
# from skimage.transform import rescale, resize, downscale_local_mean
from PIL import Image


image_folder = "../samling_ex_jobb/*.jpg" #assuming jpg
image_list = []
for filename in glob.glob(image_folder): 
    im=Image.open(filename)
    image_list.append(im)

print(len(image_list))

data = {'Image': [],
        'Crooked': [],
        'BadFocus': [],
        'Shadowed': [],
        'Sky': [],
        'BadColor': []}

