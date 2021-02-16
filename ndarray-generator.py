import numpy as np

ndarray = np.floor(10*np.random.random([100,1000]))

np.savetxt('random-ndarray.csv',ndarray)