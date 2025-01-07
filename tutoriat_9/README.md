

# Programare Dinamică

---

### Table of contents
- [Ce este programarea dinamică](#ce-este-programarea-dinamică)
- [De ce avem nevoie de DP?](#de-ce-avem-nevoie-de-programare-dinamică)
- [Cum se rezolvă problemele prin DP?](#cum-se-rezolvă-problemele-prin-programare-dinamică)
- [Gândirea din spate pentru DP](#gândirea-din-spate-pentru-dp)
- [Exerciții](#exerciții)

### **Ce este Programarea Dinamică?**

**Programarea Dinamică (DP)** este o metodă de rezolvare a problemelor care implică împărțirea unei probleme complexe în subprobleme mai mici, rezolvarea acestora și reutilizarea soluțiilor pentru a evita calculul repetitiv.  
Pe scurt, este o tehnică bazată pe:  
1. **Divizare**: Împărțirea problemei în subprobleme mai simple.  
2. **Memoizare**: Salvarea soluțiilor pentru subprobleme ca să nu le recalculăm.  
3. **Reutilizare**: Folosirea rezultatelor din subprobleme pentru a rezolva problema principală.

---

### **De ce avem nevoie de Programare Dinamică?**

Problemele pe care le rezolvăm cu DP au, de obicei, **calcul repetitiv**, ceea ce face ca soluțiile brute să fie ineficiente. Exemple:  
- Numărarea căilor într-o matrice (labirint).  
- Obținerea celei mai mari sume posibile dintr-o serie de numere.  

DP reduce **timpul de execuție** prin evitarea recalculării soluțiilor la aceleași subprobleme.

Programarea Dinamică este folosită pentru a rezolva:  
- Probleme de **optimizare** (ex. găsirea unei soluții maxime/minime).  
- Probleme **combinatorice** (ex. numărarea căilor posibile).  
- Probleme de **decizie** (ex. poate sau nu să fie rezolvată problema cu constrângeri date).  

---

### **Cum se rezolvă problemele prin Programare Dinamică?**

#### **Exemplu 1: Problema Fibonacci**
**Problema:** Găsește al n-lea număr din seria Fibonacci.  
Formula:  
\[
F(n) = 
\begin{cases} 
1 & \text{dacă } n = 1 \text{ sau } n = 2 \\
F(n-1) + F(n-2) & \text{altfel}
\end{cases}
\]

---

#### **Soluție cu Recursie (ineficientă):**
```python
def fibonacci(n):
    if n <= 2:
        return 1
    return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(10))  # Output: 55
```

Dezavantaj: Aceasta recalculă aceleași valori de mai multe ori.  

---

#### **Soluție cu Programare Dinamică (Memoizare):**
```python
def fibonacci_dp(n, memo={}):
    if n in memo:
        return memo[n]
    if n <= 2:
        return 1
    memo[n] = fibonacci_dp(n-1, memo) + fibonacci_dp(n-2, memo)
    return memo[n]

print(fibonacci_dp(10))  # Output: 55
```

Explicație: Memorăm rezultatele în dicționarul `memo`.

---

#### **Soluție cu Programare Dinamică (Iterativă):**
```python
def fibonacci_iterative(n):
    if n <= 2:
        return 1
    dp = [0] * (n + 1)
    dp[1], dp[2] = 1, 1
    for i in range(3, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
    return dp[n]

print(fibonacci_iterative(10))  # Output: 55
```

Explicație: Folosim un tabel (`dp`) pentru a salva rezultatele intermediare.

---

### **Gândirea din spate pentru DP**

1. **Identificarea subproblemelor**: Care este cea mai simplă versiune a problemei?  
   Exemplu: În problema Fibonacci, subproblemele sunt calcularea \( F(n-1) \) și \( F(n-2) \).  

2. **Definirea relației de recurență**: Cum depinde soluția curentă de subprobleme?  
   Exemplu: \( F(n) = F(n-1) + F(n-2) \).  

3. **Memoizare sau tabulare**: Alegi să folosești memoizarea (salvare recursivă) sau tabulare (salvare iterativă).  

4. **Construcția soluției**: Cum combini soluțiile subproblemelor pentru a rezolva problema principală?

---

### **Exerciții**

#### **1. Problema Drumului Maxim (Matrix Path Sum)**
**Problema:** Găsește suma maximă pe care o poți obține mergând din colțul stânga-sus al unei matrice la colțul dreapta-jos. Te poți deplasa doar în jos sau la dreapta.  

**Intrare:**  
Matricea:  
\[
\begin{bmatrix}
1 & 3 & 1 \\
1 & 5 & 1 \\
4 & 2 & 1
\end{bmatrix}
\]

**Ieșire:**  
Suma maximă: 12 (\(1 \to 3 \to 5 \to 2 \to 1\)).

---

#### **2. Problema Rucsacului (0/1 Knapsack Problem)**
**Problema:** Ai un rucsac de capacitate \( W \) și \( n \) obiecte. Fiecare obiect are o greutate și o valoare. Găsește valoarea maximă pe care o poți transporta în rucsac.  

**Exemplu:**  
Obiecte:  
\[
\text{Greutăți}: [1, 3, 4, 5], \quad \text{Valori}: [1, 4, 5, 7]
\]  
Capacitate rucsac: \( W = 7 \).  

**Ieșire:**  
Valoarea maximă: \( 9 \) (\( Obiectul\ 2 + Obiectul\ 3\)).