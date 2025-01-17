with open("galeti.in") as f:
    n = int(f.readline())
    t = [int(x) for x in f.readline().split()[:n]]
    C = int(f.readline())

t.sort(reverse = True)
sol = []

for galeata in t:
    if C - galeata >= 0:
        C -= galeata
        sol.append(galeata)

if C == 0:
    for galeata in sol:
        print(galeata, end = " ")
else:
    print("Imposibil")