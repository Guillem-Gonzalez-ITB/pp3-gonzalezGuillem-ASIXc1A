"""
Guillem González Rodríguez
ASIXc 1C
1/2/2024


num files i columnes matriu (input)
comprovar files == columnes
files%2 == 0
1 a les vores 0 a la resta
print matriu
"""
try:
    files = int(input())
    columnes = int(input())

    if files == columnes and files % 2 == 0:
        for n in range(files):
            for m in range(files):
                if n == 0 or n == files-1 or m == 0 or m == files-1:
                    print("[1]", end="")
                else:
                    print("[0]", end="")

            print()
    else:
        print("error")
except:
    print("error")
