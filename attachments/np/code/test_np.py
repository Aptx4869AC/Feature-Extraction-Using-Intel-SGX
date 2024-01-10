# -*- coding: utf-8 -*-
# @Author: qiaohezhe
# @github: https://github.com/Aptx4869AC
# @Date: 2024/1/11

import os

os.environ['OMP_NUM_THREADS'] = '1'
import numpy as np

print(np.__file__)

arr = np.array([[1, 2, 3], [4, 5, 6]])
print(arr)


print("sum:", arr.sum())
print("mean:", arr.mean())
print("max:", arr.max())
print("min:", arr.min())


arr_T = arr.T
print(arr_T)
