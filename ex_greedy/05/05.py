with open("nuferi.in", "r") as f:
    nuferi = [int(x) for x in f.readline().split()]

sol = [1]
n = len(nuferi)
poz = 0
while poz < n - 1:
    dmax = poz + nuferi[poz]
    if dmax >= n - 1:
        sol.append(n)
        break
    aux = poz 
    for i in range(poz + 1, dmax + 1):
        if i + nuferi[i] > aux + nuferi[aux]:
            aux = i
    poz = aux 
    sol.append(poz + 1)

print(sol)