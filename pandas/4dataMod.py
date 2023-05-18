import pandas as pd
import numpy as np
import seaborn as sns

s = pd.Series(range(10))
s[3] = np.nan
print(s, "\n", s.count(), "\n", s.size)
np.random.seed(2)
df = pd.DataFrame(np.random.randint(5, size=(4, 4)), dtype=float)
df.iloc[2, 3] = np.nan
print(df, "\n", df.count(), "\n", df.size)

titanic = sns.load_dataset("titanic")
print(titanic)
print(titanic.head())
print(titanic.size, '\n', titanic.count())
print(titanic['deck'].count())
print(titanic['deck'].size)
print(titanic['deck'].unique())
print(titanic['deck'].value_counts())
