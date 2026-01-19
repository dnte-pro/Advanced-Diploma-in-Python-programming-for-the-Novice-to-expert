import pandas as pd
import numpy as np

np_arr = np.array([1,2,3,4,5])
series_np =pd.Series(np_arr)
print(series_np)


series_list =pd.Series([10,20,30,40,50])
print(series_list)

di = {'First':100,'second':200,'Third':300}
series_dict = pd.Series(di)
print(series_dict)

scalar_value = 10
series_scalar = pd.Series(scalar_value)
print(series_scalar)