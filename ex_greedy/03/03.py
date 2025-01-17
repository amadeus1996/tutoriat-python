with open("bijuterii.in") as f:
    t = []
    aux = f.readline().split()
    m, n = int(aux[0]), int(aux[1])
    for _ in range(m):
        t.append([float(x) for x in f.readline().split()])

sol = [(m, t[m - 1].index(max(t[m - 1])) + 1)]
suma = t[sol[-1][0] - 1][sol[-1][1] - 1]

ok = 1
for i in range(m - 2, -1, -1):
    max_val = -1
    aux = t[sol[-1][0] - 1][sol[-1][1] - 1]
    for j in range(n):
        if t[i][j] > max_val and t[i][j] < aux:
            max_val = t[i][j]
            index = (i + 1, j + 1)
    if max_val != -1:
        suma += max_val
        sol.append(index)
    else:
        ok = 0
        print("Imposibil")
        break

if ok:
    print(suma)
    for x in sol[::-1]:
        print(*x)