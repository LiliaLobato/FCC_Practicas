
######### VARIABLES ###########
Nodos = []
Relacion = []
####################

######### RELACION ###########
#obtenemos las variables
arr = input("\nNodos: ")   #Nodos
if(len(arr) != 0):
	Nodos = list(map(str,arr.split(','))) #quitamos las comas y guardamos en un arreglo

Relacion_raw = "not done"
while Relacion_raw != ["done"] :
	Relacion_raw = input("\nRelacion: ")   #Relacion
	if(len(Relacion_raw) != 0):
		Relacion_raw = list(map(str,Relacion_raw.split(','))) #quitamos las comas y guardamos en un arreglo
		print(Relacion_raw)
		Relacion.append(tuple(Relacion_raw))
Relacion.pop(len(Relacion)-1)

print("\n############### RELACION ###############")
print("NODOS: ",Nodos)
print("RELACION: ",Relacion)

num_nodos = len(Nodos)
transiciones = len(Relacion)

####################

########## REVISAR SI ES REFLEXIVO
isReflexivo = 0
for i in range(transiciones):
	transicion_1 = (Relacion[i])
	node1_0 = transicion_1[0]
	node1_1 = transicion_1[1]
	if (node1_0 == node1_1): #validamos que sea un loop
		isReflexivo=isReflexivo+1
		#print(transicion_1)


if (isReflexivo) >= num_nodos:
	print("############ ES REFLEXIVO ###############")
else :
	print("########### NO ES REFLEXIVO ##############")


########## REVISAR SI ES SIMETRICO
isSimetrico = 0
for i in range(transiciones):
	transicion_1 = (Relacion[i])
	node1_0 = transicion_1[0]
	node1_1 = transicion_1[1]
	for j in range(transiciones):
		transicion_2 = (Relacion[j])
		node2_0 = transicion_2[0]
		node2_1 = transicion_2[1]
		if (node1_0 != node1_1): #validamos que no sea un loop
			if (node1_0 != node2_0) and (node1_1 != node2_1): #valida que no sea el mismo
				if (node1_0 == node2_1) and (node1_1 == node2_0): #valida que sea inverso
					isSimetrico=isSimetrico+1
					print(transicion_1,transicion_2)
		#else:
			#isSimetrico=isSimetrico+1
			#print(transicion_1,transicion_2)

if isSimetrico%num_nodos == 0 and isSimetrico != 0:
	print("############ ES SIMETRICO ###############")
else:
	print("########### NO ES SIMETRICO ##############")
	

########## REVISAR SI ES TRANSITIVO

isTransitivo = 0

for i in range(transiciones):
	transicion_1 = (Relacion[i])
	#obtenemos x,y
	node1_x = transicion_1[0]
	node1_y = transicion_1[1]
	for j in range(transiciones):
		transicion_2 = (Relacion[j])
		#obtenemos y,z
		node2_y = transicion_2[0]
		node1_z = transicion_2[1]

		if(node1_y == node2_y): #validamos que ambas Y sean las mismas
			node_y = node2_y

			for k in range(transiciones):
				transicion_3 = (Relacion[k])
				#obtnemos x,z
				node2_x = transicion_3[0]
				node2_z = transicion_3[1]
				if(node1_x == node2_x) and (node1_z == node2_z): #Validamos que X y Z sean los mismos
					node_x = node2_x
					node_z = node2_z
					if (str(node_x), str(node_z)) in Relacion:
						print("Los nodos: x=",node_x, " y=",node_y, " z=", node_z, "son transitivos")
						isTransitivo = isTransitivo +1
					else:
						isTransitivo = 0
						print("Los nodos: x=",node_x, " y=",node_y, " z=", node_z, "NO EXISTE")
					#print(node2_x,node1_x)
					#print(node2_y,node1_y)
					#print(node2_z,node1_z)


					
if isTransitivo == transiciones:
	print("############ ES TRANSITIVO ###############")
else:
	print("########### NO ES TRANSITIVO ##############")
	

########## CALCULAR DOMINIO
dominio=[]
for i in range(transiciones):
	dominio.append(Relacion[i][0])

dominio = list(set(dominio))
dominio.sort()
print ("DOMINIO: ", dominio)

########## CALCULAR CODOMINIO
codominio=[]
for i in range(transiciones):
	codominio.append(Relacion[i][1])

codominio = list(set(codominio))
codominio.sort()
print ("CODOMINIO: ", codominio)


########## ES FUNCIÓN?
isFuncion = True;
for i in range (transiciones-1):
	for j in range (0, len(Relacion)-1):
		if (i != j) and (Relacion[i] == Relacion[j]):
			isFuncion = True
		else:
			if len(Relacion[i]) == 1 or len(Relacion[i+1]) == 1:
				isFuncion = False
			if Relacion[i][0] == Relacion[i+1][0]:
				isFuncion = False

if isFuncion == True:
	print("############ ES FUNCIÓN ###############")
else:
	print("########### NO ES FUNCIÓN ##############")