# from scipy.misc import lena
from pylab import imread
from scipy.ndimage import gaussian_filter
from stl_tools import numpy2stl, text2png
import os
import cv2
import time
import shutil

# run in an anaconda base environment
"python C:\Repositories\3dPython\stl_tools\STL_pat.py"
"""
Some quick examples
"""

# A = lena()  # load Lena image, shrink in half
# A = gaussian_filter(A, 1)  # smoothing
# numpy2stl(A, "examples/Lena.stl", scale=0.1, solid=False)
folder = r"/mnt/c/Users/patri/Pictures/BlackAndWhite/Corners-Halloween/"


def preprocess(file, optionThreshold):
    """ Convert to black and white"""
    im = cv2.imread(file)
    grayfileName = f"{os.path.splitext(file)[0]}new.png"
    grayImage = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
    (thresh, blackAndWhiteImage) = cv2.threshold(grayImage, optionThreshold, 255, cv2.THRESH_BINARY_INV)
    # f"{os.path.splitext(file)[0]}.stl"
    	
    cv2.imwrite(f"/mnt/c/Users/patri/Pictures/BlackAndWhite/Glow/bw{optionThreshold}.png", blackAndWhiteImage)c
    return blackAndWhiteImage
    
# Option_array = [5, 15, 25, 35, 45, 55, 65, 75, 85, 100, 105, 110, 115, 120, 125, 130, 135, 140, 145, 150, 155]
Option_array=[110]

for file in os.listdir(folder): 
    print(file)
    if "png" in file: 

        print(file, os.path.splitext(file))
        pngfileName = file
        stlfileName = f"{os.path.splitext(file)[0]}.stl"
        print(stlfileName)
        pngfilePath= os.path.join(folder, pngfileName)
        stlfilePath = os.path.join(folder, stlfileName)
        for item in Option_array: 
            BWImage = preprocess(pngfilePath, int(item))
        try:
            shutil.rmtree(stlfilePath)
        except:
            print("stl doesn't exist")
        numpy2stl(BWImage, stlfilePath, min_thickness_percent=0.00, scale=0.035, mask_val=0., solid=True)
