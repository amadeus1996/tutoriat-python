# Tutoriat 5 - Complexități

## Table of contents
- [Introducere în Complexități](#1---introducere-în-complexități)
- [Complexitatea de Timp și de Memorie](#2---complexitatea-de-timp-și-de-memorie)
- [Complexitățile Funcțiilor Implicite în Python](#3---complexitățile-funcțiilor-implicite-în-python)
- [Functii Recursive](#4---functii-recursive)
- [Exerciții Practice](#5---exerciții-practice)
- [Exercitii Extra](#6---exercitii-extra)

---

## 1 - Introducere în Complexități
# Tutoriat 5 - Complexități

## Table of contents
- [Introducere în Complexități](#1---introducere-în-complexități)
- [Complexitatea de Timp și de Memorie](#2---complexitatea-de-timp-și-de-memorie)
- [Complexitățile Funcțiilor Implicite în Python](#3---complexitățile-funcțiilor-# Tutoriat 5 - Complexități

## Table of contents
- [Introducere în Complexități](#1---introducere-în-complexități)
- [Complexitatea de Timp și de Memorie](#2---complexitatea-de-timp-și-de-memorie)
- [Complexitățile Funcțiilor Implicite în Python](#3---complexitățile-funcțiilor-implicite-în-python)
- [Functii Recursive](#4---functii-recursive)
- [Exerciții Practice](#5---exerciții-practice)
- [Exercitii Extra](#6---exercitii-extra)

---

## 1 - Introducere în Complexități

### 1.1 - Ce sunt complexitățile?
Complexitățile sunt o metodă de a analiza și evalua **eficiența algoritmilor**. Aceasta implică determinarea resurselor necesare pentru a executa un algoritm, cum ar fi timpul de rulare și memoria utilizată, în funcție de dimensiunea intrării.

De ce este importantă analiza complexităților?
- **Optimizare**: Alegerea celui mai eficient algoritm poate reduce timpul de execuție și consumul de memorie.
- **Scalabilitate**: Înțelegerea comportamentului unui algoritm pe seturi mari de date.
- **Comparabilitate**: Ne permite să comparăm diferite soluții pentru aceeași problemă.

### 1.2 - Notarea Big-O
Pentru a exprima complexitatea unui algoritm, folosim notația **Big-O**, care descrie cea mai rea situație posibilă (worst-case). Aceasta ne spune cum crește timpul/memoria în raport cu dimensiunea datelor de intrare.

Exemple frecvente:
- **O(1)**: Constantă - timpul/memoria nu depind de dimensiunea datelor.
- **O(log n)**: Logaritmică - creștere lentă (ex: căutare binară).
- **O(n)**: Liniară - timpul crește proporțional cu dimensiunea datelor.
- **O(n²)**: Pătratică - folosită frecvent în algoritmi simpli de sortare (ex: Bubble Sort).
- **O(2ⁿ)**: Exponențială - extrem de ineficientă pentru intrări mari.

---

## 2 - Complexitatea de Timp și de Memorie

### 2.1 - Complexitatea de timp
Reprezintă timpul necesar pentru a executa un algoritm, în funcție de dimensiunea intrării.

#### Exemple practice:
1. **Parcurgerea unei liste**:
    ```python
    def print_elements(lst):
        for element in lst:
            print(element)
    ```
    Complexitatea: **O(n)**, deoarece iterăm prin fiecare element o dată.

2. **Căutare într-o listă sortată**:
    ```python
    def binary_search(lst, target):
        low, high = 0, len(lst) - 1
        while low <= high:
            mid = (low + high) // 2
            if lst[mid] == target:
                return mid
            elif lst[mid] < target:
                low = mid + 1
            else:
                high = mid - 1
        return -1
    ```
    Complexitatea: **O(log n)**, datorită reducerii intervalului la jumătate la fiecare pas.

### 2.2 - Complexitatea de memorie
Reprezintă cantitatea de memorie suplimentară utilizată de un algoritm în funcție de dimensiunea intrării.

#### Exemple practice:
1. **Stocarea unei liste în memorie**:
    ```python
    lst = [i for i in range(10)]
    ```
    Complexitatea: **O(n)**, unde `n` este numărul de elemente.

2. **Folosirea unui generator**:
    ```python
    def generate_numbers(n):
        for i in range(n):
            yield i
    ```
    Complexitatea: **O(1)**, deoarece generatorii utilizează memoria doar pentru elementul curent.

---

## 3 - Complexitățile Funcțiilor Implicite în Python

### Liste
1. **Accesare elemente**:
    ```python
    lst = [1, 2, 3, 4]
    print(lst[2])  # O(1)
    ```
2. **Adăugare la final**:
    ```python
    lst.append(5)  # O(1)
    ```
3. **Inserare în listă**:
    ```python
    lst.insert(0, 10)  # O(n)
    ```

### Seturi
1. **Adăugare element**:
    ```python
    s = set()
    s.add(1)  # O(1)
    ```
2. **Verificare apartenență**:
    ```python
    print(1 in s)  # O(1)
    ```

### Dictionare
1. **Accesare valoare**:
    ```python
    d = {'a': 1, 'b': 2}
    print(d['a'])  # O(1)
    ```
2. **Adăugare pereche cheie-valoare**:
    ```python
    d['c'] = 3  # O(1)
    ```

---

## 4 - Functii recursive
O functie recursiva, in general, este o functie care se autoapeleaza.

Un exemplu fundamental: factorialul unui numar. Sa presupunem ca vrem sa definim o functie recursiva <b>def factorial(n)</b>, care sa returneze factorialul unui numar natural <b>n</b>. Se stie ca <b>n! = 1 * 2 * ... * n</b>, deci <b>n! = n * (n - 1)!</b>, adica am putea gandi functia noastra asa: <b>factorial(n) = n * factorial(n - 1)</b> (aici intervine autoapelul).

Unde se termina autoapelurile? De exemplu, <b>factorial(15) = 15 * factorial(14)</b>, apoi <b>factorial(14) = 14 * factorial(13)</b>, etc. Urmarind aceasta logica, functia ar trebui sa se autoapeleze la infinit; din acest motiv, orice functie recursiva trebuie sa contina un caz de baza (o conditie de stop). In cazul functiei <b>factorial</b>, am putea considera cazul de baza ca fiind <b>n == 1</b>:

    def factorial(n):
        if n <= 1: # daca ajungem la n = 1 SAU input-ul e un numar negativ, functia returneaza 1
            return 1 
        return n * factorial(n - 1) # altfel, apelul curent returneaza n * factorial(n - 1)
    
    # exemplu:
    # factorial(3) = 3 * factorial(2)
    # factorial(2) = 2 * factorial(1)
    # factorial(1) = 1
    
    # factorial(2) = 2 * 1 = 2
    # factorial(3) = 3 * 2 = 6
    
Calculul din exemplul de mai sus ilustreaza comportamentul functiilor recursive; se foloseste o stiva (principiul <b>LIFO</b> - last in, first out). De fiecare data cand se apeleaza functia, se salveaza pe stiva un return address (o adresa care retine linia unde ar trebui sa se intoarca functia dupa ce a terminat apelurile recursive), argumente, variabile locale, etc. Odata ce s-a ajuns la cazul de baza (acesta fiind ultimul element adaugat pe stiva/stack), atunci vor incepe pop-urile.

    def f(n):
        ... instructiuni
        f(n - 1):         stack-ul va retine un return address pentru cand iese din apel
        ... instructiuni: aici va fi return address-ul

---

## 5 - Exerciții Practice

1. **Determină complexitatea** pentru următoarele funcții:
    ```python
    def f1(n):
        for i in range(n):
            for j in range(n):
                print(i, j)
    ```

    ```python
    def f2(lst):
        for i in lst:
            if i % 2 == 0:
                print(i)
    ```

    ```python
    def f3(d):
        for key in d:
            print(key, d[key])
    ```

2. **Analizează eficiența unei funcții recurente**:
    ```python
    def fibonacci(n):
        if n <= 1:
            return n
        return fibonacci(n - 1) + fibonacci(n - 2)
    ```

3. **Compară două metode de generare a pătratelor numerelor**:
    ```python
    # Metoda 1
    squares = [x**2 for x in range(10)]
    
    # Metoda 2
    squares = []
    for x in range(10):
        squares.append(x**2)
    ```

4. **Folosind `time`**, măsoară eficiența pentru următorul cod:
    ```python
    import time

    lst = [i for i in range(1000000)]
    
    start = time.time()
    print(999999 in lst)
    print("Execution time:", time.time() - start)
    ```

---

## 6 - Exercitii Extra
Determinati complexitatile de timp pentru urmatoarele secvente de cod:

    # EX 1
    a = 0
    b = 0
    for i in range(N):
        a += 1
    for i in range(M):
        b += 1

    # ----------------------------

    # EX 2
    k = 0
    i, j = n // 2, 2
    while i <= n:
        while j <= n:
            k += n / 2
            j *= 2
        i += 1
        
    # ----------------------------
    
    # EX 3
    a = 0
    i = n
    while i > 0:
        a += i
        i //= 2
        
    # ----------------------------    
        
    # EX 4
    k = 0
    for i in range(n):
        for j in range(i):
            k += 1