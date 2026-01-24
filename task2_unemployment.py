import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# ==================================================
# DATASET 1: Unemployment_Rate_upto_11_2020.csv
# ==================================================

df1 = pd.read_csv("Unemployment_Rate_upto_11_2020.csv")

# Rename columns
df1.rename(columns={
    'Region': 'State',
    ' Date': 'Date',
    ' Estimated Unemployment Rate (%)': 'Unemployment_Rate',
    ' Estimated Employed': 'Employed',
    ' Estimated Labour Participation Rate (%)': 'Labour_Participation',
    'Region.1': 'Area'
}, inplace=True)

# Convert Date
df1['Date'] = pd.to_datetime(df1['Date'])

print("DATASET 1 INFO")
print(df1.info())

# 1. Unemployment Trend (2020)
plt.figure(figsize=(10,5))
plt.plot(df1['Date'], df1['Unemployment_Rate'])
plt.title("Unemployment Rate in India (2020)")
plt.xlabel("Date")
plt.ylabel("Unemployment Rate (%)")
plt.show()



# 2. Covid-19 Impact
covid = df1[df1['Date'].dt.month >= 3]
sns.lineplot(x='Date', y='Unemployment_Rate', data=covid)
plt.title("Covid-19 Impact on Unemployment (2020)")
plt.show()



# 3. Rural vs Urban
sns.boxplot(x='Area', y='Unemployment_Rate', data=df1)
plt.title("Rural vs Urban Unemployment (2020)")
plt.show()




# ==================================================
# DATASET 2: Unemployment in India.csv
# ==================================================

df2 = pd.read_csv("Unemployment in India.csv")

# Rename columns
df2.rename(columns={
    'Region': 'State',
    ' Date': 'Date',
    ' Estimated Unemployment Rate (%)': 'Unemployment_Rate',
    ' Estimated Employed': 'Employed',
    ' Estimated Labour Participation Rate (%)': 'Labour_Participation',
    'Region.1': 'Area'
}, inplace=True)

# Convert Date
df2['Date'] = pd.to_datetime(df2['Date'])

print("\nDATASET 2 INFO")
print(df2.info())

# 4. Unemployment Trend (All Periods)
plt.figure(figsize=(10,5))
plt.plot(df2['Date'], df2['Unemployment_Rate'])
plt.title("Unemployment Rate in India (Overall)")
plt.xlabel("Date")
plt.ylabel("Unemployment Rate (%)")
plt.show()




# 5. State-wise Average Unemployment
state_avg = df2.groupby('State')['Unemployment_Rate'].mean().sort_values()

plt.figure(figsize=(8,10))
state_avg.plot(kind='barh')
plt.title("Average Unemployment Rate by State")
plt.xlabel("Unemployment Rate (%)")
plt.show()

