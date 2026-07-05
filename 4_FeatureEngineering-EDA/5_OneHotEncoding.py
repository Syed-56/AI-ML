import pandas as pd
from sklearn.preprocessing import OneHotEncoder

# Create a simple dataframe
df = pd.DataFrame({
    'color': ['red', 'blue', 'green', 'green', 'red', 'blue']
})
df.head()

#Create encoder instance and fit-transform
encoder = OneHotEncoder()

encoded = encoder.fit_transform(df[['color']])  # note: double brackets → 2D input required
#fit_transform() returns a sparse matrix by default. Convert it to a dense array to view it:
encoded.toarray()

#convert to readable df
encoded_df = pd.DataFrame(
    encoded.toarray(),
    columns=encoder.get_feature_names_out()
)   #This gives columns like color_blue, color_green, color_red, each populated with 0s and 1s.

#combine with original df
df_encoded = pd.concat([df, encoded_df], axis=1)
print(df)
print(df_encoded)