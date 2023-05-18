
import matplotlib as mpl
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

iris = sns.load_dataset("iris")    # 붓꽃 데이터
titanic = sns.load_dataset("titanic")    # 타이타닉호 데이터
tips = sns.load_dataset("tips")    # 팁 데이터
flights = sns.load_dataset("flights")    # 여객운송 데이터

#분포 플롯
x = iris.petal_length.values

sns.rugplot(x)
plt.title("Iris data,Rug Plot ")
plt.show()
sns.kdeplot(x)
plt.title("Iris data,Kernel Density Plot")
plt.show()
sns.distplot(x, kde=True, rug=True)
plt.title("Iris data, Dist Plot")
plt.show()

#카운트 플롯
sns.countplot(x="class", data=titanic)
plt.title("passenger count by class on titanic")
plt.show()

sns.countplot(x="day", data=tips)
plt.title("tip count per days")
plt.show()

#다차원 데이터
sns.jointplot(x="sepal_length", y="sepal_width", data=iris)
plt.suptitle("Joint Plot of The length and width", y=1.02)
plt.show()
sns.jointplot(x="sepal_length", y="sepal_width", data=iris, kind="kde")
plt.suptitle("Joint Plot and Kernel Density Plot of The length and width", y=1.02)
plt.show()

sns.pairplot(iris)
plt.title("Pair Plot of Iris Data")
plt.show()
sns.pairplot(iris, hue="species", markers=["o", "s", "D"])
plt.title("Iris Pair Plot, Hue visualization")
plt.show()

#카테고리 데이터
titanic_size = titanic.pivot_table(
    index="class", columns="sex", aggfunc="size")
print(titanic_size)
sns.heatmap(titanic_size, cmap=sns.light_palette(
    "gray", as_cmap=True), annot=True, fmt="d")
plt.title("Heatmap")
plt.show()

#2차원 복합데이터
sns.barplot(x="day", y="total_bill", data=tips)
plt.title("total tips")
plt.show()

sns.boxplot(x="day", y="total_bill", data=tips)
plt.title("Box Plot of Total tips")
plt.show()

sns.violinplot(x="day", y="total_bill", data=tips)
plt.title("Violin Plot of Total tips")
plt.show()

sns.stripplot(x="day", y="total_bill", data=tips, jitter=True)
plt.title("Strip Plot of total tips")
plt.show()

flights_passengers = flights.pivot("month", "year", "passengers")
plt.title("Heatmap of Yearly, monthly passenger number")
sns.heatmap(flights_passengers, annot=True, fmt="d", linewidths=1)
plt.show()

#스타일
def sinplot(flip=1):
    x = np.linspace(0, 14, 100)
    for i in range(1, 7):
        plt.plot(x, np.sin(x + i * .5) * (7 - i) * flip)
sns.set_style("ticks")
sinplot()
# sns.set_style("darkgrid")
# sinplot()
plt.show()
