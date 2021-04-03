
######### FUNCIONES ###########
def pedirNumeroEntero():

	correcto=False
	num=0
	while(not correcto):
		try:
			num = int(input("Introduce un numero entero: "))
			correcto=True
		except ValueError:
			print('Error, introduce un numero entero')
	return num

def UNION_func(A,B):
	print("A U B:" ,A," U ", B)
	U = list(set(A) | set(B))
	return U

def INTERSEC_func(A,B):
	print("A ∩ B:" ,A," ∩ ", B)
	U = list(set(A) | set(B))
	return U
####################


######### VARIABLES ###########
salir = False
opcion = 0
####################

#TODO: COMO INTRODUCIR UNA LISTA VACIA!!!!! 
#obtenemos los conjuntos A, B y C
arr = input("\nConjunto A: ")   #A
A = list(map(int,arr.split(','))) #quitamos las comas y guardamos en un arreglo

arr = input("\nConjunto B: ")   #B
B = list(map(int,arr.split(','))) #quitamos las comas y guardamos en un arreglo

arr = input("\nConjunto C: ")   #C
C = list(map(int,arr.split(','))) #quitamos las comas y guardamos en un arreglo

print("\n############### CONUNTOS ###############")
print("A: ",A)
print("B: ",B) 
print("C: ",C)
print("\n###########################\n")

#MENU
while not salir:

	print("\n############### OPERACIONES DISPONIBLES ###############")
	print ("1. UNION")
	print ("2. INTERSECCION")
	print ("3. DIFERENCIA")
	print ("4. DIFERENCIA SIMETRICA")
	print ("5. SALIR")

	opcion = pedirNumeroEntero()

	if opcion == 1:
		#UNION
		print(UNION_func(A,B))
	elif opcion == 2:
		#INTERSECCION
		print(INTERSEC_func(A,B))
	elif opcion == 3:
		print("Opcion 3")
	elif opcion == 4:
		print("Opcion 3")
	elif opcion == 5:
		salir = True
	else:
		print ("Elige alguna de las opciones")

print ("Gracias")
