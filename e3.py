"""
Guillem González Rodríguez
ASIXc 1C
1/2/2024


num files i columnes matriu (input)
"""

frase = str.upper(input())

LLETRES = ("A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M",
           "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z")

for lletra in frase:
    if lletra in LLETRES:
        print(ord(str(lletra))-65, end=":")

    else:
        print("\b", lletra, end="")
print("\b")
