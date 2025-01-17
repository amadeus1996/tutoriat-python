def modifica_prefix(x,y,prop):
    L=[cuv for cuv in prop.split()]
    nrcuv=0
    k=len(x)
    for i in range(len(L)):
        # if L[i][:k]==x:
        if L[i].startswith(x):
            # L[i]=y+L[i][k:]
            L[i] = L[i].replace(x, y, 1)
            nrcuv+=1
    
    return " ".join(L),nrcuv

print(modifica_prefix("cu", "F", "cun sir de cuvicunte"))


# Punctul b)

def poz_max(lista):
    # maxim=max(lista)
    # sol = []
    # for i in range(len(lista)):
        # if lista[i]==maxim:
            # sol.append(i+1)
    # return sol
    return [i + 1 for i in range(len(lista)) if lista[i] == max(lista)]

print(poz_max([1,4,2,2,4,2,2,4]))


# Punctul c)
cuv1 = "cea"
cuv2 = "ca"
with open("propozitii.in") as f:
    sir = f.readlines()
    
with open("propozitii_modificate.out", "w") as f:
    nr_max = -1
    sol = []
    # for prop in sir:
    for i in range(len(sir)):
        sir1, nrcuv = modifica_prefix(cuv1, cuv2, sir[i])
        if nrcuv > nr_max:
            nr_max = nrcuv
            sol.clear()
            sol.append(i+1)
        elif nr_max == nrcuv:
            sol.append(i+1)
        f.write(f"{sir1}\n")

print(*sol)

            
