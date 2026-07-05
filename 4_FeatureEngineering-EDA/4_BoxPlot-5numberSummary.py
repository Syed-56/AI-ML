import numpy as np

list_of_marks = [45, 32, 56, 75, 89, 54, 32, 89, 90, 87, 67, 54, 45, 98, 99, 67, 74]

minimum, q1, median, q3, maximum = np.quantile(
    list_of_marks, [0, 0.25, 0.50, 0.75, 1.0]
)
IQR = q3-q1
lower_fence = q1 - 1.5 * IQR
upper_fence = q3 + 1.5 * IQR
#this list contains no outliers

import seaborn as sns
import matplotlib.pyplot as plt
sns.boxplot(data=list_of_marks)
plt.title('Distribution of Marks')
plt.ylabel('Marks')
plt.show()

list_with_outliers = list_of_marks + [-100, -200, 150, 170]
sns.boxplot(data=list_with_outliers)
plt.title('Distribution of Marks with outliers')
plt.ylabel('Marks')
plt.show()