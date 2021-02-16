import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

google_data = pd.read_csv('49864_274957_compressed_googleplaystore.csv/googleplaystore.csv', nrows=500)

downloads =google_data['Installs']
reviews =google_data['Reviews']
rating =google_data['Rating']
plt.figure(figsize=(9,16))
plt.scatter(rating, downloads, label='T. download', c =reviews)
#plt.bar(rating,downloads)
#plt.scatter(rating, reviews, label='Reviews', color ='blue', s =)

plt.colorbar()

plt.xlabel('google app rating')
plt.ylabel('google app reviews and downloads')

plt.xscale('log')
#plt.yscale('log')

plt.title('google app store data')
plt.legend()
plt.show()