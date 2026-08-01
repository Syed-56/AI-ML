import pandas as pd

train = pd.read_csv("train.csv")
test = pd.read_csv("test.csv")

print(train.shape)    #tells number of rows and cols
print(train.head())   #outputs csv data
print(train.info())     #tells datatype of each column
print(train.describe())     #tells count,minmax,std,quartiles
print(train.isnull().sum())     #count null values
print(train['Irrigation_Need'].value_counts())  #counts the target

from sklearn.preprocessing import LabelEncoder, StandardScaler

TARGET = 'Irrigation_Need'
X = train.drop(columns=['id',TARGET])
y = train[TARGET]
X_test = test.drop(columns=['id'])

#Encode Categorial Columns - if any
for col in X.select_dtypes(include='object').columns:
    le = LabelEncoder()
    X[col] = le.fit_transform(X[col].astype(str))
    X_test[col] = le.transform(X_test[col].astype(str))
    
#Encode Target
le_target = LabelEncoder()
y = le_target.fit_transform(y)

#Scale
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)
X_test_scaled = scaler.transform(X_test)

from sklearn.tree import DecisionTreeClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import cross_val_score, StratifiedKFold
from sklearn.metrics import accuracy_score, confusion_matrix, ConfusionMatrixDisplay

kf = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)

models = {
    "Decision Tree":    DecisionTreeClassifier(random_state=42),
    "Naive Bayes":      GaussianNB(),
    "Logistic Reg":     LogisticRegression(max_iter=1000, random_state=42),
    "KNN":              KNeighborsClassifier(),
    "Random Forest":    RandomForestClassifier(n_estimators=100, random_state=42),
}

results = {}
for name, model in models.items():
    scores = cross_val_score(model, X_scaled, y, cv=kf, scoring='accuracy', n_jobs=-1)
    results[name] = scores.mean()
    print(f"{name}: {scores.mean():.4f} ± {scores.std():.4f}")
    
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt

X_tr, X_val, y_tr, y_val = train_test_split(X_scaled, y, test_size=0.2, random_state=42)

for name, model in models.items():
    model.fit(X_tr, y_tr)
    preds = model.predict(X_val)
    acc = accuracy_score(y_val, preds)
    cm = confusion_matrix(y_val, preds)
    
    disp = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=le_target.classes_)
    disp.plot(cmap='Blues')
    plt.title(f"{name} — Accuracy: {acc:.4f}")
    plt.tight_layout()
    plt.savefig(f"cm_{name.replace(' ', '_')}.png")
    plt.show()
    print(f"{name}: {acc:.4f}")
    
best_model = RandomForestClassifier(n_estimators=200, random_state=42)
best_model.fit(X_scaled, y)  # full train data

# Generate predictions
test_preds = best_model.predict(X_test_scaled)
test_preds_labels = le_target.inverse_transform(test_preds)

# Submission file
submission = pd.DataFrame({
    'id': test['id'],
    TARGET: test_preds_labels
})
submission.to_csv("submission.csv", index=False)
print(submission.head())
print("Done")