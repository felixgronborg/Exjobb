import resize_image
import glob

from PIL import Image

image_folder = "../samling_ex_jobb/*.jpg" #assuming jpg
image_list = []
for filename in glob.glob(image_folder): 
    im=Image.open(filename)
    image_list.append(im)

scaled_list = resize_image.resize(image_list, 0.1)

# TO DO:
# Save scaled images to file
# Make folders with thumbnail size, half, and 1/3 size images
# Test BW to Gray and Anti-Aliasing


print(len(scaled_list))

print("shut up")