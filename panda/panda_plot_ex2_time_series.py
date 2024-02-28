import pandas as pd
import matplotlib.pyplot as plt

# Load time series data from a CSV file
df = pd.read_csv('time_series_data.csv')
df.head()
print(df.head())

df.plot()

plt.show()
