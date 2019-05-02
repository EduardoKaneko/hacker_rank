VP = 0
paym = 24000

for n in range(0, 81):
    VP = VP + (paym/(1.07)**n)
print(VP)
