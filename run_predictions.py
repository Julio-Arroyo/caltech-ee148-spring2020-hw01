import os
import numpy as np
import json
from PIL import Image


ALGO = 'find_red'  # 'find_red', 'catch_all'


# Algorithms
def catch_all(I):
    margin = 2
    return [[margin, margin, 240 - margin, 640 - margin]]


def find_red(I):
    '''
    4 random images used to find tones of red: {213, 291, 251, }
    '''
    # red_tones = {(253,217,113), (240,67,97), (255,242,96), (253,168,113), }

    bboxes = []

    x_offset = 8
    y_offset = 6

    i = 0
    j = 0
    min_red = 235
    min_blue = 95
    max_blue = 115
    min_green = 65
    max_green = 245
    
    # use while loops instead of for loops to jump around image, sorry i know it's ugly
    while j < I.shape[1]:
        i = 0
        while i < 3 * (I.shape[0] // 5):  # look at top three-fifths of image only
            if (I[i, j, 0] > min_red
                and I[i, j, 1] > min_green and I[i, j, 1] < max_green
                and I[i, j, 2] > min_blue and I[i, j, 2] < max_blue):
                bboxes.append([j-x_offset+2, i-y_offset, j+x_offset+2, i+y_offset])
                i = I.shape[0] - 2
                j += 20
            i += 1
        j += 1
    
    return bboxes


def detect_red_light(I):
    '''
    This function takes a numpy array <I> and returns a list <bounding_boxes>.
    The list <bounding_boxes> should have one element for each red light in the 
    image. Each element of <bounding_boxes> should itself be a list, containing 
    four integers that specify a bounding box: the row and column index of the 
    top left corner and the row and column index of the bottom right corner (in
    that order). See the code below for an example.
    
    Note that PIL loads images in RGB order, so:
    I[:,:,0] is the red channel
    I[:,:,1] is the green channel
    I[:,:,2] is the blue channel
    '''
    algos = {'find_red': find_red, 'catch_all': catch_all}

    return algos[ALGO](I)

# set the path to the downloaded data: 
data_path = 'data/RedLights2011_Medium'

# set a path for saving predictions: 
preds_path = f'data/hw01_preds/{ALGO}' 
os.makedirs(preds_path,exist_ok=True) # create directory if needed 

# get sorted list of files: 
file_names = sorted(os.listdir(data_path)) 

# remove any non-JPEG files: 
file_names = [f for f in file_names if '.jpg' in f] 

preds = {}
for i in range(len(file_names)):
# for i in range(324, 334, 1):
    if i % 50 == 0:
        print(f'Image #{i}')

    # read image using PIL:
    I = Image.open(os.path.join(data_path,file_names[i]))

    # convert to numpy array:
    I = np.asarray(I)
    
    preds[file_names[i]] = detect_red_light(I)

# save preds (overwrites any previous predictions!)
with open(os.path.join(preds_path,'preds.json'),'w') as f:
    json.dump(preds,f)
