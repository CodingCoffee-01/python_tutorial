import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('data.csv')

df.head()
print(df.head())

df.plot()

plt.show()
