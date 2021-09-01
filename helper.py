# -*- coding: utf-8 -*-
"""
Created on Wed Sep  1 17:18:11 2021

@author: Jacob
"""

import os
import numpy as np
from PIL import Image

def getData(directory, height, width):
    
    data = list()  # Python list to store the data in
    # Go through each file in the directory
    for file in os.listdir(directory):
        
        img_path = os.path.join(directory, file)           # Get the path for the image file
        img = np.array(Image.open(img_path))               # Open the image and make it into a numpy array
        img = np.resize(img, (height, width, 3))   # Resize the image based on the height and width defined above
        img = img.astype('float32')                        # Cast each pixel as a float
        img /= 255                                         # Normalize the data so that it is between 0 - 1
        data.append(img)                                   # Append the image to the array
        
    return data