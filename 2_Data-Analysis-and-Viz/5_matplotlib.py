import matplotlib.pyplot as plt  #  This is correct
x = [1, 2, 3, 4, 5]
y = [1, 4, 9, 16, 25]

#Line Graph
plt.plot(x, y, color='red', linestyle='--', marker='o', linewidth=2, markersize=9)
plt.xlabel('x axis')
plt.ylabel('y axis')
plt.title('Basic Line Plot')
plt.grid(True)
plt.show()

#SubPlot
plt.figure(figsize=(9, 5))
y1 = [1, 4, 9, 16, 25]
y2 = [1, 3, 6, 8, 5]

plt.subplot(2, 2, 1)   # (rows, cols, position) — position counts left-to-right, top-to-bottom, 1-indexed
plt.plot(x, y1, color='green')
plt.title('Plot 1')

plt.subplot(2, 2, 2)
plt.plot(x, y1, color='red')
plt.title('Plot 2')

plt.subplot(2, 2, 3)
plt.plot(x, y2, color='blue')
plt.title('Plot 3')

plt.subplot(2, 2, 4)
plt.plot(x, [v**2 for v in x], color='green')   # squaring a list needs a comprehension, not x*2
plt.title('Plot 4')

plt.tight_layout()   # prevents titles/labels overlapping — the transcript never used this
plt.show()

#Bar Graph
categories = ['A', 'B', 'C', 'D', 'E']
values = [5, 7, 3, 8, 6]
plt.bar(categories, values, color='purple')
plt.show()

#Histogram
data = [1, 1.5, 2, 2.3, 2.8, 3, 3.5, 4, 4.5, 5]
plt.hist(data, bins=5, color='orange', edgecolor='black')
plt.show()

#ScatterPlot
plt.scatter(x, y, marker='x')
plt.show()

#Pie Chart
labels = ['A', 'B', 'C', 'D']
sizes = [30, 20, 40, 10]
colors = ['gold', 'yellowgreen', 'lightcoral', 'lightskyblue']
explode = [0.1, 0, 0, 0]   # pulls the first slice out for emphasis

plt.pie(sizes, labels=labels, colors=colors, explode=explode,
        autopct='%1.1f%%', shadow=True)
plt.show()

#Practical Example
import pandas as pd
# Load your CSV data
df = pd.read_csv('sales_data.csv')
# Optional but recommended: strip any accidental trailing spaces from headers
df.columns = df.columns.str.strip()

# 1. Bar Graph: Total Sales by Item Type
total_sales = df.groupby('Item Type')['Total Revenue'].sum()
print(df.head())

total_sales.plot(kind='bar', color='teal')
plt.xlabel('Item Type')
plt.ylabel('Total Revenue')
plt.title('Total Sales by Product')
plt.xticks(rotation=45) # Rotates the text so names don't overlap
plt.tight_layout()
plt.show()

# 2. Line Graph: Sales Trend over Time
sales_trend = df.groupby('Order Date')['Total Revenue'].sum().reset_index()

plt.figure()
plt.plot(sales_trend['Order Date'], sales_trend['Total Revenue'], color='blue', marker='o')
plt.xlabel('Order Date')
plt.ylabel('Total Revenue')
plt.title('Sales Trend Over Time')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()