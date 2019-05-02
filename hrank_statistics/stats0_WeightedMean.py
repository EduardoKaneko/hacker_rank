# Stats Day 0

# Input: N (numbers of elements), A (An array of N numbers) and W (The weight of each number)

# Expected Output: Weighted Mean


# THE FIRST WAY:

size = int(input())
numbers = list(map(int, input().split()))
weights = list(map(int, input().split()))


w_mean = sum(x*y for x, y in zip(numbers, weights))/ sum(weights)
print(round(w_mean, 1))







# THE SECOND WAY:
size = int(input())
numbers = list(map(int, input().split()))
weights = list(map(int, input().split()))


sum_X = sum([a*b for a,b in zip(numbers,weights)])
print(round((sum_X/sum(weights)),1))