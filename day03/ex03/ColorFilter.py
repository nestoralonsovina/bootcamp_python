import numpy as np 


class ColorFiter:
    @staticmethod
    def invert(array):
        """ Takes a NumPy array of an image as an argument and returns an array with inverted color. """
        print(array.shape)
        for x in range(len(array)):
            for y in range(len(array[0])):
                array[x][y][0] = 255 - array[x][y][0] 
                array[x][y][1] = 255 - array[x][y][1]
                array[x][y][2] = 255 - array[x][y][2]
        return array
