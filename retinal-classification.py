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
from helper import makeDirectory, writeToOutputFile
import os
from skimage.io import imread
from skimage.transform import resize
import sys

#%%
def main():
    
    # Declare constants here
    TARGET_LOC = '../Target' # Path to the target folder which holds image data
    MODELS_LOC = '../models/model_binary' # Path to the models folder which holds the trained models
    IMG_HEIGHT = 400         # Defines the expected height of each image for the network
    IMG_WIDTH = 600          # Defines the expected width for each image for the network
    
    target_names = list()    # Used to store all of the outputs for the images
    target_img = list()      # Holds the actual data of the images
    predictions = list()     # Holds all of the final predictions
    
    # Load in the model / models here
    print("[+] Loading model")
    model = keras.models.load_model(MODELS_LOC, compile=True)
    
    print("[+] Getting images from target folder")
    
    # Get each image from folder, format it, and run it thorugh the network
    for img_path in os.listdir(TARGET_LOC):
        
        path = os.path.join(TARGET_LOC, img_path)       # Get the path to the image
        img = imread(path)                              # Load the image
        img = resize(img, (IMG_HEIGHT, IMG_WIDTH, 3))   # Resize the image
        target_img.append(img)                          # Append the img to the target image list
        target_names.append(img_path.split('.')[0])     # Add the image name to names list for output
        
    # Cast image data as a numpy array
    X = np.array(target_img)
    #print(X[1].shape) 
    # Print some output for the user
    print("[+] {0} target images found".format(len(X)))
    
    # Check length of the images. If 0 return error
    if len(X) == 0:
        print("[!] make sure that all of the images you want to evaluate are in the target folder")
        print("[!] Exiting program...")
        sys.exit("Must be at least 1 image in the target folder")
    else:
        print("[+] Running images through model...")
       
    # Make model predictions and output to the user
    print("\n----------Model Predictions:----------\n")
    
    # Run all of the images through the model
    pred = model.predict(X)
    # Go through each image and make a prediction
    for i in range(len(pred)):
        # Get the name of the image and the prediction value
        name = target_names[i]
        p = pred[i]
        # Print out some output for the user
        print("Image Name: {0}".format(name), end=' => ')
        print("Prediction: {0}".format(p))
    
    # Ask user if they want to save the output to file
    print("\n----------Evaluation complete----------")
    
    ans = input("Would you like to save output to file? ( y / n ): ")
    
    while(ans.lower() not in ['y', 'n']):
        print("[!] Input must be 'y' or 'n'. Try again.")
        ans = input("Would you like to save output to file? ( y / n ): ")
        
    if(ans.lower() == 'y'):
        print("\n[+] Output will be saved to the evaluation folder")
        
        # Create the directory
        path = makeDirectory()
        print("[+] Output files created at {0}".format(path))
        
        print("[+] Writing evaluation to file...")
        # Write the output to the created file
        writeToOutputFile(path, pred)
        print("[+] Completed")
    
        
    print("[+] Closing Program...")


y#%%
if __name__ == '__main__':
    main()