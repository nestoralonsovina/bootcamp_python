from ex01.ImageProcessor import ImageProcessor
from ex02.ScrapBooker import ScrapBooker
from ex03.ColorFilter import ColorFiter

imp = ImageProcessor()
arr = imp.load('ex01/nalonso.png')
arr = ColorFiter.invert(arr)
imp.display(arr)