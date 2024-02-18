import pandas as pd
import io
 
#uploaded = files.upload()
#df = pd.read_csv(io.BytesIO(uploaded['time_series_data.csv']))
#print(df)
# Load time series data from a CSV file
df = pd.read_csv('time_series_data.csv', parse_dates=['Date'], index_col='Date')

# Display the first few rows of the DataFrame
print(df.head())
