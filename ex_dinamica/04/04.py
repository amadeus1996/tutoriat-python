with open("tabla.in") as f:
    n = int(f.readline())
    M = []
    for _ in range(n):
        M.append([int(x) for x in f.readline().split()[:n]])
    poz = f.readline().split()
    xc, yc = int(poz[0]), int(poz[1])
xc -= 1
yc -= 1

# daca incepem de pe linia i, nu avem nevoie de liniile cu index_linie < i.
# le stergem
for i in range(xc):
    del M[i]
nrLinii = len(M)

pmax = [[0 for _ in range(n)] for _ in range(nrLinii)]
pmax[-1] = M[-1]
mutari = (1, -2), (1, 2), (2, -1), (2, 1) # cele 4 mutari posibile pt cal

sol = []
for i in range(nrLinii - 2, -1, -1):
    for j in range(n):
        for mutare in mutari:
            x = i + mutare[0]
            y = j + mutare[1]
            if 0 <= x < nrLinii and 0 <= y < n:
                if pmax[x][y] >= pmax[i][j]:
                    pmax[i][j] = pmax[x][y]
        pmax[i][j] += M[i][j]

# for linie in pmax:
    # print(*linie)

print(f"Maxim {pmax[xc][yc]} pioni")
sol = [(xc + 1, yc + 1)]
while xc != nrLinii - 1:
    max_pioni = -1
    max_coord = (-1, -1)
    for mutare in mutari:
        x = xc + mutare[0]
        y = yc + mutare[1]
        if 0 <= x < n and 0 <= y < n and pmax[x][y] > max_pioni:
            max_pioni = pmax[x][y]
            max_coord = x, y
    xc, yc = max_coord[0], max_coord[1]
    sol.append((xc + 1, yc + 1))

for poz in sol:
    print(*poz)
