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

momentan mi-e putin asa sa fac teoria aici, dar va prezentam teoria la tutoriat ca lumea (si mai gasiti teorie prin pdf-ul ala)

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