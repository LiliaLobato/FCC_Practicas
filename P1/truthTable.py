
import re, string

######### FUNCIONES ###########
def check_conditional(exp):
	if "=>" in exp:
		init= exp[exp.index("=")-1]
		final= exp[exp.index(">")+1]
		return "(~"+init+"|"+final+")"
	else:
		return exp

def space_print(exp, num):
	exp_sub = ""
	for i in range(num//2):
		exp_sub = exp_sub + " "
	exp_sub = exp_sub + exp
	for i in range(num//2):
		exp_sub = exp_sub + " "
	return exp_sub
####################

######### VARIABLES ###########
variables_list 	= []
table 			= []
table_row 		= []
par_count 		= 0
space 			= 0
####################


######### MAIN ###########

## Decidimos cuales son validas y las acomodamos en la tabla
suporter_var = ['p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

## Instrucciones de uso
print("###########################\nGENERADOR DE TABLAS DE VERDAD\n###########################")
print("Para representar:\n\t\t\t\tAND usa &\n\t\t\t\tOR usa |\n\t\t\t\tNOT usa ~")
print("\t\t\t\tCONDICIONAL usa =>\n\t\t\t\tBICONDICIONAL usa <=>")
print("Soporta las proposiciones: ", *suporter_var)
print("###########################")

## Obtenemos el enunciado a evaluar
input_exp = input("Enunciados de logica proposicional: ")
logic_exp = input_exp.lower()
logic_exp = logic_exp.replace(' ', '')

print("\n############### TABLA DE VERDAD ###############")
print(f'Enunciado: {logic_exp}\n')


#identificamos proposiciones usadas
name_regex = re.compile(r"[p-z]")
for i in range (len(suporter_var)):
	if suporter_var[i] in logic_exp:
		variables_list = variables_list + list(suporter_var[i])

# Extraemos todas las substrings de la expresión lógica
res = re.findall(r'\(.*?\)', logic_exp)

i = 0
for exp in res:
	#revisamos si la expresión contiene sub expresiones
	for letter in str(exp):
		if letter=="(":
			par_count+=1
	#si contiene subexpresiones
	if par_count > 1 : 
		res_i = res[i]
		res[i] = res_i[1:]
		#las detectamos y ponemos como una expresion nueva
		sub_res = re.findall(r'\(.*?\)', res[i]) 
		res = res + list(sub_res)
	i+=1
	par_count = 0
res.append(str(logic_exp))
imp_res=res[:]

##replace => y <=> 
##Si es una bicondicional
i = 0
for exp in res:
	if "<=>" in exp:
		#encontramos las proposiciones
		init= exp[exp.index("<=>")-1]
		final= exp[exp.index("<=>")+3]
		#si son proposiciones compuestas, las identificamos
		if init==")" :
			exp_sub = exp[:exp.index("<")]
			exp_sub = exp_sub[exp_sub.index("("):exp_sub.index(")")+1]
			init = check_conditional(exp_sub)
		if final=="(" :
			exp_sub = exp[exp.index("<=>")+3:]
			exp_sub = exp_sub[exp_sub.index("("):exp_sub.index(")")+1]
			final = check_conditional(exp_sub)
		#rearmamos la expresión en términos de AND, OR, NOT
		new_exp = "(~"+init+"|"+final+")&(~"+final+"|"+init+")"
		res[i] = new_exp
	i+=1

##Si es una Condicional
i = 0
for exp in res:
	res[i] = check_conditional(exp)
	i+=1

##Creamos la tabla de verdad
number_rows = 2 ** len(variables_list) 
for i in range(number_rows):
	##Llenamos la tabla de verdad
	current_bin = bin(i)[2:].zfill(len(variables_list))
	for letter in str(current_bin):
		table_row = table_row + list(letter)
	table.append(table_row)

	val_eval = table[i]
	j = 0

	##Para cada expresion lógica, evaluamos
	for sub_exp in res:
		logic_exp = str(sub_exp)
		## remplazamos cada variable por el valor de la columna
		for var in variables_list:
			logic_exp = logic_exp.replace(str(var), str(val_eval[j]))
			j += 1
		j=0

		##Generamos el cambio hacia expresiones que python entiende
		logic_exp = logic_exp.replace("&", " and ")
		logic_exp = logic_exp.replace("|", " or " )  
		logic_exp = logic_exp.replace("~", " not " )
		##Se evalua esta expresión
		result = str(eval(logic_exp))
		result = "1" if (result=="True" or result == "1") else "0"
		##Agregamos a nuestra tabla de verdad
		table[i] = table[i] + (list(result))
		logic_exp = sub_exp
		table_row = []


####IMPRIMIMOS TABLA DE VERDAD
##imprimimos las expresiones
variables_list = variables_list + (imp_res)
print(*variables_list, sep = "\t")
#imprimimos la tabla y las evaluaciones
for row in table:
	tt=""
	i=0
	for item in row:
		space = len(str(variables_list[i]))
		tt=tt+space_print(item, space)+"\t"
		i+=1
	print(tt)