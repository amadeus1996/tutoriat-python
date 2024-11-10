# EX 1
def ex1(*nums):
    suma, produs = 0, 1
    for x in nums:
        suma += x
        produs *= x
    return suma, produs 

print(ex1(1, 3, 5, 10), end = "\n\n")


# EX 2
def ex2(t, n = 1):
    aux = len(t) - n 
    if aux >= 0:
        del t[aux:]
    else:
        del t[0:]

t = [1, 2, 3, 4, 5]
ex2(t, 3)
print(t)
ex2(t)
print(t)
ex2(t, 4)
print(t, end = "\n\n")


# EX 3
def ex3(n):
    if n < 1:
        return None 
    def factorial(x):
        fact = 1
        while x > 0:
            fact *= x 
            x -= 1
        return fact
    return factorial(n)

print(ex3(4), end = "\n\n")


# EX 4
def ex4(s):
    return len([c for c in s if c in "aeiouAEIOU"])

print(ex4("text sample"), end = "\n\n")


# EX 5
def ex5(s, f):
    return " ".join(sorted(s.split(), key = f, reverse = True))

print(ex5("mar barca medalie perdea usa lalele aerisire", ex4), end = "\n\n")


# EX 6
print(ex5("mar barca medalie perdea usa lalele aerisire", lambda x: len([c for c in x if c in "aeiouAEIOU"])), end = "\n\n")


# EX 7
nums1 = [94, 0, 13, 28, 55, 14, 19, 20, 3, 188, 26, 264, 652, 110]
nums1.sort(key = lambda x: (len(str(x)), -(x % 10), sum([int(y) for y in str(x) if int(y) % 2 == 1])))
print(nums1)


# EX 8
s = "mar barca medalie perdea usa lalele aerisire"
print(sorted(s.split(), key = lambda x: (-ord(x[0]), x[-1])))