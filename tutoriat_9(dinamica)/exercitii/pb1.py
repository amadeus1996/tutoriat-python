# Problema drumului maxim

import time

def este_drum_valid(matrice, x, y):
    return x >= 0 and x < len(matrice) and y >= 0 and y < len(matrice[0])

# Ineficient
def gaseste_drumul_maxim(matrice, x, y):
    if not este_drum_valid(matrice, x, y):
        return 0
    dreapta = gaseste_drumul_maxim(matrice, x, y+1)
    jos = gaseste_drumul_maxim(matrice, x+1, y)
    return matrice[x][y] + max(dreapta, jos)

def gaseste_drumul_maxim_eficient(matrice, memo, x, y):
    if not este_drum_valid(matrice, x, y):
        return 0
    if memo[x][y] != -1:
        return memo[x][y]
    dreapta = gaseste_drumul_maxim_eficient(matrice, memo, x, y+1)
    jos = gaseste_drumul_maxim_eficient(matrice, memo, x+1, y)
    memo[x][y] = matrice[x][y] + max(dreapta, jos)
    return memo[x][y]

def gaseste_drumul_maxim_eficient_iterativ(matrice):
    n = len(matrice)
    m = len(matrice[0])
    memo = [[-1 for i in range(m)] for j in range(n)]
    for i in range(n-1, -1, -1):
        for j in range(m-1, -1, -1):
            if i == n-1 and j == m-1:
                memo[i][j] = matrice[i][j]
            elif i == n-1:
                memo[i][j] = matrice[i][j] + memo[i][j+1]
            elif j == m-1:
                memo[i][j] = matrice[i][j] + memo[i+1][j]
            else:
                memo[i][j] = matrice[i][j] + max(memo[i][j+1], memo[i+1][j])
    return memo[0][0]

m = [[i for i in range(100)] for j in range(100)]
memo = [[-1 for i in range(100)] for j in range(100)]
start = time.time()
print(gaseste_drumul_maxim(m, 0, 0))
# print(gaseste_drumul_maxim_eficient(m, memo, 0, 0))
# print(gaseste_drumul_maxim_eficient_iterativ(m))
end = time.time()
print("--- %s seconds ---" % (end - start))