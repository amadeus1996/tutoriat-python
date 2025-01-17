with open("parola.in") as f:
    sir = f.readline().rstrip("\n")
    k = int(f.readline())

n = len(sir)
lmax = [1] * n
ult = [-1] * n
for i in range(1, n):
    for j in range(i):
        if abs(ord(sir[i]) - ord(sir[j])) >= k and lmax[j] + 1 > lmax[i]:
            lmax[i] = lmax[j] + 1 
            ult[i] = j

maxValue = max(lmax)
count = lmax.count(maxValue)
i = lmax.index(maxValue)
sol = ""

while i != -1:
    sol += sir[i]
    i = ult[i]

print(sol[::-1])
if count > 1:
    print("solutia optima nu este unica")
else:
    print("solutia optima este unica")