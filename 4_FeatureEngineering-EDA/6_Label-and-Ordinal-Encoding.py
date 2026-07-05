#Label
from sklearn.preprocessing import LabelEncoder
import pandas as pd

df = pd.DataFrame({
    'color': ['red', 'blue', 'green', 'green', 'red', 'blue']
})
df.head()
label_encoder = LabelEncoder()
df['color_encoded'] = label_encoder.fit_transform(df['color'])

#encoding new values after fitting
redEncoded = label_encoder.transform(['red'])    # array([2])
blueEncoded = label_encoder.transform(['blue'])   # array([0])
greenEncoded = label_encoder.transform(['green'])  # array([1])
print(redEncoded, blueEncoded, greenEncoded)

#Ordinal
from sklearn.preprocessing import OrdinalEncoder
# Example dataframe
df = pd.DataFrame({
    'size': ['small', 'medium', 'large', 'medium', 'small', 'large']
})
encoder = OrdinalEncoder(categories=[['small', 'medium', 'large']])
df['size_encoded'] = encoder.fit_transform(df[['size']])
print(encoder.transform([['small']]))  # array([[0.]])