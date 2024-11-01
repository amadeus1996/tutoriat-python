varste = dict()

with open('course-examples/date.txt') as f:
    for line in f:
        date = line.split(',')
        # strip pentru a scapa de '\n' de la final
        varste[date[0]] = date[1].strip()

for (k, v) in varste.items():
    print(k, v)

# schimbam varsta Anei
print(f'Ana are {varste["Ana"]} de ani, inainte de schimbare')

varste["Ana"] = 42

print(f'Ana are {varste["Ana"]} de ani, dupa schimbare')

# verificam daca un nume dat exista in dictionar
nume_de_verificat = "Petre"

if nume_de_verificat in varste:
    print("Exista numele")
else:
    print("Nu exista numele")

del varste["Ana"]

print(varste)