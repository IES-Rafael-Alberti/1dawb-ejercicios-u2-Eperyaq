def pedirEdad():
    edad = input("Dime tu edad: ")
    return edad

def pedirDinero():
    dinero=float(input("Dime tu dinero: "))
    return dinero

def tributar (edad: int, dinero:float):
    if edad < 16 or dinero < 1000:
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
    
#TypeError: '<' not supported between instances of 'str' and 'int'