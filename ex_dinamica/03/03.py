with open("emisiuni.in") as f:
    t = []
    for linie in f:
        aux = linie.split(maxsplit = 4)
        ora_1 = (aux[0] if len(aux[0]) == 2 else "0" + aux[0]) + aux[1]
        ora_2 = aux[2] + aux[3]
        t.append((ora_1, ora_2, aux[4].rstrip("\n")))

t.sort(key = lambda x: x[1])
n = len(t)

start = t[0][0]
sfarsit = t[0][1]
durata = (int(sfarsit[:2]) * 60 + int(sfarsit[2:])) - (int(start[:2]) * 60 + int(start[2:]))
dmax = [0] * n
dmax[0] = durata
ult = [-1] * n

for i in range(1, n):
    for j in range(i - 1, -1, -1):
        start = t[i][0]
        sfarsit = t[i][1]
        durata = (int(sfarsit[:2]) * 60 + int(sfarsit[2:])) - (int(start[:2]) * 60 + int(start[2:]))
        if start >= t[j][1] and dmax[j] + durata > dmax[i]:
            dmax[i] = dmax[j] + durata 
            ult[i] = j

# print(dmax)
# print(ult)

i = dmax.index(max(dmax))
count = dmax.count(dmax[i])
sol = []
while i != -1:
    sol.append(t[i])
    i = ult[i]
for post in sol[::-1]:
    print(f"[{post[0][1] if post[0][0] == "0" else post[0][:2]}:{post[0][2:]}, {post[1][1] if post[1][0] == "0" else post[1][:2]}:{post[1][2:]}) {post[2]}")

print("solutia nu este unica" if count > 1 else "solutia este unica")
        