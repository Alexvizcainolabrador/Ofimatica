def calcula_precio_total(comida) :
    IVA = round((float(comida) * 0.1),2)
    Propina = round((float(comida) * 0.1),2)
    Precio_total = round((float(comida) + float(IVA) + float(Propina)),2)

    print("\nPrecio de la comida: " + str(float(comida)))
    print("IVA: " + str(float(IVA)))
    print("Propina: " + str(float(Propina)))
    print("Precio total: " + str(float(Precio_total))+ "\n")

    return Precio_total


num_personas = int(input("¿Cuantos sois? "))


precio_total = 0
for i in range(num_personas):

    print("Elige el plato")
    print("1- Pizza 6€")
    print("2- Ensalada 4€")
    print("3- Kebab 3€")
    print("4- Salmón 8€")

    num_orden = int(input("\n Escribe el numero del plato: "))

    if num_orden == 1:
        precio_plato = calcula_precio_total(6)
    elif num_orden == 2:
        precio_plato = calcula_precio_total(4)

    elif num_orden == 3:
        precio_plato = calcula_precio_total(3)
    elif num_orden == 4:
        precio_plato = calcula_precio_total(8)
    else:
        print("no tenemos ese plato.")
        precio_plato = 0

    precio_total = precio_total + precio_plato

print("El precio total es " + str(round(precio_total,2)) + "€")