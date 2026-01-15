import numpy as np

np_arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

np_cond = np_arr[np_arr > 3]
print(np_cond)
print(np_arr >3)