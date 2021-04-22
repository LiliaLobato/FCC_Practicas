print("PROYECTO INTEGRAL FCC")
print("TOOL KIT FCC")
print("Sucesiones\n")

formula = input("Fórmula(k): ")
m = int(input("Limite inferior: ")) #limite inferior
n = int(input("Limite superior: ")) #limite superior
print("")

suma = 0
mult = 1

print("Desarrollo de la sucesión de m a n:")

for i in range(m, n+1):
    k = i
    print("k:", i, " = ", round(eval(formula), 3), sep='')
    suma += eval(formula)
    mult *= eval(formula)

print("\nSUMATORIA:", suma)
print("MULTIPLICACIÓN:", mult)
