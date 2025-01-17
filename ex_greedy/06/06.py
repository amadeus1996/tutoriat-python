with open("balanta.in") as f:
    n = int(f.readline())
    g = float(f.readline())
    greutati = []
    for index in range(n):
        greutati.append((float(f.readline()), index + 1))
        
greutati.sort(key = lambda x: x[0])
i = 0
n = len(greutati)
count = 0
sol = []

while i != n - 1:
    if abs(greutati[i][0] - greutati[i + 1][0]) <= g:
        count += 1
        sol.append((greutati[i][1], greutati[i + 1][1]))
        i += 1
    i += 1

print(count)
for pereche in sol:
    print(f"{pereche[0]} + {pereche[1]}")