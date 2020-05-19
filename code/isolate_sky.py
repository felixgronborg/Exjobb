from PIL import Image
import glob
import pandas as pd
import numpy as np

def load_images(index_list = [], scale = 1):
    folder = glob.glob('../images/%.2f/*.png' % scale)
    im_list = []
    sky_percent = np.zeros(len(index_list))
    for filename in folder:
        for i in range(len(index_list)):
            if filename == '../images/%.2f\%d.png' % (scale, index_list[i]):
                im = np.asarray(Image.open(filename))
                im_list.append(im)
                print(filename, 'added to image list')

    d = {'image': im_list, 'amount of sky': sky_percent}

    df = pd.DataFrame(data=d, index=index_list)

    print(df)
    return df


def count_sky(im):
    count = 0
    total = 0
    newim = im.copy()
    newim.setflags(write=1)
    for i in range(0,np.shape(im)[0]):
        for j in range(0, np.shape(im)[1]):
            R = im[i,j,0]
            G = im[i,j,1]
            B = im[i,j,2]
            if(abs(int(R)-int(G))<5 and abs(int(G)-int(B)<5) and B>R and B>G and B>50):
                newim[i,j,:] = 0
                count += 1
                total += 1
            else:
                # newim[i,j,:] = im[i,j,:]
                total += 1
# if(abs(R-G)<5 and abs(G-B)<5 and B>R and B>G and B>50 and B<230)
    return newim, count/total

index_list = [17, 20, 21, 22, 23]
df = load_images(index_list, 0.5)

sky_list = []
for i in range(len(index_list)):
    [newim, percent] = (count_sky(df.iloc[i,0]))
    sky_list.append(newim)
    showthis = Image.fromarray(newim)
    showthis.show()
    print(percent)
