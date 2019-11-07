import numpy as np

class ScrapBooker:
    @staticmethod
    def crop(array, dimensions, position = (0, 0)):
        """
            array -> numpy array
            dimensions -> dimensions of the crop
            position -> cordinates of top left corner for the crop
            return cropped array 
        """
        Y = 0
        X = 1

        if dimensions[Y] > len(array) or dimensions[X] > len(array[0]):
            raise ValueError('dimensions out of bounds')

        return array[position[Y]:position[Y] + dimensions[Y], position[X]:position[X] + dimensions[X], :]
    
    @staticmethod
    def thin(array, n, axis):
        """
            delete every n-th pixel row along the specified axis ( 0 vertical 1 horizontal)
        """
        return np.delete(array, range(n, len(array), n), axis)

    @staticmethod
    def juxtapose(array, n, axis):
        """
            juxtapose n copies of the image along the specified axis (0 vertical, 1 horizontal).
        """

        orig_arr = array

        for _ in range(n):
            array = np.concatenate((array, orig_arr), axis=axis)
        
        return array
