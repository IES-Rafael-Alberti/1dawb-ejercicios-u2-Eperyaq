# Escribir un programa para una empresa que tiene salas de juegos para todas las edades y quiere calcular de forma automática el precio que debe cobrar a sus clientes por entrar. El programa debe preguntar al usuario la edad del cliente y mostrar el precio de la entrada. Si el cliente es menor de 4 años puede entrar gratis, si tiene entre 4 y 18 años debe pagar 5€ y si es mayor de 18 años, 10€.

def precios(edad : int):

    if edad < 4:
        return "Puedes entrar gratis!"
    elif edad >= 4 and edad < 18:
        return "Debes pagar 5€"
    else:
        return "Tienes que pagar 10€"
    
    
    
def main():
    edad = int(input("Dime tu edad: "))

    print(precios(edad))


if __name__=="__main__":
    main()
    
#va guay
