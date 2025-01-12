# EX1
# nrf, nrb, s = 4, 3, 4
# sol = [0] * (s + 1)
# fete = baieti = count = 0

# def bkt(k):
#     global fete, baieti, count
#     for i in range(sol[k - 1] + 1, nrf + nrb + 1):
#         sol[k] = i
#         if baieti <= s//2 and fete <= s//2 and sol[k] not in sol[1:k]:
#             if i <= nrf:
#                 fete += 1
#             else:
#                 baieti += 1
#             if k == s:
#                 # conditie pt. punctul b):
#                 # and sol[1] == 1 and sol[s//2 + 1] == nrf + 1
#                 if baieti == s/2 and sol[1] == 1 and sol[s//2 + 1] == nrf + 1:
#                     print(*sol[1:])
#                     count += 1
#             else:
#                 bkt(k + 1)
#             if i <= nrf:
#                 fete -= 1
#             else:
#                 baieti -= 1

# bkt(1)
# print(count)

# -------------------------------------------------------------------------

# EX2
# def bkt(k):
#     global count 
#     for i in range(1, n + 1):
#         s[k] = i
#         if s[k] not in s[1:k] and ((s[k] > d and s[k - 1] <= d) or (s[k] <= d)):
#             if k == n:
#                 # if s[1] <= d and s[k] <= d:
#                     print(*s[1:])
#                     count += 1
#             else:
#                 bkt(k + 1)

# d, m = 3, 2
# n = d + m
# s = [0] * (n + 1)
# count = 0

# bkt(1)
# print(count)

# -------------------------------------------------------------------------

# EX3
# count = suma = 0
# def bkt(j):
#     global count, suma
#     for i in range(1, G + 1):
#         s[j] = i
#         if True not in [abs(s[j] - s[u]) > k for u in range(1, j)]:
#             suma += s[j]
#             if j == n:
#                 # and 1 in s[1:]
#                 if suma == G:
#                     print(*s[1:])
#                     count += 1
#             else:
#                 bkt(j + 1)
#             suma -= s[j]

# G, n, k = 10, 3, 4
# s = [0] * (n + 1)
# bkt(1)
# print(count)

# -------------------------------------------------------------------------

# EX4
# def bkt(k):
#     global count, suma
#     for i in range(s[k - 1], p // 2 + 1):
#         s[k] = i
#         suma += s[k]

#         if p % i == 0 and suma <= p:
#             if suma == p:
#                 # if len(set(s[1:k+1])) == 2:
#                     print(*s[1:k+1])
#                     count += 1
#             else:
#                 bkt(k + 1)
            
#         suma -= s[k]


# p = 6
# count = suma = 0
# s = [1] * (p + 1)

# bkt(1)
# print(count)

# -------------------------------------------------------------------------

# EX5
# def bkt(k):
#     global count, suma 
#     for i in range(1, c + 1):
#         s[k] = i
#         suma += i
#         if True not in [abs(s[k] - s[j]) > p for j in range(1, k)] and suma <= c:
#             if suma == c:
#                 # if s[1] == s[k]:
#                     print(*s[1:k+1])
#                     count += 1
#             else:
#                 bkt(k + 1)
#         suma -= i 

# p, c = 3, 6
# count = suma = 0
# s = [0] * (c + 1)

# bkt(1)
# print(count)

# -------------------------------------------------------------------------

# EX6
def bkt(k):
    global count 
    for i in t:
        s[k] = i
        if s[k] not in s[1:k] and ((tipar[k - 1] == 'l' and s[k] in L) or (tipar[k - 1] == 's' and s[k] in S)):
            if k == n:
                # if s[1] in "aeiouAEIOU":
                    print("".join(s[1:]))
                    count += 1
            else:
                bkt(k + 1)

count = 0
n = 6
tipar = "lslsll"
L = set(('a', 'b', 'c', 'D'))
S = set(('@', '.'))
t = L.union(S)
s = [0] * (n + 1)

bkt(1)
print(count)