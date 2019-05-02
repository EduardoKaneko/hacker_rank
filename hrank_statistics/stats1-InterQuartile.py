from statistics import median

n = int(input())
arr = list(map(int, input().split()))
freq = list(map(int, input().split()))

data = []
for i in range(n):
    data += [arr[i]] * freq[i]

N = sum(freq)

data.sort()

if n%2 != 0:
    q1 = median(data[:N//2])
    q3 = median(data[(N//2)+1:])
else:
    q1 = median(data[:N//2])
    q3 = median(data[N//2:])

diff = round(float(U_Q3 - L_Q1), 1)
print(diff)
