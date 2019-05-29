# ~~~~~~~~~~~~~~~~~~~~   import packages  ~~~~~~~~~~~~~~~~~~~
import os
import glob
from netCDF4 import Dataset
import numpy as np
import pandas as pd
import matplotlib
import matplotlib.patches as patches
from matplotlib import pyplot as plt
from matplotlib import patches

# ~~~~~~~~~~~~~~~~~~~~   functions  ~~~~~~~~~~~~~~~~~~~~~~~~~

# def main():
#~~~~~~~~~~~~~~change things here ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#open and loop netCDF lidar files
path = ('/home/meganmason/Documents/projects/thesis/data/processing_lidar/'
    'depths_3m/all_rescaled/nc_lidar/')

# rescaled_20160407.nc')

#pt_x = 4190721.0 #lon [deep zone]
#pt_y = 301751.9 #lat

pt_x = 4193054.6 #lon [scour zone]
pt_y = 301167.1 #lat

#pt_x = 4186970.9 #lon [lyell canyon, flat]
#pt_y = 300627.2 #lat

d = [] # value from dataset (rescaled depth or depth)
dates = []
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
for filepath in sorted(glob.glob(os.path.join(path, '*.nc'))):
# for filepath in glob.glob(path):
    # f=os.path.basename(filepath)
    print(os.path.basename(filepath)) #follow which file when script runs
    # print(f)
    """
    grab dates to get a time vector
    """
    # for f in sorted(os.path.basename(filepath)):

#     dt_str = "".join([c for c in f if c.isnumeric()])
#
#     print(dt_str)
#     dates.append(dt_str)
# dates = pd.to_datetime(dates)
# print(dates)

    """
    here's the netCDF dataset
    """
    ds = Dataset(filepath)
    lat = ds.variables['x'][:] #lat values(degrees) to np arrays
    lon = ds.variables['y'][:]


    """
    find pixel for x,y point
    """
    ix_min = np.argmin(np.abs(lon-pt_x))
    iy_min = np.argmin(np.abs(lat-pt_y))


    """
    what is the depth (or rescalled depth) @ pixel
    """

    arr = ds['Band1'][:,:] #array of recaled depths
    pix = arr[ix_min,iy_min] #pixel in basin lidar
    ds.close() #done with dataset
    d.append(pix) #grow d[], need for plotting
    # print(d)

"""
subplots:
    (1). pixel location
    (2). time vs value
    (3). histogram of rescaled depths
    (4). [blank]
"""
# fig, axs = plt.subplots(1)
fig, axs = plt.subplots(2, 2, figsize=(7, 7))

#1).subplot 1
axs[0, 0].imshow(arr, origin='lower', cmap='coolwarm')
s_rect = patches.Rectangle((iy_min,ix_min),width=30,height=30,linewidth=3,edgecolor='r',facecolor='none')
# b_rect = patches.Rectangle((iy_min,ix_min),width=150,height=150,linewidth=3,edgecolor='g',facecolor='none')
axs[0,0].add_patch(s_rect)
# axs[0,0].add_patch(b_rect)
axs[0, 0].set_title('pixel location')
axs[0,0].set_xlabel('Easting'); axs[0,0].set_ylabel('Northing')

#2).subplot 2
# axs[1, 0].plot(dates,d)
axs[1, 0].plot(d)
axs[1, 0].set_title('time vs rescaled snow depth')
axs[1,0].set_xlabel('date'); axs[0,0].set_ylabel('Rescaled snow depth')
#3).subplot 3
bins = np.linspace(0, 3.5, 30)
axs[0, 1].hist(d,bins)
axs[0, 1].set_title('frequency of rescaled value')
axs[0,1].set_xlabel('Rescaled snow depth'); axs[0,0].set_ylabel('Frequency')

#
# axs[0, 0].hist(data[0])
# axs[1, 0].scatter(data[0], data[1])
# axs[0, 1].plot(data[0], data[1])
# axs[1, 1].hist2d(data[0], data[1])

plt.show()



# fig, ax = plt.subplots()
# ax.plot(dep)
#
# ax.set(xlabel='recaled snow depth', ylabel='freqency',
#        title='pixel time series')
# ax.grid()
#
# # fig.savefig("test.png")
# plt.show()


# plt.plot(dep)
# plt.show()

# if __name__ == '__main__':
#     main()
