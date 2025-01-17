with open("concurs.in", "r") as f:
    n = int(f.readline())
    valori = [int(x) for x in f.readline().split()]

suma = 0
for x in sorted(valori):
    suma += x / (n + 1)
    n -= 1

print(f"{suma:.3f}")