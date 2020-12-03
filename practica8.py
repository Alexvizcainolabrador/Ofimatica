def obtener_vocales(frase):
    vocales = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]

    num_vocales = 0

    for letra in frase:
        if  letra in vocales:
            num_vocales = num_vocales + 1

    print(num_vocales)

frase = input("Escribe una frase aleatoria")

obtener_vocales(frase)