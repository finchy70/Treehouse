def combo(a, b):
    list_of_tuple=[]
    count = 0
    for letter in a:
        list_of_tuple.append(tuple([a[count], b[count]]))
        count += 1
    return list_of_tuple











print(combo("Paul", "Finc"))