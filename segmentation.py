#!/usr/bin/env python
# coding: utf-8

# In[4]:


import numpy as np
import cv2

src = cv2.imread('Image Export-01_s4.jpg')

#percent by which the image is resized
scale_percent = 25

#calculate the 50 percent of original dimensions
width = int(src.shape[1] * scale_percent / 100)
height = int(src.shape[0] * scale_percent / 100)

# dsize
dsize = (width, height)

# resize image
output = cv2.resize(src, dsize)
cv2.imshow('Corner', output)

cv2.imwrite('C:/Users/enas8/Desktop/Test_gray.jpg', output)
cv2.waitKey(0)
cv2.destroyAllWindows()


# In[5]:


import numpy as np
import cv2

kernel = np.ones((5,5),np.uint8)
erosion = cv2.erode(output, kernel, iterations=1)
cv2.imshow('Corner', erosion)
cv2.imwrite('C:/Users/enas8/Desktop/after_gray.jpg', erosion)
cv2.waitKey(0)
cv2.destroyAllWindows()


# In[ ]:




