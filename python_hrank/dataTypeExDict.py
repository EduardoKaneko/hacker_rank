n = int(input())

d = {}

for x in range(n):
    new_key = input()
    new_grade = round(float(input()), 1)
    d[new_key] = new_grade

# Create a list of tuples sorted by index 1 i.e. value field
listofTuples = sorted(d.items() , reverse=False, key=lambda x: x[1])
sequence = []

# Iterate over the sorted sequence
for elem in listofTuples :
    sequence.append(elem[0])

sort = sorted(sequence[:2])

if elem[0] in listofTuples == elem[0]:
    for name in sort:
        print(name)
else:
    print(sort[1])
