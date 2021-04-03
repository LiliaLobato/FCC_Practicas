
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
	U = list(set(A) | set(B))
	return U

def INTERSEC_func(A,B):
	N = list(set(A) & set(B))
	return N

def DIFF_func(A,B):
	D = list(set(A)-set(B))
	return D

def DIFF_SIM_func(A,B):
	print("A Δ B:" ,A," Δ ", B)
	D = list(list(set(A)-set(B)) + list(set(B)-set(A)))
	return D
####################


######### VARIABLES ###########
salir = False
opcion = 0
sub_opcion = 0
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

#MENU PRINCIPAL
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
		print ("1. A U B")
		print ("2. B U C")
		print ("3. A U C")
		print ("4. A U (B U C)")
		sub_opcion = pedirNumeroEntero()
		if sub_opcion == 1:
			print("A U B:" ,A," U ", B)
			print(UNION_func(A,B))
		elif sub_opcion == 2:
			print("B U C:" ,B," U ", C)
			print(UNION_func(B,C))
		elif sub_opcion == 3:
			print("A U C:" ,A," U ", C)
			print(UNION_func(A,C))
		else 
			#FALTA ESTA OPCIÓN TODO
			print("A U (B U C):" ,A," U ( ", B," U ",C," )")
			print(UNION_func(A,B))

	elif opcion == 2:
		#INTERSECCION
		print ("1. A n B")
		print ("2. B n C")
		print ("3. A n C")
		print ("4. A n (B n C)")
		sub_opcion = pedirNumeroEntero()
		if sub_opcion == 1:
			print("A n B:" ,A," n ", B)
			print(INTERSEC_func(A,B))
		elif sub_opcion == 2:
			print("B n C:" ,B," n ", C)
			print(INTERSEC_func(B,C))
		elif sub_opcion == 3:
			print("A n C:" ,A," n ", C)
			print(INTERSEC_func(A,C))
		else 
			#FALTA ESTA OPCIÓN TODO
			print("A U (B U C):" ,A," U ( ", B," U ",C," )")
			print(INTERSEC_func(A,B))

	elif opcion == 3:
		#DIFERENCIA
		print ("1. A - B")
		print ("2. B - C")
		print ("3. A - C")
		sub_opcion = pedirNumeroEntero()
		if sub_opcion == 1:
			print("A - B:" ,A," - ", B)
			print(DIFF_func(A,B))
		elif sub_opcion == 2:
			print("B - C:" ,B," - ", C)
			print(DIFF_func(B,C))
		else :
			print("A - C:" ,A," - ", C)
			print(DIFF_func(A,C))

	elif opcion == 4:
		#DIFERENCIA SIMETRICA
		print ("1. A Δ B")
		print ("2. B Δ C")
		print ("3. A Δ C")
		sub_opcion = pedirNumeroEntero()
		if sub_opcion == 1:
			print("A Δ B:" ,A," Δ ", B)
			print(DIFF_SIM_func(A,B))
		elif sub_opcion == 2:
			print("B Δ C:" ,B," Δ ", C)
			print(DIFF_SIM_func(B,C))
		else :
			print("A Δ C:" ,A," Δ ", C)
			print(DIFF_SIM_func(A,C))

	else:
		salir = True

print ("Gracias")