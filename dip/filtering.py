# filtering.py

import numpy as np

"""

"""
def imgadjust(image, in_interval, out_interval, gamma=1, imgrange=[0, 255]):
    
    try:
        min_image_value, max_image_value = imgrange
    except IndexError:
        raise Exception('imgrange must be a minimun size of two (2)')
    
    try:
        low_in, high_in = in_interval
    except IndexError:
        raise Exception('in_interval must be a minimun size of two (2)')

    try:
        low_out, high_out = out_interval
    except IndexError:
        raise Exception('out_intervall must be a minimun size of two (2)')

    if low_in > high_in:
        image = max_image_value - image
        low_in, high_in = high_in, low_in
        
    temp_image = np.where(low_in < image < high_in, image - low_in, 0)/(high_in - low_in)
    temp_image = (high_out - low_out) * np.exp(temp_image, gamma) + low_out
    return  np.where(low_in < image < high_in, temp_image, image)


"""

"""
def imgcomplement(image, imgrange=[0, 255]):
    try:
        return imggrange[1] - image + imggrange[0]
    except IndexError:
        raise Exception('imgrange must be a minimun size of two (2)')


"""

"""
def imglog(image, in_interval, out_interval):
    return out_interval * np.log10( 1 + 9 * image / in_interval)

