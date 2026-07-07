# Pipeline from scikit-learn — a way to chain multiple processing steps (like feature transformation + model fitting) into a single object. Instead of manually calling PolynomialFeatures.fit_transform() and then LinearRegression.fit() separately every time, a pipeline bundles both steps together, making it easy to experiment with different polynomial degrees using one reusable function.

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
from sklearn.pipeline import Pipeline
from sklearn.metrics import r2_score

# 1. Load real data
df = pd.read_csv("height-weight.csv")

# 2. Define X and y (single feature example, e.g. predicting salary from experience)
X = df[['Height',]]   # keep as DataFrame (2D) — same rule as before
y = df['Weight']
sns.pairplot(df)
plt.show()

# 3. Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 4. Build the same pipeline function, made reusable for any dataset
def poly_regression(degree, X_train, y_train, X_test, y_test):
    poly_features = PolynomialFeatures(degree=degree, include_bias=True)
    linear_regression = LinearRegression()

    pipeline = Pipeline([
        ('poly_features', poly_features),
        ('linear_regression', linear_regression)
    ])

    pipeline.fit(X_train, y_train)

    # score on real held-out test data
    y_pred = pipeline.predict(X_test)
    score = r2_score(y_test, y_pred)
    print(f"Degree {degree} -> R2 score: {score:.4f}")

    # generate a smooth curve across the ACTUAL range of the real feature
    X_new = np.linspace(X.values.min(), X.values.max(), 200).reshape(-1, 1)
    y_new_pred = pipeline.predict(X_new)

    plt.plot(X_new, y_new_pred, color='red', label=f'Degree {degree} fit')
    plt.scatter(X_train, y_train, color='blue', label='Training Points')
    plt.scatter(X_test, y_test, color='green', label='Testing Points')
    plt.xlabel(X.columns[0])
    plt.ylabel(y.name)
    plt.legend()
    plt.show()

    return pipeline

# 5. Try different degrees on the real dataset
for d in range(1,10):
    poly_regression(d, X_train, y_train, X_test, y_test)
#degree 2 gives 0.71 R2 score which is best