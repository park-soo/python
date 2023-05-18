#https://matplotlib.org/stable/index.html#
import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.pylab as plb
import numpy as np

# plt.title("Plot")
# plt.plot([1, 4, 9, 16])
# plt.show()

# plt.title("x ticks")
# plt.plot([10, 20, 30, 40], [1, 4, 9, 16])
# plt.show()


# plt.title('title')
# plt.plot([10, 20, 30, 40], [1, 4, 9, 16],'rs--')
# plt.xlabel("x axis label")
# plt.ylabel("y axis label")
# plt.show()
'''
color
blue:b / green:g / red:r / cyan:c / magenta:m / yellow:y
black:k / white:w
marker
.:point marker / ,:pixel marker / o:circle marker /
v:triangle_down marker / ^:triangle_up marker / 
<:triangle_left marker / >:triangle_right marker / 
1:tri_down marker / 2:tri_up marker / 
3:tri_left marker / 4:tri_right marker /
s:square marker / p:pentagon marker /
*:star marker / h:hexagon1 marker / H:hexagon2 marker /
+:plus marker / x:x marker / D:diamond marker /
d:thin_diamond marker / 
line style
- : solid line style / -- : dashed line style
-. : dash-dot line style / : : dotted line style
attribute
c:선 색깔
lw:선 굵기
ls:선 스타일
marker:마커 종류
ms:마커 크기
mec:마커 선 색깔
mew:마커 선 굵기
mfc:마커 내부 색깔
'''
# plt.plot([10, 20, 30, 40], [1, 4, 9, 16], c="b",
#          lw=5, ls="--", marker="o", ms=15, mec="g", mew=5, mfc="r")
# plt.title("style example")
# plt.show()

# plt.title("x axis, y axis range setting")
# plt.plot([10, 20, 30, 40], [1, 4, 9, 16],
#          c="b", lw=5, ls="--", marker="o", ms=15, mec="g", mew=5, mfc="r")
# plt.xlim(0, 50)
# plt.ylim(-10, 30)
# plt.show()

# t = np.arange(0., 5., 0.2)
# plt.title("multiple line draw in line plot")
# plt.plot(t, t, 'r--', t, 0.5 * t**2, 'bs:', t, 0.2 * t**3, 'g^-')
# plt.show()

# plt.title("multi plot ")
# plt.plot([1, 4, 9, 16],
#          c="b", lw=5, ls="--", marker="o", ms=15, mec="g", mew=5, mfc="r")
# plt.plot([9, 16, 4, 1],
#          c="k", lw=3, ls=":", marker="s", ms=10, mec="m", mew=5, mfc="c")
# plt.show()

# X = np.linspace(-np.pi, np.pi, 256)
# C, S = np.cos(X), np.sin(X)
# plt.title("show legend")
# plt.plot(X, C, ls="--", label="cosine")
# plt.plot(X, S, ls=":", label="sine")
# plt.legend(loc=2)
# plt.show()

# y = [2, 3, 1]
# x = np.arange(len(y))
# xlabel = ['A', 'B', 'C']
# plb.title("Bar Chart")
# plb.bar(x, y)
# plb.xticks(x, xlabel)
# plb.yticks(sorted(y))
# plb.xlabel("ABC")
# plb.ylabel("TIMES")
# plb.show()

# labels = ['frog', 'pig', 'dog', 'tree']
# sizes = [15, 30, 45, 10]
# colors = ['yellowgreen', 'gold', 'lightskyblue', 'lightcoral']
# explode = (0, 0.1, 0, 0)
# plb.title("Pie Chart")
# plb.pie(sizes, explode=explode, labels=labels, colors=colors,
#         autopct='%1.1f%%', shadow=True, startangle=90)
# plb.axis('equal')
# plb.show()

# np.random.seed(0)
# x = np.random.randn(1000)
# plt.title("Histogram")
# arrays, bins, patches = plt.hist(x, bins=10)
# plt.show()
# print(arrays)
# print(bins)

# np.random.seed(0)
# X = np.random.normal(0, 1, 100)
# Y = np.random.normal(0, 1, 100)
# plt.title("Scatter Plot")
# plt.scatter(X, Y)
# plt.show()

#버블 차트(bubble chart)
#  데이터가 2차원이 아니라 3차원 혹은 4차원인 경우에는 점 하나의 크기 혹은 색깔을 이용하여 다른 데이터 값을 표시
#  크기는 s 인수로 색깔은 c 인수로 지정
# N = 30
# np.random.seed(0)
# x = np.random.rand(N)
# y1 = np.random.rand(N)
# y2 = np.random.rand(N)
# y3 = np.pi * (15 * np.random.rand(N))**2
# plt.title("Bubble Chart")
# plt.scatter(x, y1, c=y2, s=y3)
# plt.show()

