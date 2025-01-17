def citire_matrice(nume_fisier):
    M = []
    with open(nume_fisier) as f:
        M.append([int(x) for x in f.readline().split()])
        n = len(M[0])

        for linie in f:
            aux = [int(x) for x in linie.split()]
            if len(aux) != n:
                return None
            M.append(aux)
            
    return M

# print(citire_matrice("matrice.in"))


# Punctul b)
def multimi(M, *indici):
    intersectie_negative = set() 
    reuniune_pozitive = set()
    index = indici[0]
    for elem in M[index]:
        if elem<0:
            intersectie_negative.add(elem)
        else: 
            sir = str(elem)
            if sir[0] == sir[-1]:
                reuniune_pozitive.add(elem)

    for i in indici:
        negative = set()
        pozitive = set()
        for elem in M[i]:
            if elem<0:
                negative.add(elem)
            else: 
                sir = str(elem)
                if sir[0] == sir[-1]:
                    pozitive.add(elem)
        intersectie_negative.intersection_update(negative)
        reuniune_pozitive = reuniune_pozitive.union(pozitive)
    return reuniune_pozitive, intersectie_negative

M = citire_matrice("matrice.in")
print(multimi(M,  0, 3))



# Punctu c)

reuniune = multimi(M, len(M)-1, len(M)-2, len(M)-3)[0]
print(*reuniune)
negative = multimi(M, 0, len(M)-1)[1]
print(len(negative))
