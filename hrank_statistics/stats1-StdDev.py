from statistics import pstdev

n = int(input())
arr = [float(x) for x in input().split()]
stdev = round(pstdev(arr), 1)
print(stdev)
