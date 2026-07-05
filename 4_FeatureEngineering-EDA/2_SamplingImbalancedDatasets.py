#Creating Imbalanced Dataset
import numpy as np
import pandas as pd

np.random.seed(123)  # ensures reproducibility

n_samples = 1000
class_0_ratio = 0.9
n_class_0 = int(n_samples * class_0_ratio)  # 900
n_class_1 = n_samples - n_class_0            # 100

# Class 0 (majority) — two normally distributed features
class_0 = pd.DataFrame({
    'feature_1': np.random.normal(loc=0, scale=1, size=n_class_0),
    'feature_2': np.random.normal(loc=0, scale=1, size=n_class_0),
    'target': [0] * n_class_0
})

# Class 1 (minority)
class_1 = pd.DataFrame({
    'feature_1': np.random.normal(loc=2, scale=1, size=n_class_1),
    'feature_2': np.random.normal(loc=2, scale=1, size=n_class_1),
    'target': [1] * n_class_1
})

df = pd.concat([class_0, class_1]).reset_index(drop=True)
print(df['target'].value_counts())
# 0    900
# 1    100

#Upsampling
from sklearn.utils import resample

# Separate majority and minority classes
df_majority = df[df['target'] == 0]
df_minority = df[df['target'] == 1]

df_minority_upsampled = resample(
    df_minority,
    replace=True,                    # sample with replacement
    n_samples=len(df_majority),      # match majority class count
    random_state=42
)

df_upsampled = pd.concat([df_majority, df_minority_upsampled])

print(df_upsampled['target'].value_counts())
# 0    900
# 1    900

#Downsampling
df_majority_downsampled = resample(
    df_majority,
    replace=False,                   # no replacement — just reduce
    n_samples=len(df_minority),      # match minority class count
    random_state=42
)

df_downsampled = pd.concat([df_minority, df_majority_downsampled])

print(df_downsampled['target'].value_counts())
# 1    100
# 0    100