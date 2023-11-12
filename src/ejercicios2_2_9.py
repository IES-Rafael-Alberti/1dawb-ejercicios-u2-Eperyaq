"""
Escribir un programa que almacene la cadena de caracteres contraseña en una variable, pregunte al usuario por la contraseña hasta que introduzca la contraseña correcta.
"""

def definirContraseña():
    contra = "contraseña"
    return contra

def ponerContraseña():
    pregunta = input("Dime cual crees que es la contraseña: ")
    return pregunta

def bucleContraseña(contra, pregunta):
    while pregunta != contra:
        pregunta=input("Te equivocaste, prueba de nuevo: ")
        if pregunta == contra:
            print("Acertaste!!")
            
        
    return contra

def main():
    
    contra = definirContraseña()
    pregunta = ponerContraseña()
    bucleContraseña(contra, pregunta)
    
    

if __name__=="__main__":
    main()
#Arreglado