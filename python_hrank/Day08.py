n = int(input())

#Building the dictionary with user's input
for i in range(0, n):
    key, value = input().split()
    my_dict[key] = value

#Printing only what the user want
for k, v in my_dict:
    name = input()
    if name in my_dict:
        print(k + "=" + v)
    elif name not in my_dict:
        print("Not found")

        