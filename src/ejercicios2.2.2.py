def pedirEdad():
    edad = int(input("Dime tu edad: "))
    return edad

def cambioEdad(edad:int):
    while edad>=5:
        edad = edad - 1
    return edad

def main():
    edad = pedirEdad()
    print(cambioEdad(edad))
    

if __name__=="__main__":
    main()

#¿?