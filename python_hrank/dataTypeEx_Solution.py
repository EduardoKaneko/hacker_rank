# Criando uma lista vazia
marksheet = []

# Para cada "coisa" no intervalo de {0:N}
for _ in range(0,int(input())):
    # Adicione o primeiro input "name",
    # Adicione o segundo input "score" como float
    marksheet.append([input(), float(input())])

# Scores não ordenados e sem repetição, do tipo set()
# Score é o que eu quero colocar na lista, poderia fazer assim: scores_unsorted.append(score)
# Para nomes e score em marksheet, adicione só os scores não repetidos.
scores_unsorted = set([score for name, score in marksheet])

# Transformando em lista
scores_list_unsorted = list(scores_unsorted)

# Ordenando a lista
scores_sorted = sorted(scores_list_unsorted)

# Pegando só o segundo elemento da lista ordenada (O segundo pior)
second_lowest = scores_sorted[1]

# Para nomes e scores na lista ordenada pelos nomes em marksheet ([['Akriti', 41.0], ['Berry', 37.21]]):
# Adicione "name" em names_score, APENAS se o score for igual ao score da lista second_lowest(que é a lista só dos scores)
names_scores = [name for name, score in sorted(marksheet) if score == second_lowest]
print('\n'.join(names_scores))

# OUTPUT: O NOME DO SEGUNDO PIOR
