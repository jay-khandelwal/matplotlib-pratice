import matplotlib.pyplot as plt
from collections import Counter
import pandas as pd

plt.style.use('ggplot')
data = pd.read_csv('data.csv')

language = data['LanguagesWorkedWith']
print(language)
responderId = data['Responder_id']

language_counter = Counter()

for response in language:
	language_counter.update(response.split(';'))
	
languages = []
responder_id =[]

for items in language_counter.most_common(15):
	languages.append(items[0])
	responder_id.append(items[1])
	
plt.barh(languages,responder_id)
plt.show()