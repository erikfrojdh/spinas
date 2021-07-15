
import os
import numpy as np

def load_time_series(base, file_slice = None):
    files = [f for f in os.listdir(base.parent) if f.startswith(base.name)]
    files.sort()
    if file_slice is not None:
        files = files[file_slice]

    #Lets look at the first file to guess the file format
    if files[0].endswith('.tif'):
        import tifffile
        tmp = tifffile.imread(base.parent/files[0])
        dt = tmp.dtype
        shape = tmp.shape
        read = tifffile.imread
    else:
        raise ValueError("Unsupported file format")    
    

    shape = np.array((len(files), *shape))

    data = np.zeros(shape, dtype = dt)
    for i,f in enumerate(files):
        data[i] = read(base.parent/f)
    return data