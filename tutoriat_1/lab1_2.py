#LAB 1

def palindrom(n):
    s = str(n)
    print(s == s[::-1])    

def valutar(n, l):
    dif_max = 0
    zi1,zi2 = 0,0
    for i in range(len(l)-1):
        if l[i+1] - l[i] > dif_max:
            dif_max = l[i+1] - l[i]
            zi1, zi2 = i, i+1
    print(round(dif_max, 2), zi1, zi2)

def cmmdc(a, b):
    while b:
        a, b = b, a % b
    return a

def mester(l1, l2):
    n = cmmdc(l1, l2)
    print(f'nr placi: {l2 // n * l1 // n}, marimea: {n}')

def cele_mai_mari_2(l):
    s = set(c for c in l if l.count(c) == 1)
    print(s)
    
def ordonare_cifre(n):
    s = str(n)
    s = sorted(s)
    print(int("".join(s)))
    s = sorted(s, reverse=True)
    print(int("".join(s)))


def lab1():
    palindrom(123432)
    valutar(6, [4.25, 4.05, 4.25, 4.48, 4.30, 4.40])
    mester(440, 280)
    cele_mai_mari_2([1,1,2,3,4,5,6,7,7])
    ordonare_cifre(812383)

# lab 2 - stringuri

def sterge_prima_litera(s):
    litera = s[0]
    s = s.replace(litera, "")
    print(s)

def gaseste_toate_subsirurile(s, subsir):
    t = s.find(subsir)
    print(t)
    while t != -1:
        t = s.find(subsir, t+1)
        print(t)

def ana_jurnal(s):
    l = [int(c) for c in s.split() if c.isdigit()]
    print(sum(l))

def pasareascaAcodificare(s):
    vowels = "AEIOUaeiou"
    l = [c + "pa" if c in vowels else c for c in s]
    s = "".join(l)
    print(s)

def pasareascaAdecodificare(s):
    vowels = "AEIOUaeiou"
    s1 = ""
    i = 0
    while i < len(s):
        c = s[i]
        if c in vowels:
            i += 2
        s1 += c
        i += 1
    print(s1)

def codificare_silabe(text):
    cu_silabe = ""
    fara_silabe = ""
    cuvinte = text.split()
    for cuvant in cuvinte:
        silabe = cuvant.split('-')
        for silaba in silabe:
            ultima_litera = silaba[-1]
            codificata = silaba + 'p' + ultima_litera
            cu_silabe += codificata + '-'
            fara_silabe += codificata
        cu_silabe = cu_silabe[:-1] + " " 
        fara_silabe += " "
    
    return cu_silabe.strip(), fara_silabe.strip()

def decodificare_silabe(text):
    cuvinte = text.split()  
    rezultat = ""
    for cuvant in cuvinte:
        silabe = cuvant.split('-')
        for silaba in silabe:
            ultima_litera = silaba[-1]
            if len(silaba) > 2 and silaba[-2] == 'p' and silaba[-1] == ultima_litera:
                silaba_originala = silaba[:-2]
                rezultat += silaba_originala + '-'
            else:
                rezultat += silaba + '-'
        rezultat = rezultat[:-1] + " "
    return rezultat.strip()


sterge_prima_litera('ananas')
gaseste_toate_subsirurile("abccabcababcc", 'abc')
ana_jurnal("Ana a cheltuit 5 RON pe adidasi si 10 RON pe ghete")
pasareascaAcodificare("Apana are mere")
pasareascaAdecodificare("Apapapanapa aparepa meparepa")


text_silabe = "a-na a-re mul-te me-re ro-sii si de-li-cioa-se."
text_codificat_cu, text_codificat_fara = codificare_silabe(text_silabe)
text_decodificat = decodificare_silabe(text_codificat_cu)

print("Text codificat cu cratime:", text_codificat_cu)
print("Text codificat fără cratime:", text_codificat_fara)
print("Text decodificat:", text_decodificat)
