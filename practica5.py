print ("Coste de la comida ordenada en el restaurante.")
precio= input ("¿Que os a costato la comida en el restaurante? ")

a= float (precio)

iva= a*0.1
b= (iva)
print("IVA es de: " +str (b)+"€")

propina= a*0.1
c= (propina)
print("La propina es de: " +str (c)+ "€")

precio_total= a+b+c
print("El precio total es de: "+str(precio_total)+"€")