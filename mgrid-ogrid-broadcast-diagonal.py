import numpy as np

#mgrid
x,y = np.mgrid[0:10:2, 2:10:1]
print('x',x)
print('y',y)

#ogrid
x,y = np.ogrid[0:10:2, 2:10:1]
print('x',x)
print('y',y)
print('x+y:-',x+y)

#brodcast array
x2,y2 = np.broadcast_arrays(x,y)
print('x2 :-',x2)
print('y2 :-',y2)
print('x2+y2:-',x2+y2)

#diagonal mtrx
x = np.diag((1,7,2), k=2)
print(x)