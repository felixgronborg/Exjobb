import cv2
import numpy as np
import matplotlib.pyplot as plt

scale = 0.25

cold1 = cv2.imread('C:/Users/Felix/Desktop/Skola/5/exjobb/Git_repo/Exjobb/images/%.2f/0.png' % scale)
good1 = cv2.imread('C:/Users/Felix/Desktop/Skola/5/exjobb/Git_repo/Exjobb/images/%.2f/1.png' % scale)
green = cv2.imread('C:/Users/Felix/Desktop/Skola/5/exjobb/Git_repo/Exjobb/images/%.2f/3.png' % scale)
yellow = cv2.imread('C:/Users/Felix/Desktop/Skola/5/exjobb/Git_repo/Exjobb/images/%.2f/4.png' % scale)
under_exp = cv2.imread('C:/Users/Felix/Desktop/Skola/5/exjobb/Git_repo/Exjobb/images/%.2f/5.png' % scale)
over_exp = cv2.imread('C:/Users/Felix/Desktop/Skola/5/exjobb/Git_repo/Exjobb/images/%.2f/6.png' % scale)
test = cv2.imread('C:/Users/Felix/Desktop/Skola/5/exjobb/Git_repo/Exjobb/images/%.2f/test.png' % scale)


orig = cv2.imread('C:/Users/Felix/Desktop/Skola/5/exjobb/Git_repo/Exjobb/images/1/1.png')

im = over_exp
im_g = im.copy()
gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
im_g[:,:,0] = gray
im_g[:,:,1] = gray
im_g[:,:,2] = gray

cv2.imshow('image', im)
cv2.waitKey(0)
cv2.destroyAllWindows()
# BGR to HLS values: [0-180, 0-255, 0-255]
hls = cv2.cvtColor(im, cv2.COLOR_BGR2HLS)
hls_g = cv2.cvtColor(im_g, cv2.COLOR_BGR2HLS)
light_list = np.zeros(256)
light_list_g = np.zeros(256)

for i in range(hls.shape[0]):
    for j in range(hls.shape[1]):
            light_list[hls[i,j,1]] = light_list[hls[i,j,1]] + 1
for i in range(hls_g.shape[0]):
    for j in range(hls_g.shape[1]):
            light_list_g[hls_g[i,j,1]] = light_list_g[hls_g[i,j,1]] + 1

fig, axs = plt.subplots(2)
fig.suptitle('Color and Gray image comparison in lightness')
axs[0].plot(light_list)
axs[1].plot(light_list_g)

plt.show()

avg_lightness = 0
avg_lightness_g = 0
pixels = 0
median = []
for i in range(len(light_list)):
    avg_lightness = avg_lightness + (i * light_list[i])
    pixels = pixels + light_list[i]
avg_lightness = avg_lightness/pixels
pixels = 0
for i in range(len(light_list_g)):
    avg_lightness_g = avg_lightness_g + (i * light_list_g[i])
    pixels = pixels + light_list_g[i]
avg_lightness_g = avg_lightness_g/pixels
print(avg_lightness)
print(avg_lightness_g)