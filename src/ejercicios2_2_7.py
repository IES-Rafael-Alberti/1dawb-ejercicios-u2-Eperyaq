"""
Escribir un programa que muestre por pantalla la tabla de multiplicar del 1 al 10.
"""
def preguntarTabla():
    numero_tabla = int(input("Que tabla quieres que haga?: "))
    return numero_tabla

numero_multiplicar = int(input("nº: "))
for i in range (1,11):
    resultado = i * numero_multiplicar

print(numero_multiplicar, i, resultado)