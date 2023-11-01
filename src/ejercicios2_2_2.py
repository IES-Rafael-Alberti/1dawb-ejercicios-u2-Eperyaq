#Escribir un programa que pregunte al usuario su edad y muestre por pantalla todos los años que ha cumplido (desde 1 hasta su edad).
def pedirEdad():
    edad = int(input("Dime tu edad: "))
    return edad

def cambioEdad(edad:int):
    while edad>=1:
        edad = edad - 1
    return edad

def main():
    pedirEdad()
    print(cambioEdad(edad))
    

if __name__=="__main__":
    main()

#¿? me dice que le falta un argumento a print(cambioEdad()) pero cuando le pongo edad dentro me dice que no esta definida