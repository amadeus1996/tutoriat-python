# LIST COMPREHENSIONS
# a)
L1 = [chr(x) for x in range(ord('a'), ord('z') + 1)]
print(L1, end = "\n\n")

# b)
# L2 = [x * ((-1) ** (x - 1)) for x in range(1, int(input("n=")) + 1)]
n = 6
L2 = [x * ((-1) ** (x - 1)) for x in range(1, n + 1)]
print(L2, end = "\n\n")

# c)
nums = [9, 3, 4, 5, 1, 5, 2, 6, 7, 8, 2, 0, 1]
L3 = [x for x in nums if x & 1 == 1]
print(L3, end = "\n\n")

# d)
L4 = nums[1::2]
print(L4, end = "\n\n")

# e)
L5 = [nums[i] for i in range(len(nums)) if nums[i] & 1 == i & 1]
print(L5, end = "\n\n")

# f)
nums_2 = [1, 2, 3, 4]
L6 = [(nums_2[i], nums_2[i + 1]) for i in range(len(nums_2) - 1)]
print(L6, end = "\n\n")

# g)
L7 = [[f"{x}*{y}={x*y}" for x in range(1, n + 1)] for y in range(1, n + 1)]
for linie in L7:
    print(*linie)
print()

# h)
sir = "abcd"
L8 = [sir[i:] + sir[:i] for i in range(len(sir))]
print(L8, end = "\n\n")

# i)
L9 = [[i] * i for i in range(n)]
print(L9, end = "\n\n")


print("--------------------------------", end = "\n\n")
# SORTARI LISTE
# a)
numere = [13, 4892, 122, 15, 0, 692, 48]
print(sorted(numere, key = lambda x: str(x)), end = "\n\n")

# b)
print(sorted(numere, key = lambda x: str(x)[::-1]), end = "\n\n")

# c)
print(sorted(numere, key = lambda x: -len(str(x))), end = "\n\n")

# d)
print(sorted(numere, key = lambda x: len(set(str(x)))), end = "\n\n")

# e)
print(sorted(numere, key = lambda x: (len(str(x)), x)), end = "\n\n")


print("--------------------------------", end = "\n\n")
# OPERATII CU LISTE
# 1)
L1 = [3, 1, 4, 8, 6, 14]
L2 = [0, 5, 18, 2, 3, 9]
L1[0::2] = L2[0::2]
print(L1, end = "\n\n")


# 2)
L = [14, 5, 6, 0, 28, 3, 9, 9, 0, 0, 15, 0]
fst_zero_index = L.index(0)
snd_zero_index = L[fst_zero_index + 1:].index(0) + fst_zero_index + 1
del(L[fst_zero_index : snd_zero_index + 1])
print(L, end = "\n\n")


# 3)
n = len(L)
i = 0
while i < n:
    if L[i] == 0:
        del L[i]
        n -= 1
    else:
        i += 1
print(L, end = "\n\n")


# 4)
nums = [1, 2, 1, 0, 1, 1, 2, 2, 0, 1, 2, 1, 0, 1, 1, 2]
k = 4
min_sum_index = 0
min_sum = sum(nums[:k])
aux_sum = min_sum

for i in range(k, len(nums)):
    aux_sum -= nums[i - k]
    aux_sum += nums[i]
    if aux_sum < min_sum:
        min_sum = aux_sum 
        min_sum_index = i - k + 1

del nums[min_sum_index : min_sum_index + k]
print(nums, end = "\n\n")


# 5)
nums = [1, 1, 2, 3, 3, 4, 5, 5, 5, 5, 5, 6, 7, 7, 7, 7, 7, 7, 8]
print(list(set(nums)), end = "\n\n")


# 6)
nums = [-3.5, -3.2, 14, -1, 0, -1, 18, 20, 3.9, -0.1, -0.2, 2, -0.3]
i = 0
while i < len(nums):
    if nums[i] < 0:
        i += 1
        nums.insert(i, 0)
    i += 1

print(nums, end = "\n\n")


