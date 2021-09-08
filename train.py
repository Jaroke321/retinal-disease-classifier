# -*- coding: utf-8 -*-
"""
Created on Wed Sep  8 08:59:04 2021

@author: Jacob
"""

import numpy as np
import pandas as pd
from keras.models import Sequential
from keras.layers import Dense, Conv2D, Flatten
import os
from skimage.io import imread 
from skimage.transform import resize


#%%

IMG_HEIGHT = 400   # Define the constant for image height that will be used for the network
IMG_WIDTH = 600    # Define the constant for image width that will be used for the network

# Define all of the paths to the images here
PATH_TO_TRAIN = '../data/Training_Set/Training_Set/Training'
PATH_TO_VAL = '../data/Evaluation_Set/Evaluation_Set/Validation'
PATH_TO_TEST = '../data/Test_Set/Test_Set/Test'

def getData(directory):
    
    count = 0
    data = list()  # Python list to store the data in
    
    # Go through each file in the directory
    for i in range(len(os.listdir(directory))):
        
        file_name = '{0}.png'.format(i+1)
        img_path = os.path.join(directory, file_name)      # Get the path for the image file
        img = imread(img_path)                             # Open the image and make it into a numpy array
        img = resize(img, (IMG_HEIGHT, IMG_WIDTH, 3))      # Resize the image based on the height and width defined above

        data.append(img)                                   # Append the image to the array
        
        count += 1
        if (count % 50) == 0:
            progress = (count / len(os.listdir(directory))) * 100
            data_name = directory.split('/')[-1]
            print("{:.2f}% completed loading {} data".format(progress, data_name))
        
    return data

def createModel():
    '''Used to create a CNN model based on the RFMiD Dataset'''
    
    # Instantiate the model
    model = Sequential()
    
    # TODO: Add layers to the model
    
    # Return the model
    return model

#%%

def main():
    '''This function will be the main driver function to train/ retrain the retinal 
    classification model.'''
    
    # Get all of the paths for the images in the data folder
    training_data = np.array(getData(PATH_TO_TRAIN))
    validation_data = np.array(getData(PATH_TO_VAL))
    testing_data = np.array(getData(PATH_TO_TEST))

    # Load in the labels data into pandas DF
    training_labels = pd.read_csv('../data/Training_Set/Training_Set/RFMiD_Training_Labels.csv')
    validation_labels = pd.read_csv('../data/Evaluation_Set/Evaluation_Set/RFMiD_Validation_Labels.csv')
    test_labels = pd.read_csv('../data/Test_Set/Test_Set/RFMiD_Testing_labels.csv')
    
    # Make the labels only the binary disease columns
    y_train = training_labels.Disease_Risk.values.astype('float32')
    y_val = validation_labels.Disease_Risk.values.astype('float32')
    y_test = test_labels.Disease_Risk.values.astype('float32')


#%%
if __name__ == '__main__':
    
    # Ask user to proceed
    userInput = input("[!] Running this file will retrain existing models, replacing them. Do you want to proceed? (y / n): ")
    valid = False # Used to get valid input from the user
    
    # Loop until the user input is valid
    while not valid:
        
        if(userInput.lower() in ['y', 'n']):
            
            # Train new model if the user enters y
            if(userInput.lower() == 'y'):
                main()
            else:
                print("Models will not be retrained\nExiting Program...")
        else:
            print("[!] Invalid input. Must be Y, y, N, or n...")