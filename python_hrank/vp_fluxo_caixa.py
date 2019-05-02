# VP = [parcela/(1.006)ˆprazo]
VP = 0
paym = 2000

for i in range(1, 81):
    VP = VP + (paym/(1.006)**i)

print(VP)
