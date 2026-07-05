import pandas as pd

df = pd.DataFrame({
    'city': ['New York', 'London', 'Paris', 'Tokyo', 'New York', 'Paris'],
    'price': [200, 150, 320, 250, 180, 300]
})

#compute mean target value per city
mean_price = df.groupby('city')['price'].mean().to_dict()   #nyc: 190, #london: 150

#map encoded values back on dataframe
df['city_encoded'] = df['city'].map(mean_price)

#use encoded feature for training
df_final = df[['city_encoded', 'price']]