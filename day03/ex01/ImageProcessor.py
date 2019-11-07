from matplotlib import (
    image,
    pyplot as plt
)
import numpy as np


class ImageProcessor:

    def load(self, path):
        """ 
            path -> .png file to open
            return -> array with the RGB values of the image pixels

            It must display a message specifying the dimensions of the image
        """
        arr = image.imread(path)
        print(f"Loading image of dimensions {len(arr[0])} x {len(arr)}")
        return arr 
    
    def display(self, array):
        """
            array -> numpy array
            displays RGB image
        """
        plt.imshow(array)
        plt.show()

    