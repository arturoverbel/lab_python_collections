from collections import deque
import numpy as np
from time import time
import matplotlib.pyplot as plt

num_elements = [10, 100, 1000, 10000, 100000]

deque_pop_times = [0, 0, 0, 0, 0]
deque_append_times = [0, 0, 0, 0, 0]

array_pop_times = [0, 0, 0, 0, 0]
array_append_times = [0, 0, 0, 0, 0]

for idx, num_total in enumerate(num_elements):
    array = []
    t = time()
    while len(array) > num_total:
        array.append(5)
    array_append_times[idx] = time() - t

for idx, num_total in enumerate(num_elements):
    arrayDeque = deque(array)
    t = time()
    while len(arrayDeque) < num_total:
        arrayDeque.append(5)
    deque_append_times[idx] = time() - t


for idx, num_total in enumerate(num_elements):
    array = [1] * num_total
    t = time()
    while len(array) > 0:
        array.pop(0)
    array_pop_times[idx] = time() - t

for idx, num_total in enumerate(num_elements):
    arrayDeque = deque([1] * num_total)
    t = time()
    while len(arrayDeque) > 0:
        arrayDeque.pop()
    deque_pop_times[idx] = time() - t


print(array_append_times)
print(deque_append_times)
print(array_pop_times)
print(deque_pop_times)
