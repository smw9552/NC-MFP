import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

A_x_list = [0,2,4,1,1,4]
A_y_list = [4,1,5,5,2,6]
A_x = np.array(A_x_list)
A_y = np.array(A_y_list)

B_x_list = [7,7,5,7,10,9]
B_y_list = [4,0,2,2,3,3]
B_x = np.array(B_x_list)
B_y = np.array(B_y_list)

finding_point = [5, 4]

plt.figure()
plt.scatter(A_x, A_y)
plt.scatter(B_x, B_y)
plt.scatter(finding_point[0], finding_point[1], marker='*')

plt.show()