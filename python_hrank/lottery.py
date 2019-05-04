import random
lottery =[]

for nround in range(0, 21):
        lottery = sorted(random.sample(range(1,61), 6))
        print(lottery)