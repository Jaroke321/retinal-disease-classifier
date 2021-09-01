# -*- coding: utf-8 -*-
"""
Created on Wed Sep  1 15:17:14 2021

@author: Jacob
"""

import numpy as np
import pandas as pd
import keras
import matplotlib.image as mpimg
from matplotlib import pyplot as plt
from helper import getData
from PIL import Image
import os

#%%

# Define constants to be used here
IMG_HEIGHT = 200 # Defines the image height that is desired for input of the network
IMG_WIDTH = 200  # Defines the image width that is desired for the input to the network

# Get all of the paths for the images in the data folder
training_data = np.array(getData('data/Training_Set/Training_Set/Training', IMG_HEIGHT, IMG_WIDTH))
validation_data = np.array(getData('data/Evaluation_Set/Evaluation_Set/Validation', IMG_HEIGHT, IMG_WIDTH))
testing_data = np.array(getData('data/Test_Set/Test_Set/Test', IMG_HEIGHT, IMG_WIDTH))

# Load in the labels data into pandas DF
training_labels = pd.read_csv('data/Training_Set/Training_Set/RFMiD_Training_Labels.csv')
validation_labels = pd.read_csv('data/Evaluation_Set/Evaluation_Set/RFMiD_Validation_Labels.csv')
test_labels = pd.read_csv('data/Test_Set/Test_Set/RFMiD_Testing_labels.csv')

#%%

# Use the training location to print a few photos for reference
training_loc = 'data/Training_Set/Training_Set/Training/{0}.png'

plt.figure(figsize=(20,20))
# Look at a few of the images before reading and normalizing them using the training data
for i in range(6):
    loc = training_loc.format(i+1)
    img = Image.open(loc)
    img.thumbnail((IMG_HEIGHT, IMG_WIDTH), Image.ANTIALIAS)  # Resizes the image to the size defined above
    ax = plt.subplot(3, 2, i+1)
    ax.title.set_text("{0}.png".format(i+1))
    plt.imshow(img)
#%%

def main():
    print('hello')

if __name__ == '__main__':
    main()