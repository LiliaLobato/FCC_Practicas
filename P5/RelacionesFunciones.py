
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
print("\n##############################\n")

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
		print("Los nodos: ",transicion_1, " EXISTE")
		#print(transicion_1)


if (isReflexivo) >= num_nodos:
	print("############ ES REFLEXIVO ###############\n")
else :
	print("########### NO ES REFLEXIVO ##############\n")


########## REVISAR SI ES SIMETRICO
isSimetrico = 1
for i in range(transiciones):
	transicion_1 = (Relacion[i])
	node1_0 = transicion_1[0]
	node1_1 = transicion_1[1]
	if (str(node1_1), str(node1_0)) in Relacion:
		print("Los nodos:",transicion_1, "tiene inverso")
	else:
		print("Los nodos:",transicion_1, "NO tiene inverso")
		isSimetrico = 0

if isSimetrico == 1:
	print("############ ES SIMETRICO ###############\n")
else:
	print("########### NO ES SIMETRICO ##############\n")
	

########## REVISAR SI ES TRANSITIVO

isTransitivo = 1

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
			if (str(node1_x), str(node1_z)) in Relacion:
				print("Los nodos: x=",node1_x, " y=",node_y, " z=", node1_z, "son transitivos")
				#isTransitivo = 1
			else:
				isTransitivo = 0
				print("Los nodos: x=",node1_x, " y=",node_y, " z=", node1_z, "NO EXISTE")
					
if isTransitivo:
	print("############ ES TRANSITIVO ###############\n")
else:
	print("########### NO ES TRANSITIVO ##############\n")
	

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
for i in range (0, len(Relacion)-1):
    for j in range (0, len(Relacion)-1):
        if (i != j) and (Relacion[i] == Relacion[j]):
            isFuncion = True
        else:
            for k in range (0, len(Relacion)):
                if (k != i):
                    if len(Relacion[i]) == 1 or len(Relacion[k]) == 1:
                         isFuncion = False
                    elif (Relacion[i][0] == Relacion[k][0]) and (Relacion[i][1] == Relacion[k][1]):
                        isFuncion = True
                    elif Relacion[i][0] == Relacion[k][0]:
                        isFuncion = False

if isFuncion == True:
	print("############ ES FUNCIÓN ###############\n")
else:
	print("########### NO ES FUNCIÓN ##############\n")