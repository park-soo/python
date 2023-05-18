import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

np.random.seed(0)
df1 = pd.DataFrame(np.random.randn(100, 3),
                   index=pd.date_range('1/1/2018', periods=100),
                   columns=['A', 'B', 'C']).cumsum()
df1.tail()
print(df1)
df1.plot()
plt.title("Pandas's Plot method usage")
plt.xlabel("time")
plt.ylabel("Data")
plt.show()

iris = sns.load_dataset("iris")    # 붓꽃 데이터
titanic = sns.load_dataset("titanic")    # 타이타닉호 데이터

df2 = iris.groupby(iris.species).mean()
df2.columns.name = "feature"

df2.plot.bar(rot=0)
plt.title("Feature average for species")
plt.xlabel("average")
plt.ylabel("species")
plt.ylim(0, 8)
plt.show()
