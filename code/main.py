import resize_image

image_folder = "../samling_ex_jobb/*.jpg" #assuming jpg
size = 'Thumbnail'
extension = 'png'

resize_image.resize_image(image_folder, size, extension)

# TO DO:
# Save scaled images to file
# Make folders with thumbnail size, half, and 1/3 size images
# Test BW to Gray and Anti-Aliasing

print("shut up")