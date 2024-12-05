def hanoi(n, start, stop, ajutor):
    if n == 1:
        print(f"Mutam discul {n} de pe tija {start} pe tija {stop}")
        return
    hanoi(n - 1, start, ajutor, stop)
    print(f"Mutam discul {n} de pe tija {start} pe tija {stop}")
    hanoi(n - 1, ajutor, stop, start)

def hanoi_tower():
    with open("exercitii/fisiere/hanoi.in") as f:
        n = int(f.readline())
        hanoi(n, 'A', 'C', 'B')

def NrXDivImp(L, st, dr, x):
    if st == dr:
        return L[st - 1] == x
    mid = (st + dr) // 2
    return NrXDivImp(L, st, mid, x) + NrXDivImp(L, mid + 1, dr, x)

# should check if the numbers are alternating
def AlternDivImp(L, st, dr):
    if st == dr:
        return 1
    if dr - st == 1:
        return L[st - 1] % 2 != L[dr - 1] % 2
        
    mid = (st + dr) // 2

    left = AlternDivImp(L, st, mid)
    right = AlternDivImp(L, mid + 1, dr)
    boundary = L[mid - 1] % 2 != L[mid] % 2
    return left and right and boundary

# hanoi_tower()

# print(NrXDivImp([2,5,1,5,3,5,5,5,7,6],9,10,5))

# print(AlternDivImp([1,2,2,1,2,3,4], 1, 5))