"""
Guillem González Rodríguez
ASIXc 1C
1/2/2024


Lista 1M palabras
print lista
max min y avg de len(palabras)(mostrar calcs)
copiar a tuple
"""

minim = 100
maxim = 0
suma = 0
lista = []
llistamins = []

for m in range(1000000):
    paraula = input()
    if paraula == "\q":
        break
    else:
        lista.append(paraula)

print(lista)

for n in lista:
    if len(n) > maxim:
        maxim = len(n)
    elif len(n) < minim:
        minim = len(n)

    suma += len(n)
    print("lletres totals: ", suma)

avg = round(suma/(len(lista)), 3)

print("Màxima: ", maxim,
      "\nMínima: ", minim,
      "\nMitjana: ", suma, "/", len(lista), "=", avg)

for n in lista:
    if len(n) == minim:
        llistamins.append(n)
        llistamins.append(minim)

TUPLAMINS = tuple(llistamins)
print(TUPLAMINS)
