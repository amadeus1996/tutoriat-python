# Ex 1

d = {}

def adaugare_produs(nume_produs, pret_produs):
    d[nume_produs] = pret_produs

def actualizeaza_produs(nume_produs, pret_nou):
    if nume_produs in d:
        d[nume_produs] = pret_nou
    else:
        print("Produsul nu există în catalog.")

def cauta_pret(nume_produs):
    if nume_produs in d:
        return d[nume_produs]
    else:
        return "Produsul nu există în catalog."
    
# Exemplu de utilizare
# adaugare_produs("mere", 3)
# adaugare_produs("pere", 4)
# adaugare_produs("banane", 5)
# print(d)
# actualizeaza_produs("mere", 4)
# actualizeaza_produs("portocale", 6)
# print(d)
# print(cauta_pret("mere"))


# Ex 2

d = {}

def adauga_student(nume_student, nota):
    d[nume_student] = nota

def actualizeaza_nota(nume_student, nota_noua):
    if nume_student in d:
        d[nume_student] = nota_noua
    else:
        print("Studentul nu există în catalog.")

def calculeaza_media():
    return sum(d.values()) / len(d)

# Exemplu de utilizare
# adauga_student("Ion", 9)
# adauga_student("Maria", 8)
# adauga_student("Ana", 10)
# print(d)
# actualizeaza_nota("Ion", 10)
# print(d)
# print("Media notelor:", calculeaza_media())

# Ex 3

# Citirea fișierului și crearea dicționarului de autori
def citeste_carti(fisier):
    carti = {}
    with open(fisier, 'r') as f:
        for linie in f:
            titlu, autor, an = linie.strip().split(', ')
            if autor not in carti:
                carti[autor] = []
            carti[autor].append(titlu)
    return carti

# Afișarea autorilor unici
def autori_unici(carti):
    return list(carti.keys())

# Scrierea catalogului în fișier
def scrie_catalog(carti, fisier):
    with open(fisier, 'w') as f:
        for autor, titluri in carti.items():
            f.write(f"{autor}:\n")
            for titlu in titluri:
                f.write(f"  - {titlu}\n")

# Exemplu de utilizare
# carti = citeste_carti('carti.txt')
# print("Autorii unici:", autori_unici(carti))
# scrie_catalog(carti, 'catalog_autori.txt')

# Ex 4

def citeste_vanzari(fisier):
    vanzari = {}
    with open(fisier, 'r') as f:
        for linie in f:
            produs, cantitate = linie.strip().split(', ')
            cantitate = int(cantitate)
            if produs in vanzari:
                vanzari[produs] += cantitate
            else:
                vanzari[produs] = cantitate
    return vanzari

def top_vanzari(vanzari, n=3):
    return sorted(vanzari.items(), key=lambda x: x[1], reverse=True)[:n]

# vanzari = citeste_vanzari('vanzari.txt')
# top_3 = top_vanzari(vanzari)
# print("Top 3 produse vândute:", top_3)

# Ex 5

def citeste_stoc(fisier):
    stoc = {}
    with open(fisier, 'r') as f:
        for linie in f:
            produs, cantitate = linie.strip().split(', ')
            stoc[produs] = int(cantitate)
    return stoc

def actualizeaza_stoc(stoc, fisier_vanzari):
    with open(fisier_vanzari, 'r') as f:
        for linie in f:
            produs, cantitate = linie.strip().split(', ')
            cantitate = int(cantitate)
            if produs in stoc:
                stoc[produs] -= cantitate

def scrie_stoc(stoc, fisier):
    with open(fisier, 'w') as f:
        for produs, cantitate in stoc.items():
            f.write(f"{produs}, {cantitate}\n")

# stoc = citeste_stoc('stoc_initial.txt')
# actualizeaza_stoc(stoc, 'vanzari.txt')
# scrie_stoc(stoc, 'stoc_actualizat.txt')

# Ex 6

def citeste_temperaturi(fisier):
    temperaturi = []
    with open(fisier, 'r') as f:
        for linie in f:
            temperaturi.append(int(linie.strip()))
    return temperaturi

def calculeaza_raport(temperaturi):
    return {
        "maxima": max(temperaturi),
        "minima": min(temperaturi),
        "media": sum(temperaturi) / len(temperaturi)
    }

def scrie_raport(raport, fisier):
    with open(fisier, 'w') as f:
        for key, value in raport.items():
            f.write(f"{key}: {value}\n")

# temperaturi = citeste_temperaturi('temperaturi.txt')
# raport = calculeaza_raport(temperaturi)
# scrie_raport(raport, 'raport_temperaturi.txt')


# Ex 7

def citeste_likeuri(fisier):
    likeuri = {}
    with open(fisier, 'r') as f:
        for linie in f:
            persoana, nr_likeuri = linie.strip().split(', ')
            nr_likeuri = int(nr_likeuri)
            if persoana in likeuri:
                likeuri[persoana] += nr_likeuri
            else:
                likeuri[persoana] = nr_likeuri
    return likeuri

def top_likeuri(likeuri, n=3):
    return sorted(likeuri.items(), key=lambda x: x[1], reverse=True)[:n]

# likeuri = citeste_likeuri('likeuri.txt')
# top_3 = top_likeuri(likeuri)
# print("Top 3 persoane cu cele mai multe like-uri:", top_3)

# Ex 8

def citeste_tranzactii(fisier):
    conturi = {}
    with open(fisier, 'r') as f:
        for linie in f:
            cont, tip, suma = linie.strip().split(', ')
            suma = int(suma)
            if cont not in conturi:
                conturi[cont] = 0
            if tip == 'depunere':
                conturi[cont] += suma
            elif tip == 'retragere':
                conturi[cont] -= suma
    return conturi

# conturi = citeste_tranzactii('tranzactii.txt')
# print("Soldurile finale ale conturilor:", conturi)

