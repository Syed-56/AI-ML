import pandas as pd

s = pd.Series([1, 2, 3, 4, 5])          # default index 0..4
s2 = pd.Series({'a': 1, 'b': 2, 'c': 3})  # dict keys become the index
s3 = pd.Series([10, 20, 30], index=['a', 'b', 'c'])  # custom index
print(s)
print(s2)
print(s3)

#Creating Dataframes
#from a dict of lists
data = {
    'name': ['Krish', 'John', 'Jack'],
    'age': [25, 30, 45],
    'city': ['Bangalore', 'New York', 'Florida']
}
df = pd.DataFrame(data)
#from list of dicts
data = [
    {'name': 'Krish', 'age': 32, 'city': 'Bangalore'},
    {'name': 'John', 'age': 34, 'city': 'Bangalore'},
]
df = pd.DataFrame(data)

#Reading Files
df = pd.read_csv('sales_data.csv')
df.head()      # first 5 rows
df.head(10)    # first 10
df.tail()      # last 5
df.describe()  # count, mean, std, min, 25/50/75%, max — numeric columns only
df.info()      # dtypes + non-null counts, very useful — the transcript never mentioned this one

#accessing files
df['name']          # whole column -> Series
df.loc[0]            # row with label 0 -> Series
df.iloc[0]            # row at position 0 -> Series
df.iloc[0, 1]          # row 0, col 1 (by position)
df.loc[0:1, 'name':'age']  # slice by labels — note: loc slicing INCLUDES the endpoint
df.at[1, 'age']        # fast scalar access by label
df.iat[2, 2]            # fast scalar access by position

# Add a column
df['salary'] = [50000, 60000, 70000]
# Modify a column in place, vectorized (no loop needed — same idea as NumPy)
df['age'] = df['age'] + 1
# Drop a column
df.drop('salary', axis=1, inplace=True)     # axis=1 = columns, axis=0 = rows (default)
# Drop a row by index label
df.drop(0, axis=0, inplace=True)