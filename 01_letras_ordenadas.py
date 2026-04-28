letra1: str = ""
letra2: str = ""
letra3: str = ""

letra1 = input("Ingrese letra #1: ").upper()
letra2 = input("Ingrese letra #2: ").upper()
letra3 = input("Ingrese letra #3: ").upper()

print("Letras ingresadas:", letra1, letra2, letra3)

if letra1 < letra2 and letra1 < letra3:
    if letra2 < letra3:
        print("Letras ordenadas:", letra1, letra2, letra3)
    else:
        print("Letras ordenadas:", letra1, letra3, letra2)
elif letra2 < letra1 and letra2 < letra3:
    if letra1 < letra3:
        print("Letras ordenadas:", letra2, letra1, letra3)
    else:
        print("Letras ordenadas:", letra2, letra3, letra1)
else:
    if letra1 < letra2:
        print("Letras ordenadas:", letra3, letra1, letra2)
    else:
        print("Letras ordenadas:", letra3, letra2, letra1)
