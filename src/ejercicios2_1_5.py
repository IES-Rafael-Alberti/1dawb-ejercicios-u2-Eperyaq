"""
Para tributar un determinado impuesto se debe ser mayor de 16 años y tener unos ingresos iguales o superiores a 1000 € mensuales. Escribir un programa que pregunte al usuario su edad y sus ingresos mensuales y muestre por pantalla si el usuario tiene que tributar o no.
"""
def pedirEdad():
    edad = input("Dime tu edad: ")
    return edad

def pedirDinero():
    dinero=float(input("Dime tu dinero: "))
    return dinero

def tributar (edad: int, dinero:float):
    if edad < "16" or dinero < 1000:
        return True
    else:
        return False
    




def main():
    edad = pedirEdad()
    
    dinero = pedirDinero()
    
    if tributar(edad, dinero)==True:
        print("No debes tributar todavia")
    else:
        print("Ya puedes tributar!")


if __name__=="__main__":
    main()
    
#FUNCIONA!