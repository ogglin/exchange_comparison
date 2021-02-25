from multiprocessing import Pool
from timeit import default_timer as timer
import numpy as np


def createandsort(n):
    rand = np.random.RandomState(42)  # Give a seed to reproduce results
    a = rand.rand(n)  # Generate an array of size n
    return a.sort()  # Sort the array


# Create sizes for 3 arrays.
sizes = [10 ** 1 for i in range(0, 3)]  # Size of each array is 10 here.
# Applying the function sequentially
tic = timer()
[createandsort(size) for size in sizes]
tac = timer()
print("time for sequential sorting: ", tac - tic)
# Using multiprocessing
if __name__ == "__main__":
    pool = Pool(processes=3)
    tic = timer()
    pool.map(createandsort, sizes)
    tac = timer()
    print("time for parallel sorting: ", tac - tic)
