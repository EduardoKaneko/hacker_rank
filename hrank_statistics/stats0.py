# Stats Day 0

# Input: N (numbers of elements) and A (An array of N numbers)

# Expected Output: Mean, Median, Mode

import numpy as np 
from scipy import stats

size = int(input())
numbers = list(map(int, input().split()))

mean = np.mean(numbers)
median = np.median(numbers)
mode = stats.mode(numbers)

print(mean)
print(median)
print(float(mode[0]))