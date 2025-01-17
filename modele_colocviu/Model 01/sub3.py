# Punctul a)
with open("autori.in") as f:
    d = {}
    aux = f.readline().split()
    m = int(aux[0])
    n = int(aux[1])
    for _ in range(m):
        aux = f.readline().split(maxsplit = 1)
        id_autor = int(aux[0])
        nume_autor = aux[1].rstrip("\n")
        d[id_autor] = [nume_autor, {}]
    for _ in range(n):
        aux = f.readline().split(maxsplit = 4)
        id_autor = int(aux[0])
        id_carte = int(aux[1])
        an = int(aux[2])
        nr_pag = int(aux[3])
        nume_carte = aux[4].rstrip("\n")

        info_carte = an, nr_pag, nume_carte
        d[id_autor][1][id_carte] = info_carte

print(d, end = "\n\n")


# Punctul b)
def sterge_carte(t, id_carte):
    for autor in t:
        if id_carte in t[autor][1]:
            del t[autor][1][id_carte]
            return t[autor][0]
    return None

autor = sterge_carte(d, 111)
if autor != None:
    print(f"Cartea a fost scrisa de {autor}")
else:
    print("Cartea nu exista")
print(d, end = "\n\n")


# Punctul c)
def carti_autor(t, id_autor):
    if id_autor not in t:
        return None
    autor = t[id_autor][0]
    carti = sorted([carte for carte in t[id_autor][1].values()], key = lambda x: (x[0], -x[1], x[2]))
    return autor, carti

date = carti_autor(d, 11)
if date != None:
    print(date[0])
    for carte in date[1]:
        print(f"{carte[2]} {carte[0]} {carte[1]}")
else:
    print("cod incorect")
