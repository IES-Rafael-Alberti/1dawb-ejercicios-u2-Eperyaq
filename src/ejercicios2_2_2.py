#Escribir un programa que pregunte al usuario su edad y muestre por pantalla todos los años que ha cumplido (desde 1 hasta su edad).
def pedirEdad():
    edad = int(input("Dime tu edad: "))
    return edad

def cambioEdad(edad:int):
    while edad>=1:
        print(edad)
        edad = edad - 1
    
    return edad

def main():
    edad = pedirEdad()
    cambioEdad(edad)
    

if __name__=="__main__":
    main()

