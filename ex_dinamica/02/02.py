with open("sir.in") as f:
    t = [int(x) for x in f.readline().split()]

n = len(t)
lmax = [1] * n 
ult = [-1] * n
for i in range(1, n):
    for j in range(i - 1, -1, -1):
        if t[j] < t[i] and lmax[j] + 1 > lmax[i]:
            lmax[i] = lmax[j] + 1
            ult[i] = j

print(lmax)
print(ult)

i = lmax.index(max(lmax))
sol = []
while i != -1:
    sol.append(t[i])
    i = ult[i]
print(sol[::-1])
