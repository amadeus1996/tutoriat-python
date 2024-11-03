# EX 1
n = 1932
d = 2
t = {}
while n > 1:
    count = 0
    while n % d == 0:
        n /= d
        count += 1
    if count:
        t[d] = count
    d += 1
print(t, end = "\n\n")


# EX 2
t = {}
sir = "teste programare teste"
for cuv in sir.split():
    t[cuv] = t.get(cuv, {})
    for litera in cuv:
        t[cuv][litera] = t[cuv].get(litera, 0) + 1
print(f"{t}\n")


# EX 3
nums = [50, 21, 13, 84, 50, 60]
t = {}
for num in nums:
    aux = []
    # for i in range(2, (num >> 1) + 1)
    for i in range(2, num // 2 + 1):
        if num % i == 0:
            aux.append(i)
    t[num] = tuple(aux)
print(t, end = "\n\n")


# EX 4
nums1 = {10, 20, 14}
nums2 = ([10, 11, 10], [20, 20, 40], [5], [10, 11])
n = len(nums2)
t = {}
for num in nums1:
    t[num] = []
    for i in range(n):
        aux = nums2[i].count(num)
        if aux:
            t[num].append((i, aux))
print(f"{t}\n")


# EX 5
nums = [82375, 201, 51, 73, 3456, 2855, 1021, 90, 153]
t = {}
for num in nums:
    aux = sum([int(x) for x in str(num)]) / len(str(num))
    if aux not in t:
        t[aux] = []
    t[aux].append(num)
for medie in t:
    t[medie].sort(reverse = True)
print(t, end = "\n\n")


# EX 6
nums = [1011, 234, 8158558, 234]
t = {}
for num in nums:
    if num not in t:
        t[num] = []
        for cifra in set(str(num)):
            t[num].append((int(cifra), str(num).count(cifra)))
print(t, end = "\n\n")


# EX 7
sir = "asa merem palindrom "
t = {}
vowels = set("aeiouAEIOU")
for cuv in sir.split():
    if cuv == cuv[::-1]:
        aux = [c for c in cuv if c in vowels]
        # if (len(aux) << 1) >= len(cuv):   
        if len(aux) >= len(cuv) - len(aux):
            t[cuv] = list(set(aux))
        else:
            t[cuv] = list({c for c in cuv if c not in set(aux)})
print(t)


# EX 8
with open("text.in") as f:
    t = {}
    count = 0
    for linie in f:
        for cuv in linie.split():
            for litera in cuv:
                if litera.isalpha():
                    count += 1
                    t[litera.lower()] = t.get(litera.lower(), 0) + 1

with open("text.out", "w") as g:
    for key in t:
        g.write(f"{key}: {t[key] / count:.3f}\n")


# EX 9
with open("numere.in") as f:
    t = [[int(x) for x in linie.split()] for linie in f]

min_length = len(t[0])
for lista in t:
    min_value = min(lista)
    i, n = 0, len(lista)
    while i < n:
        if lista[i] == min_value:
            del lista[i]
            n -= 1
        else:
            i += 1
    if n < min_length:
        min_length = n

with open("numere.out", "w") as g:
    for lista in t:
        del lista[min_length:]
        for num in lista:
            g.write(f"{num} ")
        g.write("\n")
