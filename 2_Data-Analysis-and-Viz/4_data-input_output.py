import pandas as pd
from io import StringIO

#JSON
json_str = '{"employee_name": {"0":"James"}, "email": {"0":"james@gmail.com"}}'
df = pd.read_json(StringIO(json_str))

df.to_json(orient='index')     # default: {"col":{"0":val,...}}
df.to_json(orient='records')    # [{"col":val,...}, {...}]   <- usually what you want for APIs

#From URL
url = "https://archive.ics.uci.edu/ml/machine-learning-databases/wine/wine.data"
df = pd.read_csv(url, header=None)   # header=None -> no header row in source, columns become 0,1,2...
df.to_csv('wine.csv', index=False)     # index=False avoids writing the row index as a junk extra column

#HTML Tables
from bs4 import BeautifulSoup
import lxml
import html5lib
tables = pd.read_html(url)          # returns a LIST of DataFrames, one per <table>
df = tables[0]
# narrow down which table with `match`
tables = pd.read_html(url, match='Country', header=0)
df = tables[0]

#Excel
import openpyxl
df = pd.read_excel('data.xlsx', sheet_name=0)   # sheet_name: index, name, or None for all sheets as a dict
df.to_excel('output.xlsx', index=False)

#Pickle
df.to_pickle('data.pkl')
df2 = pd.read_pickle('data.pkl')