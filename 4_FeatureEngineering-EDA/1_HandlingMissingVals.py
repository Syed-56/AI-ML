#HANDLING MISSING VALUES
import seaborn as sns
df = sns.load_dataset('titanic')
df.head()
print(df.isnull()) #check missing values
print(df.isnull().sum())   #count missing values per column
print((df.isnull().sum()/len(df))*100)    #%age missing per column

#DELETION
#row-wise deletion (avoid)
df.shape          # (891, ...)
df.dropna()       # drops any row with at least one NaN
df.dropna().shape # (182, ...)

#column-wise deletion (appropriate)
df.dropna(axis=1)  # drops entire columns that contain any NaN

#IMPUTATION
#mean
sns.histplot(df['age'], kde=True)  # check distribution shape first
df['age_mean'] = df['age'].fillna(df['age'].mean())
#median
df['age_median'] = df['age'].fillna(df['age'].median())
#mode
df['embarked'].unique()          # e.g. array(['S', 'C', 'Q', nan], dtype=object)
df['embarked'].notna()           # boolean mask: True where value exists
mode_value = df['embarked'].mode()[0]   # most frequent category
df['embarked_mode'] = df['embarked'].fillna(mode_value)
# Verify no missing values remain
df['embarked_mode'].isnull().sum()   # 0

#Random Sample Imputation
random_sample = df['age'].dropna().sample(df['age'].isnull().sum(), random_state=0)
random_sample.index = df[df['age'].isnull()].index
df.loc[df['age'].isnull(), 'age_random'] = random_sample

#Prod-standard
from sklearn.impute import SimpleImputer
imputer = SimpleImputer(strategy='mean')  # or 'median', 'most_frequent', 'constant'
df['age'] = imputer.fit_transform(df[['age']])