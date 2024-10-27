print("1. ERORI LA DESCHIDEREA FISIERELOR")
try:
    f = open("test.txt")
    # f = open("abc.txt")
    f.close()
    print("Success \"r\"")
except FileNotFoundError:
    print("File not found \"r\"")


print()
try:
    # f = open("D:D\\tetst.txt", "x")
    f = open("test.txt", "x")
    f.close()
    print("Success \"x\"")
except FileNotFoundError:
    print("Wrong path \"x\"")
except FileExistsError:
    print("File already exists \"x\"")
print()


print("2. CITIREA DATELOR DINTR-UN FISIER")
f = open("elevi.in")

# aux = f.read()
# print(aux)

# aux = f.readline()
# print(aux)
# aux = f.readline()
# print(aux)

aux = f.readline()
while aux != "":
    print(aux, end = "")
    aux = f.readline()

# for aux in f:
    # print(aux)

# aux = f.readlines()
# print(aux)

print("\n")
f.close()


print("3. SCRIEREA DATELOR INTR-UN FISIER")

f = open("write.txt", "w")

# f.write("Test")
# f.write("Fisier")

# aux = ["Un", "Text", "Scurt"]
# f.writelines(aux)

print()
f.close()


print("4. SINTAXA CU \"with\"")
with open("elevi.in", "r") as f:
    for _ in range(int(f.readline())):
        print(f.readline(), end = "")