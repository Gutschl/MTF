import matplotlib.pyplot as plt
import numpy as np
from scipy import stats
import scipy.misc
import os
from PIL import Image

def read_dir(path):
    direc = os.listdir(path)
    images = []
    for filename in direc:
        if (filename.split(".")[1] == "png"):
            img = scipy.misc.imread(os.path.join(path, filename), mode="I")
            #img = scipy.misc.toimage(img, low=0, high=4095, mode="I")
            #img = img.astype(np.uint16)
            images.append(img)
            #print(img.shape)
    images = np.asarray(images)

    return images

def do_mtf(mtf_images):
    mtf_images_crop=[]
    for image in mtf_images:
        mtf_images_crop.append (image[436:472,690:726])
        #print(mtf_images_crop.__sizeof__())


    std_mtf_images_crop = np.std(mtf_images_crop, axis=(1,2))

    return std_mtf_images_crop


images_f8_test = read_dir('mtf_f8')
print(images_f8_test[1])

images_f2 = read_dir('mtf_f2')
mtf_images_f2 = do_mtf(images_f2)
mtf_images_f2_y = mtf_images_f2/mtf_images_f2[0]

images_f4 = read_dir('mtf_f4')
mtf_images_f4 = do_mtf(images_f4)
mtf_images_f4_y = mtf_images_f4/mtf_images_f2[0]

images_f14 = read_dir('mtf_f14')
mtf_images_f14 = do_mtf(images_f14)
mtf_images_f14_y = mtf_images_f14/mtf_images_f2[0]

#images_f2 = read_dir('mtf_f2')
#mtf_images_f2 = do_mtf(images_f2)
#mtf_images_f2_y = mtf_images_f2/mtf_images_f2[0]

images_f8 = read_dir('mtf_f8')
mtf_images_f8 = do_mtf(images_f8)
mtf_images_f8_y = mtf_images_f8/mtf_images_f2[0]

images_f16 = read_dir('mtf_f16')
mtf_images_f16 = do_mtf(images_f16)
mtf_images_f16_y = mtf_images_f16/mtf_images_f2[0]



def crop(mtf_images):
    mtf_images_crop=[]
    for image in mtf_images:
        mtf_images_crop.append (image[436:472,690:726])

    return mtf_images_crop

#def std(mtf_images_crop):
 #   std_mtf_images_crop = np.std(mtf_images_crop, axis=(1,2))
#
 #   return std_mtf_images_crop

#mtf_images_f4 = read_dir("mtf_f4")
#mtf_images_f4_crop = crop(mtf_images_f4)
#std_mtf_images_f4_crop = std(mtf_images_f4_crop)
#std_mtf_images_f4_crop_y = std_mtf_images_f4_crop/std_mtf_images_f4_crop[0]



mtf_x = [10,16,25,32,50,100]
mtf_x2 = [10,16,25,32]

print(mtf_images_f4_y.shape)

print(mtf_images_f16_y)
mtf_test=[]
mtf_test = crop(images_f2)

plt.figure(0)
plt.imshow(mtf_test[3], cmap='Greys_r')
plt.figure(2)
plt.imshow(mtf_test[4], cmap='Greys_r')



#mtf_x = [10,16,25]

plt.figure(1)
plt.title("Modular Transfer Function")
plt.ylabel('Contrast')
plt.xlabel('lp/mm')
plt.plot(mtf_x,mtf_images_f14_y,'b--',label="Blende 1.4")
plt.plot(mtf_x,mtf_images_f2_y,'g--',label="Blende 2")
plt.plot(mtf_x,mtf_images_f4_y,'r^',label="Blende 4")
plt.plot(mtf_x2,mtf_images_f8_y,'y--',label="Blende 8")
plt.plot(mtf_x,mtf_images_f16_y,'k--',label="Blende 16")
plt.legend()






plt.show()







