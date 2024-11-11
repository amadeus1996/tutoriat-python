# Tutoriat 4

## Table of contents
- [Functii](#1---functii)
- [Functii lambda](#2---functii-lambda)
- [Sortari](#3---sortari)
- [Exercitii](#4---exercitii)

## 1 - Functii

### <ins>1.1 - Notiuni introductive</ins>
Functiile le stiti deja din <b>C++</b> (sau orice alt limbaj studiat pana acum): o functie este un set de instructiuni ce efectueaza o sarcina specifica; aceste instructiuni sunt scrise sub un nume unic si pot fi apelate. Functiile sunt doar o utilitate disponibila pentru organizarea unui program - ele pot modifica date, scrie date in fisiere, afisa date pe consola, etc.

Principalul avantaj al functiilor este ca grupeaza blocuri reutilizabile de cod, pentru a evita rescrierea continua a codului si pentru a minimiza numarul de linii intr-un mod accesibil, oferind ordine si claritate. Subliniez faptul ca organizarea eficienta a codului este o cerinta imperativa in orice subdomeniu al programarii.

Este de tinut minte faptul ca nu este necesar ca tipul de date returnat sau tipurile de date ale parametrilor sa fie specificate (totusi, merge facut acest lucru). Mai jos gasiti sintaxa pentru functiile din <b>C++</b> si <b>Python</b> (le-am inclus pe amandoua pentru a putea compara):

    1. C++:
    tip_return nume_functie(tip arg1, tip arg2, ...) {
        ...instructiuni...
    }
    
    2. Python:
    def nume_functie(arg1, arg2, ...):
        ...instructiuni...
        
    3. Python (specificand tipurile de date):
    def nume_functie(arg1: tip, arg2: tip, ...) -> tip_return:
        ...instructiuni...

Evident, argumentele sunt optionale - o functie poate sa nu aiba parametri.

### <ins>1.2 - Ce returneaza o functie?</ins>
Functiile din <b>Python</b> pot returna orice tip de date; mai important este faptul ca pot returna mai multe valori. De exemplu, instructiunea "<b>return x</b>" este intuitiva, dar exista si posibilitatea de a scrie instructiuni precum "<b>return x, y, z</b>".

Din acest motiv, exista 2 tipuri de date returnate: <b>valori individuale</b> (o functie poate sa returneze un int, o lista, un dictionar, un bool, o structura definita de noi) sau <b>tupluri de date</b> (cand se returneaza mai multe lucruri, sunt stocate intr-un tuplu care este apoi returnat de functie).

    def f(t):
        return [-x for x in t]

    def g(sir):
        aux = sir.split()
        return aux, len(aux), aux[-1]
    
    print(f([1, 3, 6])) # [-1, -3, -6]
    print(g("Text sample")) # (["Text", "sample"], 2, "sample")

    
### <ins>1.3 - Tipuri de parametri</ins>
* <b>Parametri simpli</b>: sunt doar niste argumente obisnuite; o functie cu <b>n</b> parametri simpli va avea tot <b>n</b> argumente in apelul acesteia.

        def printString(s):
            print(s)
            
        printString("Text sample") # apelam functia
        # se afiseaza pe ecran "Text sample"
        
        # printString() # acest apel va da eroare
        # nr. de argumente din apel difera de nr. de parametri (0 != 1)
        
        # printString("Text", "sample") # eroare
        # nr. de argumente != nr. de parametri (2 != 1)
        
        # --------------------------------------------
        
        def quadratic(a, b, c, x):
            return a * x ** 2 + b * x + c

        print(quadratic(3, 1, 2, 2))

        print(quadratic(b = 5, a = 1, x = 2, c = 4))
        
        # --------------------------------------------

* <b>Parametri cu valori implicite</b>: in cazul in care o functie este apelata fara sa primeasca anumiti parametri, acestia pot avea valori implicite. Un exemplu practic - un serviciu costa implicit <b>N</b> lei, dar daca se specifica si alte conditii particulare, pretul creste in functie de cerinte. Acele conditii ar avea implicit valoarea "<b>false</b>" ca sa nu afecteze pretul, si devenind "<b>true</b>" daca sunt explicit mentionate.

        def afisare(varsta, nume = "anonim"):
            print(f"Varsta: {varsta}\nNume: {nume}\n")
            
        afisare(18) # apel corect
        # Varsta: 18
        # Nume: anonim
        
        afisare(22, "Dana") # apel corect
        # Varsta: 22
        # Nume: Dana
        
        # ce se intampla aici?
        afisare("Nume")
        afisare()
        
        # --------------------------------------------
        
        def afisare_type(varsta: int, nume: str = "anonim") -> None:
            print(f"Varsta: {varsta}\nNume: {nume}\n")
            
        afisare_type(18) # apel corect
        
        afisare_type(22, "Dana") # apel corect
        
        # ce se intampla aici?
        afisare_type("Nume")
        afisare_type()
        
        # --------------------------------------------
        
        def add(x = 0, y = 0):
            return x - y
        
        # ce valoare are x dupa fiecare apel?    
        x = add()
        
        x = add(1)
        
        x = add(1, 2)
        
        x = add(y=3, x=10)
        
        x = add(y=5)
        
        x = add(1, 2, 3)
    
        # -------------------------------------------
        
        # ce se intampla cu aceste functii?
        
        def f(a = 10, b = 10, c):
            return a + b - c
        
        def f(a, b = 2, c):
            return a * b * c
        
        # -------------------------------------------
        
        # o functie poate sa primeasca alte functii ca si parametri
        def suma(x = 0, y = 0):
            return x + y 

        def f(x, y, g):
            return x * y - g(x, y)

        print(f(3, 5, suma))

        print(f(suma(1, 2), 3, suma))

* <b>Numar variabil de parametri</b>: in programul nostru putem avea o functie care concateneaza 2 siruri de caractere, o functie care calculeaza suma a 3 numere, una care returneaza numerele negative dintr-o lista, etc. Totusi, cand vrem sa definim o functie cu un comportament general (suma pentru n numere, concatenarea a k siruri de caractere), aici intervine numarul variabil de argumente. Sintaxa este <b>*nume_parametru</b>; putem da oricat de multe argumente dorim, iar acestea vor fi stocate intr-un tuplu, ulterior putand fi accesate.

        def f(*args):
            return sum([x for x in args if type(x) == int])

        print(f(1, "test", [1, 2, 3], 50, False, 3.14, 60)) 
        # se va afisa 111
        
        # -------------------------------------------
        
        # cum credeti ca se apeleaza aceasta functie?
        def g(*args, n):
            return sum([x % n for x in args if type(x) == int])

### <ins>1.4 - Transmiterea parametrilor</ins>
In <b>C++</b> parametrii pot fi transmisi in 2 moduri - prin <b>valoare</b> (se transmite o copie a valorii parametrului, deci modificarile asupra acestuia nu se reflecta in exterior) sau prin <b>referinta</b> (se transmite adresa parametrului, deci modificarile efectuate in interior sunt vazute in exterior).

In <b>Python</b>, transmiterea parametrilor are loc intr-un stil mai diferit, care combina cele 2 metode: <b>transmitere prin referinta la obiect</b> (call by object reference).

In primul rand, toate variabilele din Python sunt doar niste referinte catre obiecte in memorie. Cand avem, de exemplu, "<b>x = 2</b>", <b>x</b> este o referinta catre adresa unui obiect din memorie. Daca vrem sa ii schimbam valoarea scriind, de exemplu, "<b>x = 10</b>", asta nu va modifica valoarea obiectului, ci va crea un obiect nou in memorie cu valoarea 10 (si acum avem 2 obiecte - cel cu valoarea 2 si cel cu valoarea 10), apoi <b>x</b> primeste noua adresa catre acel obiect, iar in cazul in care nu mai exista referinte catre vechiul obiect, acesta este sters.

Care este diferenta dintre 2 obiecte in memorie? Acestea se diferentiaza prin <b>identificatoare</b> (care sunt unice, sub forma de numere), iar 2 obiecte au ID-uri diferite cand au valori diferite. 

    x = 1
    y = 1
    # id-urile pentru x si y sunt egale
    print(id(x))
    print(id(y))

    # -------------------------------------------

    a = 2
    b = x + 1
    c = y * 2
    # id-urile pentru a, b, c cum sunt?
    print(id(a))
    print(id(b))
    print(id(c))

Exista 2 tipuri de date in <b>Python</b> - <b>mutabile</b> si <b>imutabile</b>. Un <b>obiect mutabil</b> este unul care isi poate schimba valoarea (si in acelasi timp sa isi pastreze id-ul); altfel, daca nu isi poate modifica valoarea in memorie, este <b>imutabil</b>. Majoritatea tipurilor de date din <b>Python</b> sunt imutabile, adica valorile lor in memorie nu pot fi modificate; printre acestea se regasesc <b>int</b>, <b>float</b>, <b>bool</b>, <b>str</b>, <b>tuple</b>, etc.

    x = (1, 2, 3)
    print(id(x)) # se va afisa un id
    
    x = True # s-a creat un obiect nou si s-au pierdut toate referintele catre obiectul vechi
    print(id(x)) # alt id
    
Printre tipurile de date mutabile se regasesc, de exemplu, <b>listele</b> si <b>dictionarele</b>; acestea pot sa isi modifice datele fara sa isi schimbe identitatea. De exemplu, metodele <b>append</b>, <b>insert</b> si <b>del</b> modifica doar valoarea si nu creeaza obiecte noi.

In concluzie in legatura cu mutabilitatea datelor, este de tinut minte ca atribuirea unei valori la o variabila folosind operatorul "<b>=</b>" face un obiect nou in memorie si transmite adresa acelui obiect catre variabila. Accesarea datelor pastrate de obiect se realizeaza prin acea adresa, care poate fi accesata la randul ei prin numele variabilei. Modificarea <b>in-place</b> pe tipuri de date <b>mutabile</b> este mult mai rapida decat crearea si stergerea obiectelor din memorie; mai jos am inclus un exemplu practic:

    x = []
    for i in range(100000):
        x.append(i) # in-place, nu modifica identitatea obiectului, doar valoarea
        
    y = []
    for i in range(100000):
        y = y + [i] # se creeaza un obiect nou de fiecare data, foarte lent
        
    # rulati ambele metode separat si trageti o concluzie
    
Revenind la subiectul initial - cand o functie primeste un parametru, ea de fapt primeste o copie a referintei catre acel obiect in memorie. Cand folosim operatorul <b>"="</b> sa atribuim o valoare, de fapt doar modificam valoarea copiei => copia va retine o alta referinta (astfel, va pointa catre alt obiect in memorie), iar obiectul original ramane neschimbat. In acelasi timp, putem folosi metode <b>in-place</b> cum ar fi <b>append</b>, ceea ce modifica datele obiectului original.

    def f1(t):
        # momentan "t" este o copie a referintei catre obiectul original
        t = t + [10] # acum i-am atribuit alta referinta
        # astfel, s-a pierdut referinta catre obiectul original
        # deci cand iesim din functie, t-ul din afara va fi neschimbat
        
    t = [1, 2, 3]
    f1(t)
    print(t) # [1, 2, 3]
    
    # -------------------------------------------

    def f2(t):
        t.append(10)
        t.insert(2, 0)
        del t[0:2]
        # toate metodele sunt in-place, nu fac obiecte noi in memorie

    t = [1, 2, 3]
    f2(t)
    print(t) # [0, 3, 10]

### <ins>1.5 - Variabile locale si globale</ins>
<b>Variabilele locale</b> sunt cele declarate in interiorul functiilor. Acestea nu pot fi accesate in afara functiei (sunt sterse odata ce functia si-a terminat apelul).

    def f():
        x = 5
        print(x)
        
    f() # o sa se afiseze 5, iar x nu mai poate fi accesat

O <b>variabila globala</b> este o variabla declarata in afara oricarei functii. Se pot declara variabile locale care au acelasi nume ca variabilele globale; in acest caz, in interiorul functiei se va lucra cu variabilele locale.

    def f1():
        x = 5
        print(x)
    
    x = 0
    f1() # se va afisa 5
    
    # -------------------------------------------

    def f2():
        for x in nums:
            print(x ** 2, end = " ")
            
    nums = [3, 4, 5, 6]
    f2() # se va afisa 9 16 25 36
    
    # -------------------------------------------

    # ce se intampla aici?
    def f3():
        print(nums)
        nums = [10]
        
    nums = [5]
    f3()
    print(nums)

Cuvantul cheie "<b>global</b>" urmat de numele unei variabile este utilizat pentru a specifica functiei sa lucreze cu acea variabila din exterior (din programul principal), schimbarile asupra ei regasindu-se si in afara functiei (de exemplu, reatribuiri).

    # ce se intampla aici?
    def f():
        global nums
        print(nums)
        nums = [10]
        
    nums = [5]
    f()
    print(nums)

### <ins>1.6 - Functii imbricate</ins>
O functie poate fi definita si apelata in interiorul altei functii; de exemplu, daca in interiorul functiei <b>f</b> definim functia <b>g</b>, atunci vom putea accesa functia <b>g</b> doar din interiorul lui <b>f</b>, nu si din exterior (in programul principal). Acestea se numesc <b>functii imbricate</b>.

O functie imbricata are access la parametrii functiei din care face parte si la variabilele locale ale functiei respective. Totusi, aceasta nu poate modifica variabilele locale ale functiei parinte; se va genera o eroare daca se incearca. Pentru a rezolva aceasta problema, se poate utiliza cuvantul cheie "<b>nonlocal</b>" impreuna cu numele variabilei locale; se va cauta definirea variabilei respective in cel mai apropiat spatiu exterior functiei imbricate (in afara de cel global), iar variabila va putea fi modificata.

Ca si ultim detaliu, functiile imbricate se pot privi in felul urmator: consideram functia parinte ca fiind un fel de "<b>main</b>", iar functia imbricata ca pe o functie normala in programul principal.

    # un exemplu de functii imbricate, utilizand global si nonlocal
    # nu e ceva foarte practic, dar e util pentru a intelege mecanismele
    # de exemplu, puteti comenta anumite linii cum ar fi cea cu "nonlocal z", vedeti ce se intampla
    
    def f(x, y = 1):
        global a
        z = a * (x + y) ** 2

        def g(t):
            nonlocal z
            global b
        
            z *= b 
            return z - t

        return g(5)

    a = 0.5
    b = 10
    print(f(3)) # 75.0

___

## 2 - Functii lambda
O <b>functie lambda</b> este o functie fara nume, cu unul sau mai multi parametri, care returneaza o valoare furnizata de o singura expresie; ele nu pot contine instructiuni sau mai multe expresii, sunt scurte si nu mai pot fi apelate in alte parti din program (pentru ca nu au nume).

Functiile lambda pot avea mai multe tipuri de parametri - <b>simpli</b>, <b>impliciti</b> si <b>numar variabil</b>, si pot returna tupluri de valori. Ele vor fi utilizate cel mai mult in <b>sortari</b> (urmatoarea sectiune).

    t = [0, 1, 2, 3, 4, 5]
    aux = (lambda x: len([i for i in x if i % 2]))(t)
    print(aux) # 3
    
    # -------------------------------------------

    aux = (lambda x, y, z: x ** 3 + y ** 2 - z)(3, 3, 2)
    print(aux) # ce se afiseaza?
    
    # -------------------------------------------

    # transmiterea unei functii lambda ca si parametru
    def f(nums, t, functie):
        suma = 0
        for x in nums:
            suma += (t * functie(x))
        return suma

    nums = [1, 2, 3, 4, 5]
    t = 2
    
    aux = f(nums, t, lambda x: x ** 2 - 1)
    print(aux) # 100
 
___

## 3 - Sortari
In general, sortarile se vor aplica asupra datelor stocate in liste (dar si asupra altor colectii de date). Exista numeroase criterii de sortare in practica - de exemplu, lista de note pentru un student ar putea fi sortata crescator dupa valorile notelor, iar studentii ar putea sa fie sortati descrescator dupa media aritmetica a notelor.

Niste evenimente ar putea sa fie sortate crescator dupa data (pentru a vedea care vor avea loc cel mai devreme), apoi dupa pret (daca au loc in aceeasi data, le vom vedea mai intai pe cele mai ieftine) si descrescator dupa durata (daca au aceeasi data si acelasi pret, vedem care sunt estimate sa dureze cel mai mult). Dupa cum se poate observa, se pot aplica mai multe criterii de sortare in acelasi timp, iar ordinea acestor criterii conteaza.

Sunt 2 metode predefinite pentru sortari - <b>sort()</b> si <b>sorted()</b>; ele sunt folosite in functie de situatie. Metoda <b>sort</b> modifica datele originale (in-place) si n-are nevoie de atribuiri, in timp ce <b>sorted()</b> returneaza o noua lista cu datele sortate si nu modifica datele originale.

De asemenea, exista parametrul <b>reverse</b> care poate avea valoarea "True" sau "False" (datele pot fi sortate in ordine crescatoare sau descrescatoare).

    a = ["un", "text", "scurt", "si", "neordonat"]
    
    a.sort()
    print(a) # ["neordonat", "scurt", "si", "text", "un"]
    
    # -------------------------------------------
    
    b = [1, 4, 0, 6]
    
    sorted(b, reverse = True)
    
    print(sorted(b, reverse = True)) # [6, 4, 1, 0]
    print(b) # ce se afiseaza aici?
    
    # -------------------------------------------
    
    c = [True, -3.14, (False,)]
    
    # ce se intampla pentru ambele variante?
    
    # c.sort()
    
    # print(sorted(c))
    
    # -------------------------------------------
    
    d = (6, 12, 8)
    
    # ce se intampla pentru ambele variante?
    
    # d.sort()
    
    # print(sorted(d))
    
    # -------------------------------------------
    
    e = {
        'x': 20,
        'h': 10,
        'a': 50,
        'v': 18,
        'o': 20
    }
    
    # ce se intampla pentru ambele variante?
    
    # e.sort()
    
    # print(sorted(e))
    
Pentru a putea aplica diverse criterii de sortare in acelasi timp, aici intervine parametrul optional <b>key</b>, caruia ii atribuim o functie cu scopul de a asocia o cheie fiecarui element. De exemplu, in cazul in care vrem sa sortam niste numere intregi in functie de numarul de cifre, numarul "101" va avea cheia "3" (3 cifre), "0" va avea cheia "1", "1555" va avea cheia "4" si asa mai departe. Daca vrem sa sortam in functie de suma cifrelor, atunci numarul "903" va avea cheia "12".

In folosirea parametrului <b>key</b>, i se pot atribui si functii normale, dar si <b>functii lambda</b> (aceasta este o utilitate practica a functiilor lambda).

    def f(t):
        # ce criteriu de sortare este acesta?
        return len(set(str(t)))

    a = [55, 14, 1342, 3, 922, 13003103]
    print(sorted(a, key = f)) # [55, 3, 14, 922, 13003103, 1342]
    
    # -------------------------------------------
    
    b = ["un", "sir", "mai", "scurt"]

    b.sort(key = lambda x: x[-1])
    print(b) # ce se afiseaza? care e criteriul de sortare?
    
    # -------------------------------------------
    
    c = (10, "e"), (15, "c"), (10, "b"), (15, "a"), (8, "h"), (11, "e"), (8, "x")
    
    # aici sunt mai multe detalii
    print(sorted(c, key = lambda x: (-sum([int(y) for y in str(x[0])]), x[1])))
    
    # in primul rand, observati cum am omis parantezele
    # datele sunt separate doar prin virgula
    # cu aceasta sintaxa, am facut un tuplu care sa contina toate acele date
    # deci "c" e un tuplu
    
    # am folosit "sorted"
    # "sort" nu merge pe tupluri (nu poti modifica datele unui tuplu)
    
    # s-au folosit 2 criterii de sortare (intre paranteze, separate prin virgula)
    # deci acea functie lambda returneaza un tuplu cu 2 valori
    # mai intai, se foloseste prima cheie
    # daca pentru 2 valori sunt egale cheile, se trece la a doua cheie 
    
    # prima cheie calculeaza suma cifrelor unui numar intreg
    # dar am pus un "-" fix inainte de rezultat
    # acel "-" face o sortare inversa (un fel de "reverse = True")
    # de ce functioneaza asa?
    # pt ca: [20, 15] devine [2, 6] care devine [-2, -6] => sortarea e [-6, -2]
    # iar [-6, -2] e [15, 20]
    
    # daca valorile sunt egale pentru prima cheie, se trece la a doua
    # a doua cheie sorteaza dupa al doilea element din tuplu
    # adica se sorteaza sirurile crescator
    
    # in final ce se afiseaza?
    # [(8, 'h'), (8, 'x'), (15, 'a'), (15, 'c'), (11, 'e'), (10, 'b'), (10, 'e')]
    
## 4 - Exercitii
1. Definiti o functie care primeste un numar variabil de parametri (numere intregi) si returneaza suma si produsul lor. Apelati functia si afisati rezultatul.
2. Definiti o functie cu 2 parametri: o lista si un numar intreg <b>n</b> cu valoarea implicita 1. Functia doar modifica lista, astfel incat sa fie sterse ultimele <b>n</b> elemente. Daca numarul de elemente care sa fie sterse e mai mare decat numarul de elemente din lista, se vor sterge toate elementele din lista.
3. Definiti o functie care sa returneze numarul de permutari posibile, daca se primesc <b>n</b> numere. Formula pentru permutari este <b>n!</b>, si se vor folosii functii imbricate: se va defini o functie care returneaza factorialul unui numar, in interiorul functiei principale.
4. Definiti o functie care primeste un sir ca si parametru, returnand numarul de vocale din sir.
5. Definiti o functie care sa sorteze cuvintele dintr-o propozitie descrescator dupa numarul de vocale. Aceasta functie va primi 2 parametri: un sir de cuvinte separate prin spatii si o alta functie. Functia va returna noul sir sortat. Apelati functia, transmitand ca si parametru functia definita la exercitiul 4.
6. Apelati functia de la exercitiul 4, transmitand ca si parametru o functie lambda.
7. Sortati o lista de numere intregi crescator dupa numarul de cifre, iar in caz de egalitate, descrescator dupa ultima cifra, iar apoi (in caz de egalitate) crescator dupa suma cifrelor impare. Apelati metoda <b>sort</b>, utilizand o <b>functie lambda</b> ca si cheie.
8. Se da o propozitie (cuvinte separate prin spatii). Sortati descrescator dupa prima litera, iar in caz de egalitate, crescator dupa ultima litera (<b>sort</b> si <b>functii lambda</b>).
