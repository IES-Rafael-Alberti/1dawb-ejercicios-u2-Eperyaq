"""
Escribir un programa que almacene la cadena de caracteres contraseña en una variable, pregunte al usuario por la contraseña e imprima por pantalla si la contraseña introducida por el usuario coincide con la guardada en la variable sin tener en cuenta mayúsculas y minúsculas.
"""
def testPassword(passw):
    passOrig = "contraseña"
    if passw.replace(" ", "").lower() == passOrig:
        return True
    else:
        return False

def getPassword():
    """
    
    """
    return input("Introduzca la contraseña: ")

def main():
    password =  getPassword
    if testPassword(password):
        print ("Has acertado la contraseña! ")
    else:
        print("Siga jugando")
    print()


if __name__ == "__main__":
    main()

#AttributeError: 'function' object has no attribute 'replace'