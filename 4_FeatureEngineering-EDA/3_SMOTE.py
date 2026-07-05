#create imbalanced dataset
from sklearn.datasets import make_classification

X, y = make_classification(
    n_samples=1000,
    n_features=2,
    n_redundant=0,        # no redundant (linear combination) features
    n_clusters_per_class=1,
    weights=[0.90],       # 90% majority class, 10% minority class
    random_state=12
)

#visualizing imbalance
import pandas as pd
import matplotlib.pyplot as plt

df1 = pd.DataFrame(X, columns=['f1', 'f2'])
df2 = pd.DataFrame(y, columns=['target'])
final_df = pd.concat([df1, df2], axis=1)

final_df['target'].value_counts()
# 0    900
# 1    100

scatter = plt.scatter(final_df['f1'], final_df['f2'], c=final_df['target'])
plt.legend(*scatter.legend_elements(), title="Classes")
plt.show()

#applying SMOTE
from imblearn.over_sampling import SMOTE
oversample = SMOTE()
X, y = oversample.fit_resample(final_df[['f1', 'f2']], final_df['target'])

#verify
X.shape   # (1800, 2) — up from 900 majority-only rows before
y.shape   # (1800,)
len(y[y == 0])   # 900
len(y[y == 1])   # 900 — now equal to majority class

#visualize oversampled data
oversampled_df = pd.concat([X, y], axis=1)
scatter = plt.scatter(oversampled_df['f1'], oversampled_df['f2'], c=oversampled_df['target'])
plt.legend(*scatter.legend_elements(), title="Classes")
plt.show()