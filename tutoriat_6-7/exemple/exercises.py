# EX 1
# citirea datelor
# o piesa va fi memorata intr-un tuplu de forma (nr_piesa, durata_secunde)
with open("piese.in") as f:
    T = int(f.readline()[:-2])
    t = []
    for linie in f:
        aux = linie.split()
        t.append((int(aux[1]), int(aux[2][:2]) * 60 + int(aux[2][3:5])))

sol = []
aux = T 
t.sort(key = lambda x: x[1]) # sortam ca sa avem piesele cu cea mai scurta durata

for piesa in t:
    # cat timp nu depasim durata T, adaugam cea mai scurta piesa
    if aux - piesa[1] < 0:
        break
    aux -= piesa[1]
    sol.append(piesa)

with open("piese.out", "w") as g:
    for piesa in sol:
        g.write(f"Piesa {piesa[0]}: {piesa[1]}s\n")
    g.write(f"Durata totala: {T - aux}/{T}\n")


# EX 2
# datele de intrare
t = [4, -5, 2, 7, -1, 5, 6, -3, 4]
k = 5

# sortam lista ca sa putem face transformarile optime de semn
t.sort()

suma = 0
# luam primele k numere si le schimbam semnul, le adunam
for i in range(k):
    suma += (~t[i] + 1) # stiti de la ASC ca asa se schimba semnul unui nr :)
    
print(suma + sum(t[k:])) # adunam numerele ramase si afisam rezultatul