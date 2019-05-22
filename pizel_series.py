# ~~~~~~~~~~~~~~~~~~~~   import packages  ~~~~~~~~~~~~~~~~~~~
import os
import glob
from netCDF4 import Dataset
import numpy as np
from matplotlib import pyplot as plt
# ~~~~~~~~~~~~~~~~~~~~   functions  ~~~~~~~~~~~~~~~~~~~~~~~~~
#select pixel
def get_closest(arr,pt):
    idx = np.argmin(np.abs(arr-pt)) #indexs location
    return idx

# def get_depth()
#get snow depth
#write to file (apend to list)



#open and loop netCDF lidar files
path = '/home/meganmason/Documents/projects/thesis/data/processing_lidar/\
depths_3m/all_rescaled/nc_lidar/'

pt_x = 4190721.0 #lon
pt_y = 301751.9 #lat

dep = []
# idx_x = []
# idx_y = []

for filepath in sorted(glob.glob(os.path.join(path, '*.nc'))):
    ds = Dataset(filepath)
    lat = ds.variables['x'][:] #lat values(degrees) to np arrays
    lon = ds.variables['y'][:]

    ix_min = get_closest(lon, pt_x)
    iy_min = get_closest(lat, pt_y)

    arr = ds['Band1'][:,:]
    scaled_dep = arr[ix_min,iy_min] #gets recaled depth value

    dep.append(scaled_dep)



#
fig, ax = plt.subplots()
ax.plot(dep)

ax.set(xlabel='recaled snow depth', ylabel='freqency',
       title='pixel time series')
ax.grid()

# fig.savefig("test.png")
plt.show()


# plt.plot(dep)
# plt.show()
