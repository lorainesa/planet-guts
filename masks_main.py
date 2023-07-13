import numpy as np
import astropy.io.fits as pyfits
from masks_functs import *
from design_class import *

def main(nholes, hrad): 
    while 1: # keep looping until we get a valid design
        my_design = design(nholes, hrad) # initialize design object
        rng = np.random.default_rng(seed=None) # set random number generator
        aperture = pyfits.getdata('/Users/kenzie/Desktop/CodeAstro/planet-guts/keck_aperture.fits') # set Keck primary aperture
        for i in range(nholes): # keep adding and checking a single hole until it's acceptable
            my_design.xy_coords[i] = add_hole(hrad, rng, aperture)

        my_design.get_uvs() # calculate design uv coordinates

        rcheck = check_redundancy(my_design)  # check design for redundancy
        if rcheck == 1: # if true, there's some redundancy and we need to start over
            print("Uh-oh, mask has redundancies! Trying again...")
        if rcheck == 0: # if this statement is true, exit the loop and return our final design!
            print("Yay! Mask design is non-redundant. Plotting design...")
            #print(my_design.xy_coords)
            plot_design(my_design, aperture)
            return my_design