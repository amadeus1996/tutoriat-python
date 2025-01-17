with open("cuvinte.in", "r") as f:
    n = int(f.readline())
    cuvinte = f.readline().split()[:n]

lmax = [1]*n 
prev = [-1]*n
for i in range(1, n):
    for j in range(i):
        if ord(cuvinte[i][0]) == ord(cuvinte[j][-1]) + 1 or ord(cuvinte[i][0]) == ord(cuvinte[j][-1]) - 1:
            if lmax[i] < lmax[j] + 1 :
                lmax[i] = lmax[j] + 1
                prev[i] = j

# print(lmax)
# print(prev)

sol = []
i = lmax.index(max(lmax))
while i != -1:
    sol.append(cuvinte[i])
    i = prev[i]
    
for cuv in cuvinte:
    if cuv not in sol:
        print(cuv, end = " ")