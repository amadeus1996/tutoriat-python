def suma(L, st, dr):
    if st == dr:
        return L[st]
    mid = (st + dr) // 2
    return suma(L, st, mid) + suma(L, mid + 1, dr)

L = [i for i in range(100)]
print(suma(L, 0, len(L) - 1))