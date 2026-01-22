import numpy as np

my_arr = np.arange(20)
print(my_arr)

my_arr_reshaped = np.reshape(my_arr, (4, 5), order='F')
print(my_arr_reshaped)


my_list = list(my_arr)

print(my_list[1])
print(my_arr[1])