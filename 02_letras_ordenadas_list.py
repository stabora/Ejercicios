import locale
import re

MAXIMO_LETRAS: int = 27
cantidad_letras: int = 0
letras: list[str] = []
letra_valida = re.compile("^[A-ZÑ]$", flags=re.IGNORECASE)
locale.setlocale(locale.LC_ALL, "es_AR.UTF-8")

while not cantidad_letras > 0:
    try:
        cantidad_letras = int(input("Cantidad de letras: "))

        if cantidad_letras > MAXIMO_LETRAS:
            cantidad_letras = 0
            raise ValueError
    except ValueError:
        print("Valor no admitido")
        cantidad_letras = 0

for ingreso in range(cantidad_letras):
    letra: str = ""

    while letra == "":
        letra: str = input(f"Ingrese letra {ingreso + 1} de {cantidad_letras}: ").upper()

        if not letra_valida.match(letra):
            print("Valor no admitido")
            letra = ""
        elif letra in letras:
            print("Letra ya ingresada:", " - ".join(letras))
            letra = ""

    letras.append(letra)

print("Letras ingresadas:", " - ".join(letras))
print("Letras ordenadas:", " - ".join(sorted(letras, key=locale.strxfrm)))