print("--------------------------------", end = "\n\n")
# SORTARI
# 1)
prop = "Aceasta a fost o propozitie scrisa intr-o perioada de timp"
print(" ".join(sorted([cuv for cuv in prop.split() if len(cuv) > 1], key = lambda x: -len(x))), end = "\n\n")


# 2)
v = [11, 45, 20, 810, 179, 81, 1000]
print(sorted(v, key = lambda x: (sum([int(c) for c in str(x)]), -x)), end = "\n\n")


# 3)
# a)
with open("elevi.in", "r") as f:
    n = int(f.readline())
    elevi = []
    for _ in range(n):
        aux = f.readline().split(maxsplit = 3)
        elevi.append([aux[0], aux[1], aux[2], [int(x) for x in aux[3].split()]])

print(elevi, end = "\n\n")

# b)
for i in range(len(elevi)):
    for nota in elevi[i][3]:
        if nota < 5:
            elevi[i].append(False)
            break 
    else:
        elevi[i].append(True)

print(elevi, end = "\n\n")

# c)
print(sorted(elevi, key = lambda x: (int(x[2]), x[0], x[1])), end = "\n\n")

# d)
print(sorted(elevi, key = lambda x: (-int(x[2]), x[4], (((sum(x[3]) / len(x[3])), x[0]) if x[4] == True else -len([y for y in x[3] if y < 5]))), reverse = True), end = '\n\n')

# e)
medie_maxima = max([sum(x[3]) / len(x[3]) for x in elevi])
for student in elevi:
    if sum(student[3]) / len(student[3]) == medie_maxima:
        print(student[0] + " " + student[1])
print()


# 4)
nums = [1, 8, 6, 5, 2, 3, 9, 1, 0, 4, 2, 6, 7, 5, 4, 8, 10]
print(sorted(nums, key = lambda x: (-(x & 1), x if (x & 1) else -x)), end = "\n\n")


print("--------------------------------", end = "\n\n")
# MATRICE, VECTORI
# 1)
matrice = [[i + j for i in range (1, 4)] for j in range(0, 9, 3)]
transpusa = [[matrice[i][j] for i in range(3)] for j in range(3)]
print(transpusa, end = "\n\n")


# 2)
matrice = [[4, 5, 2], [2, 0, 0], [8, 16, 2], [6, 3, 3]]
matrice.sort(key = lambda x: x[0])
for linie in matrice:
    for elem in linie:
        print(f"{elem : 5}", end = " ")
    print()
print()


# 3)
def factorial(n: int) -> int:
    if n == 0:
        return 1
    return n * factorial(n - 1)

t = []
n = 6
elem_max = 1
for i in range(n):
    aux = []
    for j in range(i + 1):
        elem = factorial(i) // (factorial(j) * factorial(i - j))
        if elem > elem_max:
            elem_max = elem
        aux.append(elem)
    t.append(aux)

lmax = len(str(elem_max))
for linie in t:
    for x in linie:
        print(f"{x :> {lmax + 1}}", end = " ")
    print()
print()


# 4)
def sieve(n: int) -> None:
    primes = [True for _ in range(n + 1)]
    x = 2
    while x * x <= n:
        if primes[x]:
            for i in range(x * x, n + 1, x):
                primes[i] = False
        x += 1

    for i in range(2, n + 1):
        if primes[i]:
            print(i, end = " ")
    print("\n")

sieve(100)


# 5)
A = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20}
B = {0, 4, 6, 10, 12, 13, 18, 21, 25, 40, 90}
A = list(A)
B = list(B)

union, intersection, i, j = [], [], 0, 0
length_A, length_B = len(A), len(B)
while i < length_A and j < length_B:
    if A[i] < B[j]:
        union.append(A[i])
        i += 1
    elif A[i] > B[j]:
        union.append(B[j])
        j += 1
    else:
        intersection.append(A[i])
        union.append(B[j])
        i += 1
        j += 1

while i < length_A:
    union.append(A[i])
    i += 1

while j < length_B:
    union.append(B[j])
    j += 1

print(f"UNION: {sorted(union)}")
print(f"INTERSECTION: {intersection}")