import numpy as np

class NumPyCreator:
    @staticmethod
    def from_list(lst, dtype = None):
        """ Takes in a list and returns its corresponding NumPy array """
        return np.array(lst, dtype=dtype)
    

    @staticmethod
    def from_tuple(tpl, dtype = None):
        """ takes in a tuple and returns its corresponding NumPy array """
        return np.array(lst, dtype=dtype)


    @staticmethod
    def from_iterable(itr, dtype = None):
        """ takes in an iterable and returns an array which contains all of its elements. """
        return np.array(itr, dtype=dtype)


    @staticmethod
    def from_shape(shape, value, dtype = None):
        """ returns an array filled with the same value 
            shape -> tuple that specifies the shape of the aray
            value -> int that specifies the value inside the array
        """
        return np.full(shape, value, dtype=dtype)
    

    def random(shape, dtype = None):
        """ returns an array filled with random values
            shape -> tuple that specifies the shape of the aray
        """
        return np.random.rand(shape, dtype=dtype)
    

    def identity(n, dtype = None):
        """ return an array representing the identity matrix of size n """
        return np.identity(n, dtype=dtype)


    
