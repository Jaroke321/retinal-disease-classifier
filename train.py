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

def main():
    '''This function will be the main driver function to train/ retrain the retinal 
    classification model.'''


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