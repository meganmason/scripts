# gdal_translate -of AAIGrid rescaled_20170604.tif ascii_lidar/rescaled_20170604.asc
#
# gdal_translate -of XYZ rescaled_20170604.tif ascii_lidar/rescaled_20170604.asc
#
# gdal_translate -of netCDF rescaled_20170604.tif ascii_lidar/rescaled_20170604.nc

# 5-1-2019
#convert rescaled lidar tifs to rescaled netCDF (.nc)

import subprocess as sp
import glob
import os
import sys


path = '/home/meganmason/Documents/projects/thesis/data/processing_lidar/depths_3m/all_rescaled/'


for filepath in sorted(glob.glob(os.path.join(path, '*.tif'))):
    dir = os.path.dirname(filepath)
    # print(dir)
    dt_str = filepath.split("/")[-1] #splits on / and saves the last one
    dt_str = "".join([c for c in dt_str if c.isnumeric()]) #grabs numeric values
    out_fname = dir + '/nc_lidar/rescaled_' + dt_str + '.nc'
  # out_fname = test.nc
    sp.check_output("gdal_translate -of netCDF {} {}".format(filepath, out_fname), shell=True) #goes to command line, since gdal wont work in virtual env


    # sys.exit() #one way to run single item in for loop
