# Tutoriat 3

## Table of contents
- [Introducere](#introducere)
- [Hash Tables](#hash-tables)
- [Seturi](#seturi)
- [Dicționare](#dictionare)
- [Exerciții (part 1)](#exercitii-introductive)
- [Exerciții (part 2)](#exercitii-din-examene-si-colocvii)

## Introducere
În acest tutoriat, vom explora trei structuri de date esențiale în Python: **hash tables**, **seturi** și **dicționare**. Aceste structuri sunt similare cu cele din C++ (precum `unordered_map` și `set`), dar sunt mult mai ușor de utilizat în Python, datorită sintaxei simplificate și funcțiilor integrate.

## Hash tables
**Hash table** este o structură de date ce mapează o cheie la o valoare. Intr-un hash table, datele sunt stocate intr-un format de liste, dar fiecare valoare are cheia sa proprie, folosita la a identifica valoarea. Din asta rezulta performanta buna in a lua valori din hash tables.
În Python, acestea sunt implementate prin dicționare (`dict`).

De exemplu, avem urmatorul hash table care retine pentru mai multi oameni, luna in care s-au nascut. Cheile sunt numele oamenilor, iar valorile sunt lunile.
```
+-----------------------+
|   Key   |   Value     |
+-----------------------+
| Alice   | January     |
| Bob     | May         |
| Charlie | January     |
| David   | August      |
| Eve     | December    |
| Brain   | May         |
+-----------------------+
```

Pentru a gasi in ce luna este Alice nascuta (odata ce am stocat intr-un hash table valorile), trebuie sa gasim o cale de a afla index-ul din lista la care se afla Alice (pentru ca am zis ca in spate, hash tables sunt reprezentate ca liste). Aici intervine **hash function**. Un hash function primeste o valoare de tip cheie (in cazul nostru, va primi un nume: "Alice") si returneaza index-ul la care se afla valoarea sa.

Ce face o **functie hash** sa fie buna?
R: Sa distribuie cheile cat mai balansate in toata lista (un exemplu de asa nu: Nu vrem ca functia noastra sa returneze mereu 0, pentru ca in acest caz toate valorile ar fi una peste alta), astfel incat minimizam sansa de coliziune (cand 2 chei returneaza acelasi index)

Un exemplu de o functie hash (una foarte simpla), ar fi sa luam numele (adica cheia) si sa returnam valoarea ASCII a primei litere MODULO marimea listei

```python
def simple_hash(key, array_size):
    return ord(key[0]) % array_size
```

Functia este simpla, dar s-ar putea sa existe coliziuni, deoarece chei diferite pot incepe cu aceeasi litera (astfel indexii returnati vor fi la fel). Sa luam ca exemplu marimea listei = 10. Daca am rula functia pentru toate numele de mai sus am ajunge la:

![Cheie-valoare](assets/hash-tables-in-python-2.png)

Dupa cum puteti observa, `Bob` si `Brian` au acelasi index => coliziune.

##### De retinut: 
Functiile Hash sunt un aspect esential al eficientei tabelelor hash.

![Inserare in hash table](assets/hash-tables-in-python-3.png)

#### Cum rezolvam o coliziune?

##### Separate Chaining
![](assets/hash-tables-in-python-4.png)

##### Open Addressing
Metoda folosită de dicționarele Python pentru a gestiona coliziunile este mai sofisticată decât separate chaining. Python folosește o formă de open addressing numită „probing”.

În probing, când apare o coliziune, tabela hash verifică următorul slot disponibil și plasează acolo perechea cheie-valoare. Procesul de găsire a următorului slot disponibil se numește „probing”, iar pentru acesta se pot folosi mai multe strategii, cum ar fi:

    Probing liniar – verificarea sloturilor unul câte unul, în ordine
    Probing pătratic – verificarea sloturilor în puteri crescătoare ale lui doi

## Seturi
Un set este o colecție neordonată de elemente unice. În Python, putem folosi set() pentru a crea astfel de colecții. Seturile sunt utile pentru a elimina duplicatele și a verifica existența unor elemente într-o colecție.

### Exemple

1. Cream un set si adaugam elemente:
```python
# Set cu elemente unice
numere = {1, 2, 3, 4}
numere.add(5)
print(numere) # Output: {1, 2, 3, 4, 5}

```

2. Verificam daca un element exista in set:
```python
if 3 in numere:
    print("3 este în set")
```

3. Seturile suporta operatii de reuniune si intersectie:
```python
A = {1, 2, 3}
B = {3, 4, 5}
print(A | B)  # Reuniune: {1, 2, 3, 4, 5}
print(A & B)  # Intersecție: {3}
```

## Dictionare
Dicționarele (dict) sunt structuri de date de tip cheie-valoare, similare cu unordered_map din C++. Ele sunt implementate in spate folosind **hash tables**. Cheile pot fi de orice tip imutabil (e.g., string, int). 

### Exemple
1. Cum am tine datele in memorie daca avem nevoie sa retinem numele unor persoane si varstele? (Datele sunt citite din fisier)
Ex: 
```
Ana,20
Bogdan,30
Carmen,28
``` 
R: Creăm un dicționar pentru a asocia numele unor persoane cu vârstele lor:
   ```python
   # Hash Table folosind dicționare
   varste = {"Ana": 25, "Bogdan": 30, "Carmen": 28}
   print(varste["Ana"])  # Output: 25

   # afisare valori dictionar:
    #Metoda 1
    print(varste)

    #Metoda 2
   for (k, v) in varste.items():
    print(k, v)
   ```

2. Cum modificam numele unei persoane, deja existente in dictionar?
R:
```python
# schimbam varsta Anei
print(f'Ana are {varste["Ana"]} de ani, inainte de schimbare')

varste["Ana"] = 42

print(f'Ana are {varste["Ana"]} de ani, dupa schimbare')
```

3. Verificarea daca un nume exista deja in dictionar (cheie exista deja in dictionar)
```python
# verificam daca un nume dat exista in dictionar
nume_de_verificat = "Petre"

if nume_de_verificat in varste:
    print("Exista numele")
else:
    print("Nu exista numele")
```

4. Eliminarea unei chei din dictionar
```python
del varste["Ana"]

print(varste) # {'Bogdan': '30', 'Carmen': '28'}

del varste["Ana"] # Raises KeyError: "Ana"

print(varste.pop("Ana", "Necunoscut")) # Necunoscut
```

**Grija la accesare**:
```python
print(varste["Ana"]) # 42
print(varste["Popa"]) # Raises KeyError: 'Popa'

print(varste.get("Popa", "Necunsocut")) # Necunoscut
```


## Exercitii introductive

1. Numără elementele unice: Creează un program care citește o listă de numere și folosește un set pentru a elimina duplicatele. Afișează setul și numărul elementelor unice.
Ex: `1, 2, 3, 4, 2, 2, 4, 6, 7, 1`
R: `6`

2. Contor de cuvinte: Scrie un program care numără de câte ori apare fiecare cuvânt într-o listă de cuvinte folosind un dicționar.
Ex: `Ana se duce la piata dimineata. Ana are foarte multa energie dimineata. Piata se deschide abia la 8.`
R: 
```
'ana': 2
'se': 2
'duce': 1
'la': 2
'piata': 2
'dimineata': 2
...
```

3. Creează două seturi de numere întregi și realizeaza toate operatiile pe multimi (reuniune, intersectie, diferenta, diferenta simetrica).

4. Stocare și căutare de produse: Creează un dicționar care mapează produse la prețuri. Oferă utilizatorului opțiunea de a adăuga un produs nou, de a actualiza prețul unui produs existent și de a căuta prețul unui produs.

5. Dicționar de studenți: Creează un dicționar care stochează numele studenților și nota lor la un examen. Scrie funcții care adaugă un nou student, actualizează nota unui student existent și calculează media notelor.

## Exercitii din examene si colocvii

> **Disclaimer**: Aceste cerinte au fost preluate din modele de examene si colocvii, dar sunt usor modificate astfel incat sa includa doar materia studiata pana acum.

___

1. Descompuneti un numar natural <b>(n>=2)</b> in factori primi si stocati rezultatul intr-un dictionar de forma <b>{divizor_prim:exponent}</b>.

        n = 1932

        {2: 2, 3: 1, 7: 1, 23: 1}
        
___

2. Fiind dat un sir de cuvinte separate prin spatii, sa se creeze un dictionar de dictionare de forma <b>{cuvant: {litera: frecventa}}</b>. Cuvintele din sir se pot repeta.

        sir = "teste programare teste"

        {'teste': {'t': 4, 'e': 4, 's': 2}, 'programare': {'p': 1, 'r': 3, 'o': 1, 'g': 1, 'a': 2, 'm': 1, 'e': 1}}
        
___

3. Se da o lista de numere naturale. Sa se creeze un dictionar de forma <b>{numar: (divizori)}</b>, care stocheaza pentru fiecare numar divizorii sai proprii intr-un tuplu.

        nums = [50, 21, 13, 84, 50, 60]

        {50: (2, 5, 10, 25), 21: (3, 7), 13: (), 84: (2, 3, 4, 6, 7, 12, 14, 21, 28, 42), 60: (2, 3, 4, 5, 6, 10, 12, 15, 20, 30)}
        
___

4. Se da un set de numere intregi si un tuplu de liste formate din numere intregi. Sa se stocheze intr-un dictionar perechi de forma <b>{numar: [(indice, frecventa)]}</b>, unde <b>numar</b> e un numar din set, iar lista contine tupluri cu indicii listelor (incepand de la 0) care contin numarul (si frecventa lui).

        nums1 = {10, 20, 14}, nums2 = ([10, 11, 10], [20, 20, 40], [5], [10, 11])

        {10: [(0, 2), (3, 1)], 20: [(1, 2)], 14: []}

___

5. Se da o lista de numere naturale. Sa se stocheze informatii intr-un dictionar cu structura <b>{medie: [numere]}</b>, unde <b>[numere]</b> este o lista formata din numerele care au media aritmetica a cifrelor egala cu <b>medie</b>. Listele de numere trebuie sa fie sortate in ordine descrescatoare.

        nums = [82375, 201, 51, 73, 3456, 2855, 1021, 90, 153]

        {5.0: [82375, 2855, 73], 1.0: [1021, 201], 3.0: [153, 51], 4.5: [3456, 90]}
        
___

6. Se da o lista de numere naturale. Sa se stocheze intr-un dictionar perechi de forma <b>{numar: [(cifra, frecventa)]}</b>.

        nums = [1011, 234, 8158558, 234]

        {1011: [(1, 3), (0, 1)], 234: [(3, 1), (4, 1), (2, 1)], 8158558: [(1, 1), (8, 3), (5, 3)]}
        
___

7. Se da un sir de cuvinte separate prin spatii. Sa se stocheze intr-un dictionar perechi de forma <b>{palindrom: [vocale SAU consoane]}</b>. Se vor selecta doar palindromurile din sir, iar lista va fi formata din vocalele din cuvant (fara duplicate) daca numarul de vocale e mai mare decat numarul de consoane (sau egal); altfel, lista va fi formata din consoane.

        sir = "asa merem palindrom "

        {'asa': ['a'], 'merem': ['m', 'r']}
        
___

8. Fisierul <b>"text.in"</b> contine, pe mai multe linii, propozitii in care cuvintele sunt despartite prin spatii si semnele de punctuatie uzuale. Sa se scrie in fisierul <b>"text.out"</b> literele din textul dat si frecventele lor relative. Frecventa relativa a unei litere intr-un text este egala cu raportul dintre frecventa sa in textul respectiv si numarul total de litere din acel text. Literele si frecventele vor fi scrise in fisierul <b>"text.out"</b>. Nu se va face distinctie intre litere mici si litere mari.

        text.in
        Ana are multe pere si mere,
        dar are mai multe mere
        decat pere si prune
        mai multe decat pere.

        text.out
        a: 0.125
        n: 0.028
        r: 0.125
        e: 0.250
        m: 0.097
        u: 0.056
        l: 0.042
        t: 0.069
        p: 0.056
        s: 0.028
        i: 0.056
        d: 0.042
        c: 0.028

___

9. Fisierul <b>"numere.in"</b> contine, pe mai multe linii, numere naturale despartite intre ele prin spatii. Sa se creeze o lista de subliste, unde o sublista contine numerele de pe un rand. Apoi, sa se elimine din fiecare sublista fiecare aparitie a valorii minime (valoarea minima specifica acelei subliste), iar in final sa se pastreze doar primele N elemente (unde N e lungimea minima a unei subliste, odata ce s-au eliminat valorile minime din toate sublistele). Sublistele rezultante vor fi scrise pe randuri diferite in fisierul <b>"numere.out"</b>.

        numere.in
        100 54 101 54 2 81 92
        10 1 1 2 2 1 70
        12 81 10 8 9 8 10
        
        numere.out
        100 54 101 54 
        10 2 2 70 
        12 81 10 9 
