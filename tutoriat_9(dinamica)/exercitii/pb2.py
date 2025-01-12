# Problema Rucsacului 0/1

greutati = [1, 3, 4, 5]
valori = [1, 4, 5, 7]
capacitate_rucsac = 7

# Varianta ineficientă (recursive brute force)
def varianta_ineficienta(L=[]):
    if len(L) == len(valori):
        suma_curenta = 0
        greutate_curenta = 0
        for i, val in enumerate(L):
            if val == 1:
                suma_curenta += valori[i]
                greutate_curenta += greutati[i]
        if greutate_curenta <= capacitate_rucsac:
            return suma_curenta
        return 0

    # Generăm toate combinațiile posibile (0/1 pentru fiecare element)
    return max(varianta_ineficienta(L + [0]), varianta_ineficienta(L + [1]))

# Varianta eficientă (Dynamic Programming)
def varianta_eficienta():
    # Inițializăm lista cu valori maxime pentru fiecare greutate
    dp = [0] * (capacitate_rucsac + 1)

    for greutate, valoare in zip(greutati, valori):
        for i in range(capacitate_rucsac, greutate - 1, -1):
            dp[i] = max(dp[i], dp[i - greutate] + valoare)

    # Valoarea maximă pentru întreaga capacitate
    return dp[capacitate_rucsac]

# Testăm ambele variante
valoare_max_ineficienta = varianta_ineficienta()
print(f"Valoarea maximă (ineficient): {valoare_max_ineficienta}")

valoare_max_eficienta = varianta_eficienta()
print(f"Valoarea maximă (eficient): {valoare_max_eficienta}")