# Naive red traffic light detection algorithm using only numpy.

# data
Images of size (640, 480)

# Algorithms
1. "Catch all": Draw a big box on the entire top-half of the image, as that is where
    traffic lights tend to be.
2. "Box if there is red": Iterate pixel by pixel. If the red channel is above a minimum threshold, and the green and blue values are within a predetermined range, enclose the surrounding area by a bounding box. Its hyperparameters are
    a.	Dimensions of predicted bounding box: (hand-picked based on trial and error so that predictions appeared of correct dimension. I take advantage of the fact of the little variability of size of red traffic lights, since most images were shot from a similar position)
    b.	Color thresholds: We sampled four images with red traffic lights at random, used imagecolorpicker.com to find the RGB value of red traffic lights, and set the minimum red to the smallest “R” value of the four, and the ranges of the “G” and “B” such that all values were within the range.
