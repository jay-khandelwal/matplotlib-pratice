import matplotlib.pyplot as plt
import numpy as np

for color in ['red','blue','green','yellow','orange','pink','black','white']:
	
	x,y = np.random.rand(2,1000)
	size = 200*np.random.rand(1000)
	
	plt.scatter(x,y,color=color,s=size, cmap='hot')
plt.axis('off')	
plt.legend()
plt.savefig('bestscatterplt.png')
plt.show()