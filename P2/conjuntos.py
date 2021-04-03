
######### FUNCIONES ###########
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
	DS = list(list(set(A)-set(B)) + list(set(B)-set(A)))
	return DS
####################

######### VARIABLES ###########
salir = False
opcion = 0
sub_opcion = 0
A = []
B = []
C = []
####################

######### Instrucciones de uso ###########
print("###########################\nTEORIA DE CONJUNTOS\n###########################")
print("Intoduce hasta 3 conjuntos:\tA\tB\tC")
print("Navega por las opciones de operaciones:\t\tUNION\t\tINTERSECCION\t\tDIFERENCIA\t\tDIFERENCIA SIMETRICA")
print("###########################")

######### CONJUNTOS ###########
#obtenemos los conjuntos A, B y C
arr = input("\nConjunto A: ")   #A
if(len(arr) != 0):
	A = list(map(int,arr.split(','))) #quitamos las comas y guardamos en un arreglo

arr = input("\nConjunto B: ")   #B
if(len(arr) != 0):
	B = list(map(int,arr.split(','))) #quitamos las comas y guardamos en un arreglo

arr = input("\nConjunto C: ")   #C
if(len(arr) != 0):
	C = list(map(int,arr.split(','))) #quitamos las comas y guardamos en un arreglo

print("\n############### CONUNTOS ###############")
print("A: ",A)
print("B: ",B) 
print("C: ",C)
print("\n###########################\n")

######### MENU PRINCIPAL ###########
while not salir:

	print("\n############### OPERACIONES DISPONIBLES ###############")
	print ("1. UNION")
	print ("2. INTERSECCION")
	print ("3. DIFERENCIA")
	print ("4. DIFERENCIA SIMETRICA")
	print ("5. SALIR")

	opcion = int(input("Introduce la operacion deseada: "))

	if opcion == 1:
		#UNION
		print ("1. A U B")
		print ("2. B U C")
		print ("3. A U C")
		print ("4. A U (B U C)")
		sub_opcion = int(input("Introduce los conjuntos a operar: "))
		if sub_opcion == 1:
			print("A U B:" ,A," U ", B)
			print(UNION_func(A,B))
		elif sub_opcion == 2:
			print("B U C:" ,B," U ", C)
			print(UNION_func(B,C))
		elif sub_opcion == 3:
			print("A U C:" ,A," U ", C)
			print(UNION_func(A,C))
		else :
			#FALTA ESTA OPCIÓN TODO
			print("A U (B U C):" ,A," U ( ", B," U ",C," )")
			print(UNION_func(A,UNION_func(B,C)))

	elif opcion == 2:
		#INTERSECCION
		print ("1. A n B")
		print ("2. B n C")
		print ("3. A n C")
		print ("4. A n (B n C)")
		sub_opcion = int(input("Introduce los conjuntos a operar: "))
		if sub_opcion == 1:
			print("A n B:" ,A," n ", B)
			print(INTERSEC_func(A,B))
		elif sub_opcion == 2:
			print("B n C:" ,B," n ", C)
			print(INTERSEC_func(B,C))
		elif sub_opcion == 3:
			print("A n C:" ,A," n ", C)
			print(INTERSEC_func(A,C))
		else :
			#FALTA ESTA OPCIÓN TODO
			print("A n (B n C):" ,A," n ( ", B," n ",C," )")
			print(INTERSEC_func(A,INTERSEC_func(B,C)))

	elif opcion == 3:
		#DIFERENCIA
		print ("1. A - B")
		print ("2. A - C")
		print ("3. B - A")
		print ("4. B - C")
		print ("5. C - A")
		print ("6. C - B")
		sub_opcion = int(input("Introduce los conjuntos a operar: "))
		if sub_opcion == 1:
			print("A - B:" ,A," - ", B)
			print(DIFF_func(A,B))
		elif sub_opcion == 2:
			print("A - C:" ,A," - ", C)
			print(DIFF_func(A,C))
		if sub_opcion == 3:
			print("B - A:" ,B," - ", A)
			print(DIFF_func(B,A))
		elif sub_opcion == 4:
			print("B - C:" ,B," - ", C)
			print(DIFF_func(B,C))
		elif sub_opcion == 5:
			print("C - A:" ,C," - ", A)
			print(DIFF_func(C,A))
		else :
			print("C - B:" ,C," - ", B)
			print(DIFF_func(C,B))

	elif opcion == 4:
		#DIFERENCIA SIMETRICA
		print ("1. A Δ B")
		print ("2. A Δ C")
		print ("3. B Δ A")
		print ("4. B Δ C")
		print ("5. C Δ A")
		print ("6. C Δ B")
		sub_opcion = int(input("Introduce los conjuntos a operar: "))
		if sub_opcion == 1:
			print("A Δ B:" ,A," Δ ", B)
			print(DIFF_SIM_func(A,B))
		elif sub_opcion == 2:
			print("A Δ C:" ,A," Δ ", C)
			print(DIFF_SIM_func(A,C))
		if sub_opcion == 1:
			print("B Δ A:" ,B," Δ ", A)
			print(DIFF_SIM_func(B,A))
		elif sub_opcion == 2:
			print("B Δ C:" ,B," Δ ", C)
			print(DIFF_SIM_func(B,C))
		elif sub_opcion == 2:
			print("C Δ A:" ,C," Δ ", A)
			print(DIFF_SIM_func(C,A))
		else :
			print("C Δ B:" ,C," Δ ", B)
			print(DIFF_SIM_func(C,B))

	else:
		salir = True

print ("Gracias")


######### INFO ADICIONAL ###########
# https://www.w3schools.com/python/python_sets.asp
# https://www.geeksforgeeks.org/python-union-two-lists/
# https://www.geeksforgeeks.org/python-difference-two-lists/
# https://www.geeksforgeeks.org/python-intersection-two-lists/
