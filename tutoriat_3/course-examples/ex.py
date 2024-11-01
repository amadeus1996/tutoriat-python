def ex1():
    L = [1,2,3,4,2,2,1,6,7,1]
    a = set(L)
    print(len(a))

def ex2():
    prop = 'Ana se duce la piata dimineata. Ana are foarte multa energie dimineata. Piata se deschide abia la 8.'
    L = [x.strip('!.,?;').lower() for x in prop.split()]
    d = {x : L.count(x) for x in L}
    print(d)

def ex3():
    A = {1, 2, 3, 4, 5}
    B = {4, 5, 6, 7, 8}

    # Reuniune
    reuniune = A | B
    print("Reuniunea A ∪ B:", reuniune)  # Output: {1, 2, 3, 4, 5, 6, 7, 8}

    # Intersecție
    intersectie = A & B
    print("Intersecția A ∩ B:", intersectie)  # Output: {4, 5}

    # Diferență
    diferenta_A_B = A - B
    print("Diferența A - B:", diferenta_A_B)  # Output: {1, 2, 3}

    diferenta_B_A = B - A
    print("Diferența B - A:", diferenta_B_A)  # Output: {6, 7, 8}

    # Diferență simetrică
    diferenta_simetrică = A ^ B
    print("Diferența simetrică A △ B:", diferenta_simetrică)  # Output: {1, 2, 3, 6, 7, 8}

# 4. Stocare și căutare de produse

# Dicționarul de produse și prețuri
preturi_produse = {}

# Funcție pentru adăugarea unui produs nou
def adauga_produs(produs, pret):
    preturi_produse[produs] = pret
    print(f"Produsul '{produs}' a fost adăugat cu prețul {pret}.")

# Funcție pentru actualizarea prețului unui produs existent
def actualizeaza_pret(produs, pret):
    if produs in preturi_produse:
        preturi_produse[produs] = pret
        print(f"Prețul produsului '{produs}' a fost actualizat la {pret}.")
    else:
        print(f"Produsul '{produs}' nu există în dicționar.")

# Funcție pentru căutarea unui produs
def cauta_pret(produs):
    if produs in preturi_produse:
        return preturi_produse[produs]
    else:
        return f"Produsul '{produs}' nu există."

# Exemplu de utilizare
adauga_produs("mere", 2.5)
adauga_produs("banane", 3.0)
actualizeaza_pret("mere", 2.8)
print("Prețul pentru mere:", cauta_pret("mere"))  # Output: 2.8
print("Prețul pentru pere:", cauta_pret("pere"))  # Output: Produsul 'pere' nu există.

# 5. Dicționar de studenți

# Dicționar pentru a stoca notele studenților
note_studenti = {}

# Funcție pentru adăugarea unui nou student
def adauga_student(nume, nota):
    note_studenti[nume] = nota
    print(f"Studentul '{nume}' a fost adăugat cu nota {nota}.")

# Funcție pentru actualizarea notei unui student existent
def actualizeaza_nota(nume, nota):
    if nume in note_studenti:
        note_studenti[nume] = nota
        print(f"Nota studentului '{nume}' a fost actualizată la {nota}.")
    else:
        print(f"Studentul '{nume}' nu există în dicționar.")

# Funcție pentru calcularea mediei notelor
def calculeaza_media():
    if note_studenti:
        media = sum(note_studenti.values()) / len(note_studenti)
        return media
    else:
        return "Nu există studenți în dicționar."

# Exemplu de utilizare
adauga_student("Ana", 9.5)
adauga_student("Bogdan", 8.0)
actualizeaza_nota("Ana", 10)
print("Media notelor:", calculeaza_media())  # Output: 9.0
