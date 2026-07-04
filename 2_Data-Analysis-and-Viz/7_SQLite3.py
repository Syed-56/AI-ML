import sqlite3

conn = sqlite3.connect('example.db')   # creates the file if it doesn't exist
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS employees (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    age INTEGER,
    department TEXT
)
''')
conn.commit()

#Insert
cursor.execute(
    "INSERT INTO employees (name, age, department) VALUES (?, ?, ?)",
    ('Krish', 32, 'Data Scientist')
)
conn.commit()
#Bulk Insert
sales_data = [
    ('2024-01-01', 'Laptop', 5, 'North'),
    ('2024-01-02', 'Phone', 10, 'South'),
]
cursor.executemany(
    "INSERT INTO sales (date, product, sales, region) VALUES (?, ?, ?, ?)",
    sales_data
)
conn.commit()

#Query and Fetch
cursor.execute("SELECT * FROM employees")
rows = cursor.fetchall()      # list of tuples, all rows
# cursor.fetchone()             # just the next row
# cursor.fetchmany(5)             # next 5 rows

for row in rows:
    print(row)
    
#Update/Delete
cursor.execute("UPDATE employees SET age = ? WHERE name = ?", (34, 'Krish'))
cursor.execute("DELETE FROM employees WHERE name = ?", ('Bob',))
conn.commit()

conn.close()

#Standard Practice
with sqlite3.connect('example.db') as conn:
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM employees")
    rows = cursor.fetchall()
# commits automatically on success, rolls back on exception, though conn still needs closing separately

#Reading in DataFrame
import pandas as pd
df = pd.read_sql_query("SELECT * FROM employees", conn)