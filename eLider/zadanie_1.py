
"""select sort"""
def s_sort (l):
    for a in range (len(l) -1):
        min = a
        for b in range(a,len(l)):
            if l [b] < l [min]:
                min = b
        l[a], l[min] = l[min], l[a]
    return (l)


"""bouble sort"""
def b_sort(l):
    for i in range (len(l)-1,0,-1):
        for j in range(i):
            if l[j] > l[j+1]:
                l[j], l[j+1] = l[j+1], l[j]
    return (l)

"""program sortuje i podaje 2 co do wielkośći liczbę"""
def second_number_of_list(l):
    s_sort(l)
    #b_sort(l)
    unique = []
    for item in l:
        if item not in unique:
            unique.append(item)
    return print( unique[-2] )


second_number_of_list([1,4,6,8,3,4,6,2,6,6,0,0,-1])

