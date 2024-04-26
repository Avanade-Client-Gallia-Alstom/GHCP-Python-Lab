import pandas as pd
import matplotlib.pyplot as plt
 
# Load the data
df = pd.read_csv('train_accidents.csv')
 
# Convert 'Date' to datetime
df['Date'] = pd.to_datetime(df['Date'])
 
# Extract the year
df['Year'] = df['Date'].dt.year
 
# Group by 'Year' and 'Cause'
grouped = df.groupby(['Year', 'Cause']).size().reset_index(name='Counts')
 
# Pivot the DataFrame
pivot_df = grouped.pivot(index='Year', columns='Cause', values='Counts')
 
# Plot the DataFrame
for year in pivot_df.index:
    pivot_df.loc[year].plot(kind='pie', autopct='%1.1f%%')
    plt.title(f'Accidents in {year}')
    plt.ylabel('')
    plt.show()