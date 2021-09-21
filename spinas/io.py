
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


def replace_in_file(file_in, file_out, sub):
    with open(file_in) as f:
        lines_in = f.readlines()

    lines_out = replace_in_lines(lines_in, sub)

    with open(file_out, 'w') as f:
        f.writelines(lines_out)


def replace_in_lines(lines, sub):
    """
    Replaces keys in a list of strins. Uses f-string formatting
    to accept a natural syntax with numbers.
    """
    lines_out = []
    for line in lines:
        for key, value in sub.items():
            line = line.replace(key, f'{value}')
        lines_out.append(line)
    return lines_out



sparse_dt = [('event', np.uint32),
    ('col', np.uint32),
    ('row', np.uint32),
    ('energy', np.double),
    ('tot', np.double),
    ('toa', np.double)]

def load_sparse(fname, sorted = True):
    data = np.fromfile(fname, dtype = sparse_dt)
    data.sort(axis = 0)
    return data

# def get_info(fname):
#     magic_str = b"\x93NUMPY"
#     with open(fname, "rb") as f:
#         if f.read(6) != magic_str:
#             raise ValueError("File is not a numpy file")
#         major_version = np.fromfile(f, dtype=np.uint8, count=1)[0]
#         minor_version = np.fromfile(f, dtype=np.uint8, count=1)[0]
#         header_len = np.fromfile(f, dtype=np.uint16, count=1)[0]
#         header = f.read(header_len)
#         return eval(header)