# Exercitii recapitulative

Pana acum am facut:
- Strings
- Liste
- Fisiere
- Tupluri
- Seturi
- Dictionare
- Functii

// vreau sa pun niste exercitii care sa ii treaca inca o data prin ce au facut, si in acelasi timp sa fie clean code

**Exercitii:**

1. **Stocare și căutare de produse**: Creează un dicționar care mapează produse la prețuri. Oferă utilizatorului opțiunea de a adăuga un produs nou creand o functie numita ```adaugare_produs(nume_produs, pret_produs)```, de a actualiza prețul unui produs existent creand o functie ```actualizeaza_produs(nume_produs, pret_nou)``` (nu uitati sa vedeti daca cheia pe care o primiti exista in dictionar) și de a căuta prețul unui produs printr-o functie ```cauta_pret(nume_produs)```. Apelati functiile la final si aratati un flow al aplicatiei.

2. **Dicționar de studenți**: Creează un dicționar care stochează numele studenților și nota lor la un examen. Scrie funcții care adaugă un nou student, actualizează nota unui student existent și calculează media notelor.

3. **Catalog de cărți**: Ai un fișier ```carti.txt``` în care fiecare linie conține informații despre o carte: **titlul**, **autorul** și **anul publicării**, separate prin virgulă (ex. Harry Potter, J.K. Rowling, 1997). Creează un program care:

- Citește fișierul și creează un dicționar în care cheia este autorul, iar valoarea este o listă de titluri ale cărților acestuia.
- Întoarce o listă cu toți autorii unici și o listă cu toate cărțile scrise de un autor specificat de utilizator.
- Scrie datele într-un fișier catalog_autori.txt, grupate pe autori.

**Hint**: Creează funcții pentru citirea fișierului, crearea dicționarului, obținerea autorilor unici și scrierea în fișier.

4. **Top produse vândute**: Ai un fișier ```vanzari.txt``` cu produsele vândute, fiecare linie conținând produsul și cantitatea vândută, separate prin virgulă. Creează un program care:

- Citește fișierul și calculează cantitatea totală vândută pentru fiecare produs.
- Găsește produsul cu cea mai mare și cea mai mică cantitate vândută.
- Afișează top 3 cele mai vândute produse.

**Hint**: Creează funcții pentru citirea fișierului, calculul cantităților, găsirea top-ului și afișarea rezultatelor.

5. **Monitorizare inventar**: Ai două fișiere ```stoc_initial.txt``` și ```vanzari.txt```. ```stoc_initial.txt``` conține produsele și stocul inițial, iar ```vanzari.txt``` conține produsele și cantitatea vândută. Creează un program care:

- Citește ambele fișiere și actualizează stocul fiecărui produs în funcție de vânzări.
- Verifică dacă stocul este insuficient pentru vânzările cerute și afișează un mesaj de avertizare pentru fiecare produs cu stoc insuficient.
- Scrie noul stoc în stoc_actualizat.txt.

**Hint**: Creează funcții pentru citirea stocului inițial, actualizarea stocului în funcție de vânzări și scrierea în fișier.

6. **Analiză de date meteo**: Ai un fișier ```temperaturi.txt``` care conține temperaturile zilnice dintr-o lună, pe fiecare linie fiind temperatura în grade Celsius. Creează un program care:

- Citește fișierul și adaugă temperaturile într-o listă.
- Găsește temperatura maximă, minimă și media lunară.
- Afișează un raport care include cele trei valori, și scrie raportul într-un fișier raport_temperaturi.txt.

**Hint**: Creează funcții pentru citirea fișierului, calculul valorilor și scrierea raportului.

7. **Analiză rețele sociale**: Ai un fișier ```likeuri.txt``` în care fiecare linie conține numele unei persoane și numărul de like-uri primite într-o zi. Creează un program care:

- Citește fișierul și creează un dicționar cu persoanele și numărul total de like-uri pentru fiecare.
- Găsește persoana cu cele mai multe și cele mai puține like-uri.
- Afișează o listă a tuturor persoanelor, în ordine descrescătoare a like-urilor.

**Hint**: Creează funcții pentru citirea fișierului, calculul totalurilor, sortare și afișare.

8. **Analiză de tranzacții bancare**: Ai un fișier ```tranzactii.txt``` în care fiecare linie conține un nume de cont, tipul tranzacției (depunere sau retrage), și suma tranzacției. Creează un program care:

- Citește fișierul și stochează informațiile într-un dicționar cu sumele curente ale fiecărui cont.
- Afișează soldul final pentru fiecare cont.
- Verifică dacă vreun cont are sold negativ și afișează un mesaj de avertizare pentru fiecare astfel de cont.

**Hint**: Creează funcții pentru citirea fișierului, actualizarea soldurilor și afișarea avertismentelor.
