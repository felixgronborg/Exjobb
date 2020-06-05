import cv2
import numpy as np

class Pixel:
    def __init__(self, x_coord, y_coord):
        self.x_coord = x_coord
        self.y_coord = y_coord
    
    def clump(self):
        Clumps().add_pixel(pixel=self)

class Clump:

    def __init__(self, pixel):
        self.coord_list = []
        self.coord_list.append(pixel)
        self.min_x = pixel.x_coord - 5
        self.max_x = pixel.x_coord + 5
        self.min_y = pixel.y_coord - 5
        self.max_y = pixel.y_coord + 5
        self.size = 1

    def add_pixel(self, pixel):
        self.coord_list.append(pixel)
        self.size += 1
        if(pixel.x_coord < self.min_x + 5):
            self.min_x = pixel.x_coord - 5 
        if(pixel.x_coord > self.max_x - 5):
            self.max_x = pixel.x_coord + 5
        if(pixel.y_coord < self.min_y + 5):
            self.min_y = pixel.y_coord - 5
        if(pixel.y_coord > self.max_y - 5):
            self.max_y = pixel.y_coord + 5

class Clumps:
    clump_list = []    

    def add_pixel(self,pixel):
        for clump in self.clump_list:
            if(pixel.x_coord < clump.max_x and pixel.x_coord > clump.min_x and pixel.y_coord < clump.max_y and pixel.y_coord > clump.min_y):
                clump.add_pixel(pixel)
                return
            # for p in clump.coord_list:
            #     if (abs(pixel.x_coord-p.x_coord) <= 5) and (abs(pixel.y_coord-p.y_coord) <= 5):
            #         clump.add_pixel(pixel)
            #         return
        new_clump = Clump(pixel)
        self.clump_list.append(new_clump)

def is_overexposed(in_img):
    out_im = in_img.copy()
    c = Clumps()
    if(len(in_img.shape) == 3):
        img = cv2.cvtColor(in_img, cv2.COLOR_BGR2GRAY)
        white_list = []
    elif(len(in_img.shape) == 2):
        img = in_img
    else:
        print('The image needs to be 2- or 3-Dimensional')
        return None
    thresh = img.shape[0] * img.shape[1] * 1
    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            if(img[i,j] == 255):
                p = Pixel(i,j)
                c.add_pixel(p)
            else:
                img[i,j] = 0

    for clump in c.clump_list: # Fungerar inte som jag vill
        print(clump.size)
        xmin = clump.min_x
        xmax = clump.max_x
        ymin = clump.min_y
        ymax = clump.max_y
        for i in range(xmin, xmax):
            out_im[i,ymin,:] = 0
            out_im[i,ymin,2] = 255
            out_im[i,ymax,:] = 0
            out_im[i,ymax,2] = 255
        for i in range(ymin, ymax):
            out_im[xmin,i,:] = 0
            out_im[xmin,i,2] = 255
            out_im[xmax,i,:] = 0
            out_im[xmax,i,2] = 255
        
            

    print(len(c.clump_list))
    cv2.imshow('img', out_im)
    cv2.waitKey(0)
    # percent = 100*len(white_list)/(img.shape[0]*img.shape[1])
    # print('%.2f percent of the image is completely white' % percent)
    # cv2.imshow('%.2f percent of the image is completely white' % percent, img)
    # cv2.waitKey(0)