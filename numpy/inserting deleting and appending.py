import numpy as np

np_arr = np.array([[1,2],  [6,8]])
print(np_arr)
print(np_arr.shape)

np_arr = np.insert(arr=np_arr, obj=1, values=[3,4], axis=0)
print(np_arr)


# delete array
np_arr_delete = np.delete(arr=np_arr, obj=1, axis=1)
print(np_arr_delete)

#append array
np_arr_append = np.append(arr=np_arr, values=[[9,10]], axis=0)
print(np_arr_append)