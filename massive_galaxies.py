import numpy as np
import matplotlib.pyplot as plt
import os
# import astropy
# from astropy.io import fits
from astropy.io import fits as pyfits
# import pandas as pd
from astropy.table import Table
from astropy.coordinates import search_around_sky
# from astropy.cosmology import FlatLambdaCDM
# import astropy.units as u
# import scipy.integrate as integrate
# import random
# from astropy.visualization import astropy_mpl_style
# plt.style.use(astropy_mpl_style)
from astropy.utils.data import get_pkg_data_filename
# from astropy.wcs import WCS
# from astropy.table import Table
# from astropy.convolution import convolve, Box1DKernel
# import glob
# import csv
# from scipy import interpolate
# from astropy import cosmology

# given a galaxy's galactic coordiantes, find its nearest massive galaxy neighbor
# define a large galaxy as M > 10^10 solar masses
# need to calculate distances between my kcwi galaxy and those from the sloan catalog
# using the RA and Dec... need some trig equation or python function


# main working directory
kcwireducdirect= "/Users/lorainealexis/KCWI_DRP"




# read in your KCWI catalog
kcwisourcesz= kcwireducdirect + "/skysub_reduc/kcwisources_z.txt"

sourcename_kcwi=np.genfromtxt(kcwisourcesz, delimiter='\t\t\t', dtype='str', skip_header=1, usecols=0)
bfz_kcwi=       np.genfromtxt(kcwisourcesz, delimiter='\t\t\t', dtype='str', skip_header=1, usecols=1)
ra_kcwi=        np.genfromtxt(kcwisourcesz, delimiter='\t\t\t', dtype='str', skip_header=1, usecols=3)
dec_kcwi=       np.genfromtxt(kcwisourcesz, delimiter='\t\t\t', dtype='str', skip_header=1, usecols=4)




# sloan catalog: /Users/lorainealexis/KCWI_DRP/nsa_v0_1_2.fits
catalog= kcwireducdirect + '/nsa_v0_1_2.fits'
print("catalog to be used: ", catalog, "\n")


# get the data from the catalog
catalog_data= pyfits.getdata(catalog, 1)
# Table.read(catalog_data)

#catalog_file = get_pkg_data_filename('/Users/lorainealexis/KCWI_DRP/nsa_v0_1_2.fits')
#catalog_file = get_pkg_data_filename('/Users/lorainealexis/KCWI_DRP', package='nsa_v0_1_2.fits')
# hdu = fits.open(catalog_file)[1]
# catalog_data = hdu.data

# # work with the following keywords
# # catalog_data["IAUNAME"] : galaxy name
# # catalog_data["MASS"] : galaxy mass
# # catalog_data["RA"] : right ascencion
# # catalog_data["DEC"] : declination
# # catalog_data["ZSDSSLINE"] : redshift estimated from emission lines

# # np.stack((catalog_data["IAUNAME"], catalog_data["ZSDSSLINE"], catalog_data["RA"], catalog_data["DEC"], catalog_data["MASS"]),axis=-1)


# # galaxies with redshifts less than 0.02 and with mass larger than 10^10 solar masses
# inds=np.where((catalog_data["ZSDSSLINE"] < 0.02) & (catalog_data["MASS"] > 10**10))[0]
# print(inds.shape)
# inds_zm=inds[:]


# galaxies with mass larger than 10^10 solar masses
inds_m=np.where((catalog_data["MASS"] > 10**10))[0]
print(inds_m.shape)
inds_mass=inds_m[:]


sourcename_sloan=catalog_data["IAUNAME"][inds_mass]
bfz_sloan=catalog_data["ZSDSSLINE"][inds_mass]
ra_sloan=catalog_data["RA"][inds_mass]
dec_sloan=catalog_data["DEC"][inds_mass]
mass_sloan=catalog_data["MASS"][inds_mass]


# NASA-Sloan sources that fit my criterion
sloansources= np.stack((sourcename_sloan, bfz_sloan, mass_sloan, ra_sloan, dec_sloan),axis=-1)

print('right ascension')
print(ra_sloan)

# print(sloansources)
# print('testing')
# print(mass_sloan[mass_sloan < 10**10])


# I think I need to be looking for galaxies within pm 0.01 
# of the redshift of a given KCWI galaxy

nearby_galaxies=[]

for i,redshift in enumerate(bfz_kcwi):
    maxz= float(redshift) + 0.005
    minz= float(redshift) - 0.005


    temp=np.where((bfz_sloan > minz) & (bfz_sloan < maxz))[0]
    sloan_ind=temp[:]

    nearby_galaxies.append(sloan_ind)


print(len(nearby_galaxies[2]))


# calculate the distance between the two galaxies???


#astropy.coordinates.search_around_sky






