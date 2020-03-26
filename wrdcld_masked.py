import os
from os import path
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator

# Read text file
text = open('/home/lyrax/jworkspace/love.txt').read()

# Read mask image/ color image
#mask_im = np.array(Image.open(path))
im_coloring = np.array(Image.open('/home/lyrax/Pictures/Wallpapers/denise-chan-pXmbsF70ulM-unsplash.jpg'))

stopwords = set(STOPWORDS)

# Instantiate wordcloud object
wc = WordCloud(background_color="black", max_words=10000, mask=im_coloring, # can replace with mask_im
               stopwords=stopwords, contour_width=3, contour_color='steelblue',
               relative_scaling=0, max_font_size=500)

# Generate wordcloud
wc.generate(text)

# Create coloring from image
image_colors = ImageColorGenerator(im_coloring)

'''
# show normal plot
plt.imshow(wc, interpolation="bilinear")
plt.axis("off")
plt.figure()'''

# recolor wordcloud and show
plt.imshow(wc.recolor(color_func=image_colors), interpolation="bilinear")
plt.axis("off")

# Save figure
plt.savefig('/home/lyrax/Documents/lv.png', dpi=1000)
plt.show()

""" # Use this block for mask_im...
plt.imshow(wc, interpolation='bilinear')
plt.axis("off")
plt.figure()
plt.imshow(mask_im, cmap=plt.cm.gray, interpolation='bilinear')
plt.axis("off")
plt.show() """