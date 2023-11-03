"""
Escribir un programa que almacene la cadena de caracteres contraseña en una variable, pregunte al usuario por la contraseña hasta que introduzca la contraseña correcta.
"""
def ponerContraseña():
    contra = "contraseña"
    pregunta = input("Dime cual crees que es la contraseña: ")
    return pregunta, contra

def bucleContraseña(contra, pregunta):
    while pregunta != contra:
        if pregunta != contra:
            pregunta=input("Te equivocaste, prueba de nuevo: ")
        return "Acertaste!!"

def main():
  print(bucleContraseña(pregunta , ponerContraseña()))
    
    

if __name__=="__main__":
    main()
#pregunta is not defined 