import pandas as pd
import numpy as np

#missing values
df = pd.read_csv('sales_data.csv')

df.isnull()             # DataFrame of True/False per cell
df.isnull().sum()        # count of missing values per column (most useful form)
df.isnull().sum(axis=1)   # count of missing values per row
#they can be filled as
df['value'] = df['value'].fillna(0)                  # fill with a constant
df['sales'] = df['sales'].fillna(df['sales'].mean())    # fill with column mean — common for numeric data
df['category'] = df['category'].fillna(df['category'].mode()[0])  # fill categorical with most frequent value

#Dtype fix
df.dtypes                          # check types first
df['value'] = df['value'].astype(float)
df['value'] = df['value'].fillna(df['value'].mean()).astype(int)   # must fill NaN before converting to int — int can't hold NaN

#for dates
df['date'] = pd.to_datetime(df['date'])   # not .astype() — dates need this dedicated function
#column rename
df = df.rename(columns={'date': 'sales_date'})

#applying functions
df['value_doubled'] = df['value'].apply(lambda x: x * 2)
# for row-wise logic across multiple columns:
df['total'] = df.apply(lambda row: row['price'] * row['qty'], axis=1)

#group by and aggregation
df.groupby('product')['value'].mean()
df.groupby(['product', 'region'])['value'].sum()

df.groupby('region')['value'].agg(['mean', 'sum', 'count'])   # multiple aggregations at once