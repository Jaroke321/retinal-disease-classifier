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
    IMG_HEIGHT = 400         # Defines the expected height of each image for the network
    IMG_WIDTH = 600          # Defines the expected width for each image for the network
    target_names = list()    # Used to store all of the outputs for the images
    target_img = list()      # Holds the actual data of the images
    predictions = list()     # Holds all of the final predictions
    
    print("[+] Getting target images from target folder")
    
    # Get each image from folder, format it, and run it thorugh the network
    for img_path in os.listdir(TARGET_LOC):
        
        path = os.path.join(TARGET_LOC, img_path)       # Get the path to the image
        img = imread(path)                              # Load the image
        img = resize(img, (IMG_HEIGHT, IMG_WIDTH, 3))   # Resize the image
        target_img.append(img)                          # Append the img to the target image list
        target_names.append(img_path.split('.')[0])     # Add the image name to names list for output
        
    # Cast image data as a numpy array
    X = np.array(target_img)
      
    # Print some output for the user
    print("Done...")
    print("[+] {0} target images found".format(len(X)))
    
    # Check length of the images. If 0 return error
    if len(X) == 0:
        print("[!] make sure that all of the images you want to evaluate are in the target folder")
        print("[!] Exiting program...")
        sys.exit("Must be at least 1 image in the target folder")
    else:
        print("[+] Running images through network...")
       
    # Make model predictions and output to the user
    print("\n----------Model Predictions:----------\n")
    # Run each image through the network to get a prediction
    for i in range(len(X)):
        
        # Make the prediction
        pred = 0  # TODO: Import the model at the beginning of the file and make predictions here
            
        print("Image Name: {0}".format(target_names))
        print("Prediction: {0}\n".format(pred))
        
        # Add the prediction to the predictions list
        predictions.append(pred)
    
    # Ask user if they want to save the output to file
    print("----------Evaluation complete----------\n")
    
    ans = input("Would you like to save output to file? ( y / n ): ")
    
    while(ans.lower() not in ['y', 'n']):
        print("[!] Input must be 'y' or 'n'. Try again.")
        ans = input("Would you like to save output to file? ( y / n ): ")
        
    if(ans.lower() == 'y'):
        print("[+] Saving to the evaluation folder")
        
        # Create the directory
        path = makeDirectory()
        print("[+] Output directory created at {0}".format(path))
        
        print("[+] Writing evaluation to file...")
        # Write the output to the created file
        writeToOutputFile(path, predictions)
        print("[+] Done")
        
    else:
        print("[+] Closing Program...")

if __name__ == '__main__':
    main()