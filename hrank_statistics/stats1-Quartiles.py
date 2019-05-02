# Stats Day 1: Quartiles

# Input: n (numbers of elements), X (An array of n numbers).

# Expected Output: 1st quartile (25%), 2nd quartile (median, 50%) and 3rd quartile (75%)

# Importando a função que calcula a mediana da biblioteca statistics
from statistics import median

# Armazenando n como inteiro
n = int(input())

# Criando a partir da array, uma lista de inteiros
arr = [int(x) for x in input().split()]

# Ordenando a lista de inteiros
arr.sort()

# Criando a variável que divide os dados ao meio.
# Se n for ímpar, (Ex: n=9), t = 4:
    # 9/2 = 4,5. Mas a função int() trunca o número, descartando tudo depois da vírgula.
    # A mediana seria o X(5).
    # Mas o t se refere ao índice para acessar a lista em python.
    # Como python começa com índice 0, ou seja, o primeiro elemento é lista[0],
    # O índice para acessar a lista será sempre -1 se comparado às operações matemáticas
    # Portanto, lista[4] = X(5) = Mediana
# Se for par, (Ex: n = 8):
    # Matematicamente, a mediana seria (X(4) + X(5))/2
    # Em python, a mediana seria (lista[3] + lista[4])/2
i = int(len(arr)/2)

# Se o resto da divisão de n/2 for igual a zero, ou seja, se n for par: (Ex: n = 8)
    # A primeira metade da lista será do índice zero até o índice t.

if n%2==0:
    # n = 8, i = 4 lista = [1, 2, 3, 4, 5, 6, 7, 8]
    L=arr[:i] # Lower = [1, 2, 3, 4, 5]
    U=arr[i:] # Upper = [5, 6, 7, 8]
else:
    # n = 9, i = 4 lista = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    L=arr[:i] # Lower = [1, 2, 3, 4, 5]
    U=arr[i+1:]  # Upper = [6, 7, 8, 9]

print(int(median(L)))
print(int(median(arr)))
print(int(median(U)))
