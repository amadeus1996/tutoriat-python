# Set cu elemente unice
numere = {1, 2, 3, 4}
numere.add(5)
print(numere) # Output: {1, 2, 3, 4, 5}

if 3 in numere:
    print("3 este în set")

A = {1, 2, 3}
B = {3, 4, 5}
print(A | B)  # Reuniune: {1, 2, 3, 4, 5}
print(A & B)  # Intersecție: {3}