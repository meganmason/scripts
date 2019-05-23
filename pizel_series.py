# ~~~~~~~~~~~~~~~~~~~~   import packages  ~~~~~~~~~~~~~~~~~~~
import os
import glob
from netCDF4 import Dataset
import numpy as np
import matplotlib
import matplotlib.patches as patches
from matplotlib import pyplot as plt
from matplotlib import patches

# ~~~~~~~~~~~~~~~~~~~~   functions  ~~~~~~~~~~~~~~~~~~~~~~~~~

def main():
    #~~~~~~~~~~~~~~change things here ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    #open and loop netCDF lidar files
    path = ('/home/meganmason/Documents/projects/thesis/data/processing_lidar/'
    'depths_3m/all_rescaled/nc_lidar/rescaled_20160407.nc')

    pt_x = 4190721.0 #lon
    pt_y = 301751.9 #lat

    d = [] # value from dataset (rescaled depth or depth)

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    # for filepath in sorted(glob.glob(os.path.join(path, '*.nc'))):
    for filepath in glob.glob(path):
        print(os.path.basename(filepath))

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

    """
    subplots:
        (1). pixel location
        (2). time vs value
        (3). histogram
        (4). [blank]
    """
    # fig, axs = plt.subplots(1)
    fig, axs = plt.subplots(2, 2, figsize=(7, 7))
#1).subplot 1
    axs[0, 0].imshow(arr, origin='lower', cmap='coolwarm')
    s_rect = patches.Rectangle((iy_min,ix_min),width=3,height=3,linewidth=3,edgecolor='r',facecolor='none')
    b_rect = patches.Rectangle((iy_min,ix_min),width=150,height=150,linewidth=3,edgecolor='g',facecolor='none')
    # color='r')
    # edgecolor='r',facecolor='none')
    axs[0,0].add_patch(s_rect)
    axs[0,0].add_patch(b_rect)
    #https://stackoverflow.com/questions/37435369/matplotlib-how-to-draw-a-rectangle-on-image
    plt.annotate('here',xy=(iy_min, ix_min),color='r')
    # Rectangle((ix_min,iy_min), width=3, height=3, angle=0.0, fill=False)

#2).subplot 2
    axs[1, 0].plot(d)
#3).subplot 3
    axs[0, 1].hist(d)
    # axs[1, 1].hist2d(data[0], data[1])
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

if __name__ == '__main__':
    main()
