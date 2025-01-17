with open("statiune.in", "r") as f:
    n = int(f.readline())
    matrice = []
    for _ in range(n):
        matrice.append([int(x) for x in f.readline().split()])

omax = [[-1] * n for _ in range(n)]
omax[0] = matrice[0]

val_max = -1
coord_max = (-1, -1)
for i in range(1, n):
    for j in range(n):
        aux = omax[i - 1][j]
        if j > 0 and omax[i - 1][j - 1] > aux:
            aux = omax[i - 1][j - 1]
        if j < n - 1 and omax[i - 1][j + 1] > aux:
            aux = omax[i - 1][j + 1]
        if matrice[i][j] == -1:
            omax[i][j] = -aux
            if aux > val_max:
                val_max = aux 
                coord_max = i, j
        else:
            omax[i][j] = aux + matrice[i][j]

for linie in omax:
    print(*linie)

print(f"Gradul de oboseala maxim {-omax[coord_max[0]][coord_max[1]]}")   
sol = [(coord_max[0] + 1, coord_max[1] + 1)]
i, j = coord_max 
while i != 0:
    aux = omax[i - 1][j]
    coord = i - 1, j
    if j > 0 and omax[i - 1][j - 1] > aux:
        aux = omax[i - 1][j - 1]
        coord = i - 1, j - 1
    if j < n - 1 and omax[i - 1][j + 1] > aux:
        aux = omax[i - 1][j + 1]
        coord = i - 1, j + 1
    sol.append((coord[0] + 1, coord[1] + 1))
    i, j = coord[0], coord[1]

for coord in sol[::-1]:
    print(*coord)
