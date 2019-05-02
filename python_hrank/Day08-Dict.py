n = int(input())

lista = [input().split() for _ in range(n)]

dict = {k: v for k,v in lista}

while True:
    try:
        name = input()
        if name in dict:
            print(name + "=" + dict[name])
        else:
            print("Not found")

    except:
        break
