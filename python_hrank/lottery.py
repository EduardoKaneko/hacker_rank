import random
lottery =[]

for nround in range(0, 4):
        lottery = sorted(random.sample(range(1,61), 6))
        print("Jogo de 06 Números: {}".format(lottery))

for nround in range(0, 2):
        lottery = sorted(random.sample(range(1,61), 7))
        print("Jogo de 07 Números: {}".format(lottery))

for nround in range(0, 1):
        lottery = sorted(random.sample(range(1,61), 8))
        print("Jogo de 08 Números: {}".format(lottery))
