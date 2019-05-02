marksheet = []

for _ in range(0,int(input())):

    marksheet.append([input(), float(input())])

scores_unsorted = set([score for name, score in marksheet])
scores_list_unsorted = list(scores_unsorted)
scores_sorted = sorted(scores_list_unsorted)
second_lowest = scores_sorted[1]
names_scores = [name for name, score in sorted(marksheet) if score == second_lowest]

print('\n'.join(names_scores))
