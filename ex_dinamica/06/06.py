with open("padure.in", "r") as f:
    t = []
    aux = f.readline().split()
    m, n = int(aux[0]), int(aux[1])
    for _ in range(m):
        t.append(tuple([int(x) for x in f.readline().split()[:n]]))

gmax = [[-1] * n for _ in range(m)]
gmax[0][-1] = t[0][-1]
for j in range(n - 2, -1, -1):
    if gmax[0][j + 1] >= 0 and t[0][j] + gmax[0][j + 1] >= 0:
        gmax[0][j] = t[0][j] + gmax[0][j + 1]
    else:
        break

for i in range(1, m):
    if gmax[i - 1][n - 1] >= 0 and t[i][n - 1] + gmax[i - 1][n - 1] >= 0:
        gmax[i][n - 1] = t[i][n - 1] + gmax[i - 1][n - 1]
    else:
        break

for i in range(1, m):
    for j in range(n - 2, -1, -1):
        val_max = max(gmax[i - 1][j + 1], gmax[i - 1][j], gmax[i][j + 1])
        if val_max >= 0 and t[i][j] + val_max >= 0: 
            gmax[i][j] = t[i][j] + val_max

sol = []
i = m - 1
j = gmax[i].index(max(gmax[i]))
sol.append((i + 1, j + 1))
print(f"maxim {gmax[i][j]} graunte pe traseul")
while i > 0 or j != n - 1:
    val_max = -1
    if i >= 1 and gmax[i - 1][j] >= val_max:
        val_max = gmax[i - 1][j]
        x, y = i - 1, j
    if j <= n - 2 and gmax[i][j + 1] >= val_max:
        val_max = gmax[i][j + 1]
        x, y = i, j + 1
    if i >= 1 and j <= n - 2 and gmax[i - 1][j + 1] >= val_max:
        val_max = gmax[i - 1][j + 1]
        x, y = i - 1, j + 1
    sol.append((x + 1, y + 1))
    i, j = x, y

for x in sol[::-1]:
    print(*x)
