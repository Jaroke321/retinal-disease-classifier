# -*- coding: utf-8 -*-
"""
Created on Wed Sep  1 17:18:11 2021

@author: Jacob
"""

#%%
from datetime import datetime
from PIL import Image
import os

#%%

def makeDirectory():
    '''The function will create a directory to store results from the retinal 
    classification. The path name is based on today's date and uses the datetime 
    format '%A-%m-%Y'. If this path already exists under the evaluation folder, then
    a new path will be created with a simple incrementer appended to the end of the path. 
    For example, '../evaluation/Tuesday-09-2021_1' '''
    
    # Get the current datetime to name file
    time = datetime.now()
    time_str = time.strftime("%A-%m-%Y")
        
    # Create the path for the final evaluation 
    dir_name = os.getcwd()[:-3]
    a = os.path.join(dir_name, 'evaluation')
    b = os.path.join(a, time_str)
    
    # Create the final directory and return the path
    valid_path = False
    ext = 1
    # Loop until a valid path is found
    while not valid_path:
        
        try:
            os.mkdir(b)         # Attempt to create the directory
            valid_path = True   # Escape the loop
        except FileExistsError as e:
            # Append ext to the end of b to make a new path and try making the path again
            s = "_{0}".format(ext)
            b += s
            ext += 1
    
    return b  # Return the final path that was created


def writeToOutputFile(path, predictions):
    '''This function will take the path to the output folder created by makeDirectory 
    and the final predictions for those images, and write them to output files for readability 
    for the user.'''
    
    TARGET_LOC = '../Target' # Path to the target folder which holds image data
    # Create the directory to the images file where all of the images will be stored
    image_dir = os.path.join(path, 'images')
    os.mkdir(image_dir)
    
    # reread all of the images from the target folder so that the original resolution is maintained
    for file_path in os.listdir(TARGET_LOC):
        
        tar_path = os.path.join(TARGET_LOC, file_path)  # Get the path from the target folder
        image = Image.open(tar_path)                    # Load full resolution image
        # Get the new location to save the file
        new_loc = os.path.join(image_dir, file_path)
        img = image.save(new_loc)  # Save the full res image to the new images folder
        
        # Write the predictions for the images into a txt file
    
    