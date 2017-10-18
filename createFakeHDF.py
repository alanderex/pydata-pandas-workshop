import numpy as np
from pandas import HDFStore, DataFrame

# create (or open) an hdf5 file and opens in append mode
hdf = HDFStore('data/hdata.h5')

df = DataFrame(np.random.rand(1000, 3), columns=('A', 'B', 'C'))
# put the dataset in the storage
hdf.put('d1', df, format='table', data_columns=True)
print(hdf['d1'].shape)

hdf.append('d1', DataFrame(np.random.rand(5, 3),
                           columns=('A', 'B', 'C')),
           format='table', data_columns=True)

df = DataFrame(np.random.rand(1000, 3), columns=('A', 'B', 'C'))
# put the dataset in the storage
hdf.put('d2', df, format='table', data_columns=True)
print(hdf['d2'].shape)

hdf.append('d2', DataFrame(np.random.rand(5, 3),
                           columns=('A', 'B', 'C')),
           format='table', data_columns=True)
hdf.close()  # closes the file
