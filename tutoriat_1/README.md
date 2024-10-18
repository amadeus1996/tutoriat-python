# Tutoriat 1
---

## Table of contents

1. Introducere in Python

2. Instructiuni

3. Siruri de caractere

---

## 1. Introducere in Python

### Ce e Python?

- Limbaj de programare de nivel inalt
- Folosit in general pentru **web development**, **data science**, **AI** si **automatizare**

### De ce Python?
- Sintaxa simpla
- Comunitate mare si un ecosistem bogat de biblioteci
- Versatil si utilizat in multe industrii

## 2. Instructiuni

### Primul program in Python
```
name = "John Doe"
age = 21
print("My name is " + name + " and I have " + age + " years")
```

### Atentie la import-uri

a.py
```
name = "John Doe"
age = 21
print(f'My name is {name} and I am {age} years old')
```
b.py
```
import a

print(f'My name is not John Doe')
```

Afiseaza: 
```
My name is John Doe and I am 21 years old
My name is not John Doe
```

Pentru a rezolva problema codului rulat la import, se pune codul intr-o functie si se apeleaza functia intr-un if 
`if __name__ == "__main__":`
Deci a.py v-a arata astfel:
```
def printJohn():
    name = "John Doe"
    age = 21
    print(f'My name is {name} and I am {age} years old')

if __name__ == "__main__":
    printJohn()
```
Pentru mai multe detalii, accesati [aici](https://stackoverflow.com/questions/419163/what-does-if-name-main-do)

## 3. Siruri de caractere

### Probleme

##### 1. Reverse a String
##### 2. Count Vowels
##### 3. Check if a String is a Palindrome
##### 4. Count Occurrences of a Substring
##### 5. Remove Whitespace from a String
##### 6. Convert a String to Uppercase
##### 7. Replace Characters in a String
##### 8. Check if a String Contains Only Digits
##### 9. First Non-Repeated Character
##### 10. Longest Word in a Sentence
##### 11. Anagram Check
##### 12. Find All Substrings
##### 13. Capitalize First Letter of Each Word
##### 14. Compress a String
##### 15. Check if One String is a Rotation of Another
##### 16. Check for Balanced Parentheses
##### 17. Remove Duplicates in a String
##### 18. Find the Most Frequent Character
##### 19. Check if String is a Valid Shuffle of Two Strings