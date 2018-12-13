import os
import skimage
import numpy
import PIL
from skimage import io, data, filters
from scipy import misc


import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

from skimage import data
from skimage.filters import threshold_otsu
from skimage.segmentation import clear_border
from skimage.measure import label, regionprops
from skimage.morphology import closing, square
from skimage.color import label2rgb

file = os.path.join(skimage.data_dir, 'large.png')
I = numpy.asarray(PIL.Image.open(file))
im = misc.imread(file, flatten=True)

#image = data.coins()[50:-50, 50:-50]
image = im

# apply threshold
thresh = threshold_otsu(image)
bw = closing(image > thresh, square(3))

# remove artifacts connected to image border
cleared = clear_border(bw)

# label image regions
label_image = label(cleared)
image_label_overlay = label2rgb(label_image, image=image)

fig, ax = plt.subplots(figsize=(100, 60))
ax.imshow(image_label_overlay)

for region in regionprops(label_image):
    # take regions with large enough areas
    if region.area >= 10:
        # draw rectangle around segmented coins
        minr, minc, maxr, maxc = region.bbox
        rect = mpatches.Rectangle((minc, minr), maxc - minc, maxr - minr,
                                  fill=False, edgecolor='red', linewidth=2)
        ax.add_patch(rect)

ax.set_axis_off()
plt.tight_layout()
plt.show()






'''
# way to load car image from file
file = os.path.join(skimage.data_dir, 'large.png')
I = numpy.asarray(PIL.Image.open(file))
im = misc.imread(file, flatten=True)

edges = filters.sobel(im)
# way to show the input image
io.imshow(edges)
io.show()
'''