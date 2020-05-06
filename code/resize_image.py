import matplotlib.pyplot as plt
import numpy as np
import glob
import pathlib
from PIL import Image
from skimage import data, color
from skimage.transform import rescale, resize, downscale_local_mean
import sys

def resize_image(image_folder : str, scale: float or str, extension : str):
    
    if extension.upper() == 'PNG':
        saveformat = '.png'
    elif extension.upper() == 'JPG':  
        saveformat = '.jpg'

    image_list = []
    for filename in glob.glob(image_folder): 
        im=Image.open(filename)
        image_list.append(im)
    scaled_list = []
    for i in range(len(image_list)):
        im = np.array(image_list[i])

        info = np.iinfo(im.dtype) # Get the information of incoming image type
        im = im.astype(np.float64) / info.max # Normalize the data in range [0,1]
        im = 255 * im # Scale by 255
        im = im.astype(np.uint8) # Make sure data is uint8

        print(isinstance(scale, str), isinstance(scale, float), isinstance(scale, int))
        if isinstance(scale, str):
            if scale.upper() == "THUMBNAIL":
                im_scaled = np.empty((128, 128, 3))
                for i in range (0,3):
                    im_scaled[:,:,i] = resize(im[:,:,i], (128, 128))
        elif isinstance(scale, float) or isinstance(scale, int):
            rows = round(im.shape[0] * scale)
            cols = round(im.shape[1] * scale)
            dims = im.shape[2]
            im_scaled = np.empty((rows, cols, dims))
            for i in range (0,3):
                im_scaled[:,:,i] = rescale(im[:,:,i], scale, anti_aliasing = False)
        else:
            print("Scale is expected as string, float or int")
            sys.exit()
        im_scaled = im_scaled.astype(np.float64) / np.amax(im_scaled) # Normalize the data in range [0,1]
        im_scaled = 255 * im_scaled # Scale by 255
        im_scaled = im_scaled.astype(np.uint8) # Make sure data is uint8
        
        scaled_list.append(im_scaled)
        print(len(scaled_list), 'images scaled')

    path = '../images/%s' % str(scale)
    pathlib.Path(path).mkdir(parents=True, exist_ok=True) 
    
    for i in range(len(scaled_list)):
        save_location = ('%s/%d%s' % (path, i, saveformat))
        print(save_location)
        newimage = Image.fromarray(scaled_list[i])
        newimage.save(save_location)
        print('Image successfully saved to', save_location)