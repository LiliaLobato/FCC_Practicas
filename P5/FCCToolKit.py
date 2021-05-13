
######### VARIABLES ###########
salir = False
opcion = 0

######### MENU PRINCIPAL ###########
while not salir:

	print("\n############### Bienvenido ###############")
	print ("1. TABLAS DE VERDAD")
	print ("2. CONJUNTOS")
	print ("3. SUCESIONES")
	print ("4. RELACIONES")
	print ("5. SALIR")

	opcion = int(input("Introduce la operacion deseada: "))

	if opcion == 1: #TABLA DE VERDAD
		import truthTable
	elif opcion == 2: #CONJUNTOS
		import conjuntos
	elif opcion == 3: #SUCECIONES
		import sucesiones
	elif opcion == 4: #RELACIONES
		import RelacionesFunciones
	else:
		salir = True 

print ("Gracias")