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



mtf_images = read_dir("mtf_f4")
#print(mtf_images)


mtf_images_crop=[]
for image in mtf_images:
    mtf_images_crop.append (image[436:472,690:726])

print((mtf_images_crop))
std_mtf_images = np.std(mtf_images_crop,axis=(1,2))

std_mtf_images_y = std_mtf_images/std_mtf_images[0]
#plt.imshow(std_mtf_images_y[0])

plt.figure(0)
plt.imshow(mtf_images_crop[0],cmap='Greys_r')


mtf_x = [10,16,25,32,50,100]
#mtf_x = [10,16,25]

plt.figure(1)
plt.title("Modular Transfer Function")
plt.ylabel('Contrast')
plt.xlabel('lp/mm')
plt.plot(mtf_x,std_mtf_images_y,'x')

plt.show()







