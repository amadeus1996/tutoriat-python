# Tutoriat 2

## Table of contents

- [Scopul tutoriatului](#scopul-tutoriatului)
- [Fisiere](#fisiere)
- [Liste](#liste)
- [Exercitii](#exercitii)

## Scopul tutoriatului
Acest fisier este o tratare sumara a conceptelor care vor fi discutate si implementate la tutoriat, unde vom avea in vedere urmatoarele lucruri:

1. Prezentarea modalitatilor de a citi/scrie date folosind <b>fisiere</b>.
2. Intelegerea notiunilor de baza pentru <b>liste</b>.
3. Consolidarea gandirii algoritmice, rezolvarea unor probleme utilizand concepte studiate la curs/laborator despre <b>liste</b>.

## Fisiere

#### Introducere in fisiere

Pentru citirea datelor dintr-un fisier (si scrierea), exista 2 parametri (dintre care doar unul este necesar): drumul catre fisier si modul de deschidere. Al doilea parametru este optional, implicit find <b>"r"</b> (va fi explicat mai jos). De asemenea, in functie de modul de deschidere pot aparea diverse erori. Pentru exercitiile de la aceasta materie, se vor folosi in principal cele doua moduri <b>"r"</b> si <b>"w"</b>.

Datele citite din fisier sunt stocate sub forma de stringuri; in cazul in care se doreste, de exemplu, citirea si stocarea unor numere, se vor folosi conversiile necesare.

Odata ce nu mai este nevoie de fisier, acesta va trebui inchis separat. Totusi, mai exista o sintaxa ce poate fi utilizata pentru a asigura inchiderea automata a acestuia (sintaxa cu <b>"with"</b>, specificata mai jos).

#### Sintaxa

<b>f = open("path", ["open mode"])</b> urmat de  <b>f.close()</b>

<b> with open("path", ["open mode"]) as f</b>: 

#### Moduri de deschidere
- <b>"r" (read)</b>: fisierul poate fi utilizat doar pentru a citi date din el. Este modul implicit de deschidere (se va folosi automat daca se omite parametrul "open mode" in apelul functiei "open"). Daca fisierul indicat prin calea respectiva nu exista, se va genera o eroare (<b>FileNotFoundError</b>).
- <b>"w" (write)</b>: fisierul poate fi utilizat doar pentru a scrie date in el. Daca fisierul nu exista, se va crea unul nou; altfel, fisierul existent va fi sters automat si va fi inlocuit cu unul nou.
- <b>"x" (exclusive write)</b>: fisierul poate fi utilizat doar pentru a scrie date in el. Daca fisierul nu exista, se va crea unul nou; altfel, se va genera eroarea <b>FileExistsError</b>.
- <b>"a" (append)</b>: fisierul poate fi utilizat doar pentru a scrie date in el. Daca fisierul exista, atunci datele se vor scrie imediat dupa ultimul sau caracter; altfel, se va crea un fisier nou unde se vor scrie datele de la inceput.

## Liste
Listele sunt colectii de date <b>ordonate</b> (se pastreaza ordinea in care au fost inserate elementele). Acestea sunt <b>mutabile</b> (se pot insera si sterge elemente, se pot modifica elemente). Listele pot stoca mai multe tipuri de date - de exemplu <b>"t = [0, "sir", True, [1, 2, 3], (5, 6)]"</b> ar fi o lista valida.

Accesarea elementelor se realizeaza prin <b>indecsi</b>, care pot fi negativi sau pozitivi. Cu indecsii pozitivi ar trebui sa fiti familiari - indexarea incepe de la 0; cei negativi incep de la -1 si acceseaza elementele in ordine inversa, deci indexul -1 o sa acceseze ultimul element, -2 o sa acceseze penultimul element s.a.m.d. De asemenea, se pot aplica <b>sliceuri</b> (la fel ca la siruri de caractere): presupunand ca am avea lista <b>t = [1, 2, 3, 4, 5, 6, 7, 8]</b>, <b>t[2:6]</b> ar accesa elementele incepand de la indexul 2 pana la indexul 5 (range-ul nu il include pe 6), returnand [3, 4, 5, 6], iar <b>t[-8:-3:2]</b> ar returna elementele de la indexul -8 pana la -4 (cu pasul 2) => [1, 3, 5].

In principal, se va pune accentul in special pe <b>list comprehension</b>, o unealta foarte utila pentru crearea listelor. De exemplu, pentru generarea numerelor pare de la 1 la 15 s-ar putea folosi o secventa de initializare precum <b>t = [x for x in range(2, 15, 2)]</b>; selectarea patratelor perfecte din lista de numere <b>nums = [1, 3, 4, 16, 20, 25, 39, 49, 58]</b> s-ar putea scrie ca <b>t = [x for x in nums if x ** (1/2) == int(x ** (1/2))]</b>. Exista diverse moduri de scriere si detalii, dar s-au implementat multe exemple la tutoriat (exercitiile rezolvate le gasiti si aici, pe GitHub).

Reamintim ca unele din principalele metode pentru liste sunt <b>append</b> (adaugarea unui element), <b>remove</b> (stergerea unui element dupa valoare), <b>index</b> (prima pozitie gasita pentru un element de la stanga la dreapta), <b>pop</b> (stergea unui element dupa index, implicit sterge ultimul element), <b>insert</b> (inserarea unui element la un anumit index) si <b>length</b> (returneaza lungimea unei liste).

## Exercitii

##### 1. Make a reversed list with the even values in [0..n]
##### 2. Get the sum of all the digits in a given string
##### 3. Divisors of a number
##### 4. Make a list of all the square numbers in [1..n]
##### 5. Remove the vowels from every word in a given sentence
##### 6. Delete the duplicates in a list
##### 7. Sort a list of numbers by the number of even digits
##### 8. Find the missing number in [1..n]
##### 9. Calculate the sum of all the elements in a list until the first 0
##### 10. Find the 2nd largest element in a list (duplicates allowed)
##### 11. Find all pairs with a specific sum (don't repeat the same elements)
##### 12. Circular permutations of a list
##### 13. Calculate the sum of all the odd digits in a number
##### 14. Reverse sort a list of lists of numbers by the average
##### 15. Delete all the digits/numbers between the first two 0-digits in a list of numbers
##### 16. Line swapping in a matrix