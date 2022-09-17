
import numpy as np
import matplotlib.pyplot as plt
X=np.array([[2,1],[1,2],[2,2],[3,2],[2,3],[3,3],[2,4],[3,5],[4,4],[5,3]])
plt.scatter(X[:,0],X[:,1],marker='o')
plt.show()
print(X)

import numpy as np
import matplotlib.pyplot as plt
X = np.array([[2, 1], [1, 2], [2, 2], [3, 2], [2, 3], [3, 3], [2, 4], [3, 5], [4, 4], [5, 3]])
from sklearn.cluster import KMeans
x_init = np.array([[2, 1], [1, 2]])
y_pred = KMeans(n_clusters=2, max_iter=1, init=x_init).fit_predict(X)
plt.scatter(X[:, 0], X[:, 1], c=y_pred)
plt.show()
# 第一次迭代结果：
x_init = np.array([[3.16, 2.5], [2, 3.5]])
y_pred = KMeans(n_clusters=2, max_iter=1, init=x_init).fit_predict(X)
print(y_pred)
plt.scatter(X[:, 0], X[:, 1], c=y_pred)
plt.show()

# 计算矩阵：
import math
m1_x = 0.0
m1_y = 0.0
m2_x = 0.0
m2_y = 0.0
for i, y in enumerate(y_pred):
    if not y:
        m1_x += X[i][0]
        m1_y += X[i][1]
    else:
        m2_x += X[i][0]
        m2_y += X[i][1]
m1_x = m1_x / y_pred[y_pred == 0].size
m1_y = m1_y / y_pred[y_pred == 0].size
m2_x = m2_x / y_pred[y_pred == 1].size
m2_y = m2_y / y_pred[y_pred == 1].size
print("M1':" , m1_x, m1_y, "M2':" , m2_x, m2_y)
for i, x in enumerate(X):
    print(math.sqrt(math.pow(x[0] - m1_x, 2) + math.pow(x[1] - m1_y, 2)),
          math.sqrt(math.pow(x[0] - m2_x, 2) + math.pow(x[1] - m2_y, 2)))


print("**************************************************************")
x_init = np.array([[2, 1], [1, 2], [2, 2]])
y_pred = KMeans(n_clusters=3, max_iter=1, init=x_init).fit_predict(X)
plt.scatter(X[:, 0], X[:, 1], c=y_pred)
plt.show()
print(y_pred)
m1 = np.mean(X[np.where(y_pred == 0)], axis=0)
m2 = np.mean(X[np.where(y_pred == 1)], axis=0)
m3 = np.mean(X[np.where(y_pred == 2)], axis=0)
print("M1':", m1, "M2':", m2, "M3':", m3)

y_pred = KMeans(n_clusters=3, max_iter=2, init=x_init).fit_predict(X)
plt.scatter(X[:, 0], X[:, 1], c=y_pred)
plt.show()
m1 = np.mean(X[np.where(y_pred == 0)], axis=0)
m2 = np.mean(X[np.where(y_pred == 1)], axis=0)
m3 = np.mean(X[np.where(y_pred == 2)], axis=0)
print("M1':", m1, "M2':", m2, "M3':", m3)

y_pred = KMeans(n_clusters=3, max_iter=3, init=x_init).fit_predict(X)
plt.scatter(X[:, 0], X[:, 1], c=y_pred)
plt.show()
m1 = np.mean(X[np.where(y_pred == 0)], axis=0)
m2 = np.mean(X[np.where(y_pred == 1)], axis=0)
m3 = np.mean(X[np.where(y_pred == 2)], axis=0)
print("M1':", m1, "M2':", m2, "M3':", m3)