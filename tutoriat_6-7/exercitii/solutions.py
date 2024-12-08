from queue import PriorityQueue

# EX 1
with open("input/galeti.in") as f:
    n = int(f.readline())
    t = [int(x) for x in f.readline().split()[:n]]
    C = int(f.readline())

t.sort(reverse = True)
sol = []

for galeata in t:
    if C - galeata >= 0:
        C -= galeata
        sol.append(galeata)

with open("galeti.out", "w") as g:
    if C == 0:
        for galeata in sol:
            g.write(f"{galeata} ")
    else:
        g.write("Imposibil")


# EX 2
with open("input/probleme.in") as f:
    n = int(f.readline())
    t = []
    index = 1
    for _ in range(n):
        aux = f.readline().split()
        t.append((int(aux[0]), int(aux[1]), index))
        index += 1

t.sort(key = lambda x: -x[1])
q = PriorityQueue()
i = 0
sol = []
curr_time = t[0][1] # set curr time to the maximum time
punctaj = 0
while curr_time > 0:
    while i < len(t) and t[i][1] == curr_time:
        q.put((-t[i][0], (t[i][1], t[i][2])))
        i += 1
    if q.empty():
        curr_time -= 1
        continue
    aux = q.get()
    sol.append((-aux[0], aux[1][0], aux[1][1]))
    punctaj += -aux[0]
    curr_time -= 1

with open("probleme.out", "w") as g:
    g.write(f"Punctaj maxim: {punctaj}\n")
    for problema in sol:
        g.write(f"Problema {problema[2]}: {problema[0]} {problema[1]}\n")


# EX 3
with open("input/spectacole.in") as f:
    t = []
    n = int(f.readline())
    for _ in range(n):
        aux = f.readline().split()
        t.append((int(aux[1][:-1]), aux[2], aux[4]))

t.sort(key = lambda x: x[2])
sol = [t[0]]

for spectacol in t[1:]:
    if spectacol[1] >= sol[-1][2]:
        sol.append(spectacol)

with open("spectacole.out", "w") as g:
    for spectacol in sol:
        g.write(f"Spectacol {spectacol[0]}: {spectacol[1]} - {spectacol[2]}\n")


# EX 4
with open("input/balanta.in") as f:
    n = int(f.readline())
    G = float(f.readline())
    t = []
    index = 1
    for _ in range(n):
        t.append((index, float(f.readline())))
        index += 1

t.sort(key = lambda x: x[1])
sol = []
i = len(t) - 1

while i >= 1:
    if abs(t[i][1] - t[i - 1][1]) <= G:
        sol.append((t[i - 1][0], t[i][0]))
        i -= 2
    else:
        i -= 1

with open("balanta.out", "w") as g:
    g.write(f"{len(sol)}\n")
    for pereche in sol:
        g.write(f"{pereche[0]} + {pereche[1]}\n")


# EX 5
with open("input/bijuterii.in") as f:
    aux = f.readline().split()
    m, n = int(aux[0]), int(aux[1])
    t = []
    for _ in range(m):
        t.append([float(x) for x in f.readline().split()[:n]])

sol = [t[m - 1].index(max(t[m - 1])) + 1]
suma = t[m - 1][sol[-1] - 1]

for i in range(m - 2, -1, -1):
    max_val = -1
    index = -1
    for j in range(n):
        if t[i][j] < t[i + 1][sol[-1] - 1] and t[i][j] > max_val:
            max_val = t[i][j]
            index = j + 1
    if index == -1:
        break
    suma += max_val 
    sol.append(index)

with open("bijuterii.out", "w") as g:
    if len(sol) != m:
        g.write("Imposibil")
    else:
        g.write(f"{suma}\n")
        for i in range(m):
            g.write(f"{i + 1} {sol[-(i + 1)]}\n")


# EX 6
with open("input/concurs.in") as f:
    n = int(f.readline()) + 1
    t = [int(x) for x in f.readline().split()[:n]]

t.sort()
suma = 0
for num in t:
    suma += (num / n)
    n -= 1

with open("concurs.out", "w") as g:
    g.write(f"{suma:.3f}")
