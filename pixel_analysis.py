#PART 1:
import os
import pandas as pd
import sys #sys.exit()
import glob
#PART 2:
from netCDF4 import Dataset
import numpy as np
from matplotlib import pyplot as plt
# ~~~~~~~~~~~~~~~~~~~~   functions  ~~~~~~~~~~~~~~~~~~~~~~~~~

def getclosest(arr,pt):
    idx = np.argmin(np.abs(arr-pt)) #indexs location
    return idx



def pixel_plot():
    pass



# ~~~~~~~~~~~~~~~~~   loop thru rescaled lidar flights  ~~~~~~~~~~~~
# PART I:
path = '/home/meganmason/Documents/projects/thesis/data/processing_lidar/depths_3m/all_rescaled/'
dates = [] #allocate dates list
# dt_str = [] #allocate dates list

# for files in os.walk(path): #go through every directory in path
for root, dirs, files in os.walk(path): #go through every directory in path
    for f in sorted(files):
        if f.split(".")[-1]=="tif": #only grabs .tifs (excludes my readme file)
            dt_str = "".join([c for c in f if c.isnumeric()]) #list comprehension: same as below

            dates.append(dt_str) #adds date to []

dates = pd.to_datetime(dates) #convert date strings to datetime type
# print(len(dates)) #final list, outside of for loops
# print(f,dt_str,dates)


# sys.exit()
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#PART II:

# sys.exit() #don't run anything below

# # ~~~~~~~   set site locations  ~~~~~~~~~~~~
path = '/home/meganmason/Documents/projects/thesis/data/processing_lidar/depths_3m/all_rescaled/nc_lidar/'

pt_x = 4190721.0 #lon
pt_y = 301751.9 #lat

idx_x = []
idx_y = []

for filepath in sorted(glob.glob(os.path.join(path, '*.nc'))):
    # print(filepath)
    # dir = os.path.dirname(filepath)
## 1. Read the file and index x and y
    ds = Dataset(filepath)
    lat = ds.variables['x']
    lon = ds.variables['y']

    # grab lat/lon values (in degrees) to numpy arrays
    latvals = lat[:]
    lonvals = lon[:]

    ix_min = getclosest(lonvals, pt_x)
    iy_min = getclosest(latvals, pt_y)
    idx_x.append(ix_min)
    idx_y.append(iy_min)



# table=[dates,idx_x,idx_y]

# print(iy_min)
# print(ix_min)

# print('idx',iy_min)

# x = x.append(ix_min)
# y = y.append(iy_min)

# print(x)
# print(y)

ds = Dataset(filepath)

arr = ds['Band1'][:,:]
plt.annotate('here',xy=(iy_min, ix_min))
# plt.annotate('here',xy=(arr[ix_min], arr[iy_min]))
plt.imshow(arr)
#
# plt.annotate('25, 50', xy=(25, 40), xycoords='data',
#              xytext=(0.5, 0.5), textcoords='figure fraction',
#              arrowprops=dict(arrowstyle="->"))
plt.show()
# plt.savefig('foo')


# 2. write location index to files
# https://www.guru99.com/reading-and-writing-files-in-python.html
# f=open("coords.txt","a+") #appends and generates if not there
# f=open("pixel_x_and_y.txt","w+") #writes file
# foo = "%d %d\n" % (ix_min, iy_min)
# print(foo)
#
# f.write("%d %d\n" % (ix_min, iy_min)
#
# f.close()




### direction from subnaught ###
## 1. Read the file header and parse ncols,nrows,dx,dy
## 2. for i in ncols:
##      xlist.append(i*dx+xllcorner)
##       Repeat for y

## 3.xlist - myxcoordinate, repeat for y
## 4. find smallest, grab index. np.min(np.abs())
## 5. grab yo data. Do sum shit

####### netcdf ###########
## ds = Dataset("netcdf.nc")




#GOOOOOOD-ish
#
# coords = {'x': 301751.9,'y': 4190721.0}
# coords = {'x':[301751.9,301167.1,300627.2],'y': [4190721.0,4193054.6,4186970.9]}
#
# # for k,v in coords.items():
# #     coords['x']
# #     print(k,v)
# #
# for idx in range(len(coords['x'])):
#     x = coords['x'][idx] #loops through x's
#     y = coords['y'][idx] #loops through y's
