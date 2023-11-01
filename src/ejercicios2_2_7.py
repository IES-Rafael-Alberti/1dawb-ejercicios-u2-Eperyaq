def preguntarTabla():
    numero_tabla = int(input("Que tabla quieres que haga?: "))
    return numero_tabla

numero_multiplicar = int(input("nº: "))
for i in range (0,11):
    resultado = i * numero_multiplicar

print(numero_multiplicar, i, resultado)