import numpy as np
from sklearn.model_selection import KFold

x = np.array([[1,2],[3,4],[1,2],[3,4]])
y = np.array([1,2,3,4])
kf = KFold(n_splits=2)

print(kf.get_n_splits(x))

print(kf)

for train_index, test_index in kf.split(x):
    print("TRAIN:", train_index, "TEST:", test_index)
    x_train, x_test = x[train_index], x[test_index]
    y_train, y_test = y[train_index], y[test_index]

