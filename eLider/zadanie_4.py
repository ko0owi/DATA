tablica = [
    [0.12, 0.23, 0.17, 0.89, 1.00],
    [0.83, 0.25, 0.99, 0.46, 0.46],
    [0.21, 0.00, 0.63, 0.15, 0.71],
    [0.19, 0.04, 0.23, 0.38, 0.30],
    [0.38, 0.93, 0.11, 0.53, 0.06],
]

"""Dla tablicy o równych bokach(podanej w przykładzie), lub dowolnej o rownych bokach"""
def values(t):
    red_line_numbers = []
    uderscore_numbers = []

    """lista numerów po przekątnej z czerwona linią"""
    for i in range(len(t)):
        red_line_numbers.append(t[i][i])

    """Lista numeró po przekątnej z podkreśleniem"""
    a = 4
    for i in range(len(t)):
        uderscore_numbers.append(t[i][a])
        a -= 1

    """MAX pierwszej przekątnej """
    for i in range (len(red_line_numbers)-2):
        max = i
        for j in range (i, len(red_line_numbers)):
             if red_line_numbers[j] > red_line_numbers[max]:
                 max = j
    max = red_line_numbers[max]

    """MIN 2 przekątnej"""
    for i in range (len(uderscore_numbers)-2):
        min = i
        for j in range (i, len(uderscore_numbers)):
             if uderscore_numbers[j] < uderscore_numbers[min]:
                 min = j
    min = uderscore_numbers[min]

    """Srednia z wartośći przekątnych"""
    result = (max + min ) / 2
    print(result)

"""cała tablica posortowana"""
def third_value():
    for x in range(len(tablica)):
        for i in range(len(tablica[x]) - 1, 0, -1):
            for j in range(i):
                if tablica[x][j] > tablica[x][j + 1]:
                    tablica[x][j], tablica[x][j + 1] = tablica[x][j + 1], tablica[x][j]

    """lista maxów"""
    list_max = []
    for i in range(len(tablica)):
        list_max.append(tablica[i][4])

    """posortowana lista maxów i wudruk 3 co do wielkości"""
    for i in range (len(list_max)-1,0,-1):
        for j in range(i):
            if list_max[j] > list_max[j+1]:
                list_max[j],list_max[j+1] = list_max[j+1],list_max[j]
    print(list_max)

values(tablica)
third_value()