#pip install -U scikit-learn
from sklearn.datasets import load_digits
digits = load_digits()
X = digits.images[0]
print(X)

#imshow
#화상(image) 데이터처럼 행과 열을 가진 행렬 형태의 2차원 데이터는 imshow 명령을 써서 2차원 자료의 크기를 색깔로 표시
# plt.title("mnist digits; 0")
# plt.imshow(X, interpolation='nearest', cmap=plt.cm.bone_r)
# plt.xticks([])
# plt.yticks([])
# plt.grid(False)
# plt.subplots_adjust(left=0.35, right=0.65, bottom=0.35, top=0.65)
# plt.show()


#contour plot
#입력 변수가 x, y 두 개이고 출력 변수가 z 하나인 경우인 3차원 자료를 시각화하는 방법으로
#명암이 아닌 등고선(contour)을 사용하는 방법
# def f(x, y):
#     return (1 - x / 2 + x ** 5 + y ** 3) * np.exp(-x ** 2 - y ** 2)

# n = 256
# x = np.linspace(-3, 3, n)
# y = np.linspace(-3, 3, n)
# XX, YY = np.meshgrid(x, y)
# ZZ = f(XX, YY)

# plt.title("Contour plots")
# plt.contourf(XX, YY, ZZ, alpha=.75, cmap='jet')
# plt.contour(XX, YY, ZZ, colors='black')
# plt.show()

#3차원 플롯
#차원 플롯은 등고선 플롯과 달리 Axes3D라는 3차원 전용 axes를 생성하여 입체적으로 표시
from mpl_toolkits.mplot3d import Axes3D
# X = np.arange(-4, 4, 0.25)
# Y = np.arange(-4, 4, 0.25)
# XX, YY = np.meshgrid(X, Y)
# RR = np.sqrt(XX**2 + YY**2)
# ZZ = np.sin(RR)

# fig = plt.figure()
# ax = Axes3D(fig)
# ax.set_title("3D Surface Plot")
# ax.plot_surface(XX, YY, ZZ, rstride=1, cstride=1, cmap='hot')
# plt.show()

# 삼각 그리드(triangular grid)
import matplotlib.tri as mtri

x = np.array([0, 1, 2])
y = np.array([0, np.sqrt(3), 0])
triangles = [[0, 1, 2]]
triang = mtri.Triangulation(x, y, triangles)
plt.title("triangle grid")
plt.triplot(triang, 'ko-')
plt.xlim(-0.1, 2.1)
plt.ylim(-0.1, 1.8)
plt.show()

x = np.asarray([0, 1, 2, 3, 4, 2])
y = np.asarray([0, np.sqrt(3), 0, np.sqrt(3), 0, 2*np.sqrt(3)])
triangles = [[0, 1, 2], [2, 3, 4], [1, 2, 3], [1, 3, 5]]
triang = mtri.Triangulation(x, y, triangles)
plt.title("multiple triangle grid")
plt.triplot(triang, 'ko-')
plt.xlim(-0.1, 4.1)
plt.ylim(-0.1, 3.7)
plt.show()

refiner = mtri.UniformTriRefiner(triang)
triang2 = refiner.refine_triangulation(subdiv=2)
plt.title("gird segmentation")
plt.triplot(triang2, 'ko-')
plt.xlim(-0.1, 4.1)
plt.ylim(-0.1, 3.7)
plt.show()

triang5 = refiner.refine_triangulation(subdiv=5)
z5 = np.cos(1.5*triang5.x)*np.cos(1.5*triang5.y)
plt.title("3 demantion data visualization in triangle grid")
plt.tricontourf(triang5, z5, cmap="gray")
plt.show()

from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm

triang3 = refiner.refine_triangulation(subdiv=3)
z3 = np.cos(1.5 * triang3.x) * np.cos(1.5 * triang3.y)

fig = plt.figure()
ax = fig.gca( projection='3d')
ax.set_title("3D Surface Plot in triangle grid")
ax.plot_trisurf(triang3.x, triang3.y, z3, cmap=cm.jet, linewidth=0.2)
ax.tricontourf(triang3, z3, zdir='z', offset=-1.2, cmap=cm.coolwarm)
ax.set_zlim(-1, 1)
ax.view_init(40, -40)
plt.show()
