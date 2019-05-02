n = int(input())

for word in range(0, n):
    word = str(input())
    even = word[::2]
    odd = word[1::2]
    print(even, odd)
print("Este exercício está servindo de teste para aprendizagem em git e github!")
