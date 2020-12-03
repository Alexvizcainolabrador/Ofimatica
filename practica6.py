def calcula_total(comida):

    IVA = round((float(comida) * 0.1),2)
    propina = round((float(comida) * 0.1),2)
    total = round((float(comida) + (float(propina)) + (float(IVA))),2)

    print("precio comida = " + str(float(comida)))
    print("IVA = " + str(float(IVA)))
    print("propina = " + str(float(propina)))
    print("total = " + str(float(total)) + "€")

print("1.Pizza     6€")
print("2.Ensalada  4€")
print("3.Kebab     3€")
print("4.Salmon    5€")

num_ordre = int(input("Escribe el numero del plato: "))
    
if num_ordre == 1:
    calcula_total(6)
elif num_ordre == 2:
    calcula_total(4)
elif num_ordre == 3:
    calcula_total(3)
elif num_ordre == 4:
    calcula_total(5)