def pedirNombre():
    nombre = input("Dime tu nombre: ")
    return nombre

def repeticion(nombre):
    return nombre*10



def main():
    nombre = pedirNombre()
    print(repeticion(nombre))

if __name__=="__main__":
    main()

#funciona