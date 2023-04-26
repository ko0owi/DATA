import random

def make_2xlist():
    list = []
    list_1 = []
    list_2 = []
    list_3 = []
    list_4 = []
    list_5 = []
    list_6= []

    for _ in range (6):
        a = random.randrange(-1,11)
        list_1.append(a)


    for _ in range (6):
        a = random.randrange(-1,11)
        list_2.append(a)

    for _ in range(6):
        a = random.randrange(-1, 11)
        list_3.append(a)

    for _ in range(6):
        a = random.randrange(-1, 11)
        list_4.append(a)

    for _ in range(6):
        a = random.randrange(-1, 11)
        list_5.append(a)

    for _ in range(6):
        a = random.randrange(-1, 11)
        list_6.append(a)

    list.append(list_1)
    list.append(list_2)
    list.append(list_3)
    list.append(list_4)
    list.append(list_5)
    list.append(list_6)
    print(list)

    suma = 0
    for i in range (0,6,2):
        for j in range (0,6,2):
            #print(list[i][j])
            suma += list[i][j]
    print(f"Suma liczb parzystych wierwszy i kolumn to =  {suma} ")

# w pythone indexuje sie od zera w Lua od 1

make_2xlist()