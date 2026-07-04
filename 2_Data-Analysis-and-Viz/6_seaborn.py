import seaborn as sns
import matplotlib.pyplot as plt

tips = sns.load_dataset('tips')   # built-in sample datasets, no download needed
sns.scatterplot(x='total_bill', y='tip', data=tips)
plt.title('Total Bill vs Tip')
plt.show()

sns.lineplot(x='size', y='total_bill', data=tips)
plt.show()

sns.barplot(x='day', y='total_bill', data=tips)     # bar height = mean by default
sns.boxplot(x='day', y='total_bill', data=tips)       # shows median, quartiles, outliers
sns.violinplot(x='day', y='total_bill', data=tips)     # box plot + distribution shape combined
plt.show()

sns.histplot(tips['total_bill'], bins=10, kde=True)   # kde=True overlays a smoothed density curve
sns.kdeplot(tips['total_bill'], fill=True)               # just the smoothed curve, correction: 'fill', not deprecated 'shade'
plt.show()

sns.pairplot(tips)   # grid of every numeric column against every other — diagonal shows each column's own distribution
plt.show()

numeric_cols = tips[['total_bill', 'tip', 'size']]
corr = numeric_cols.corr()
sns.heatmap(corr, annot=True, cmap='coolwarm')
plt.show()