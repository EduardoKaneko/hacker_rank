n = int(input())

arr = list(map(int, input().split()))

reverse = arr[::-1]

array = " ".join(str(x) for x in reverse)

print(array)


# THE SECOND WAY

print(" ".join(map(str, arr[::-1])))
