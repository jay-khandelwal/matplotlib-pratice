import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

google_data = pd.read_csv('49864_274957_compressed_googleplaystore.csv/googleplaystore.csv', nrows=5000)
#App,Category,Rating,Reviews,Size,Installs,Type,Price,Content Rating,Genres,Last Updated,Current Ver,Android Ver

category =google_data['Category']
#reviews =google_data['Reviews']
rating =google_data['Rating']

plt.hist(rating, linestyle='--', color='g', edgecolor='blue', orientation='horizontal')
#plt.xticks(rotation=30)


#plt#.xlabel('Frequency')
#plt.ylabel('google app category')

#plt.title('google app store mostly used category')
#plt.legend()
#plt.tight_layout()
plt.show()