#Escribir un programa que almacene la cadena de caracteres contraseña en una variable,
# pregunte al usuario por la contraseña e imprima por pantalla si la contraseña introducida 
# por el usuario coincide con la guardada en la variable sin tener en cuenta mayúsculas y
# minúsculas.
def pregunta():
    contra=input("Dime cual crees que es la contraseña: ")
    return (contra)


def cuestion(contra):
    contraseña="contraseña"
    if contra() == contraseña:
        print("coincide!")
    else:
        print("no coincide.")
    return (contra)
        
print(cuestion(contra))
#sigo sin entender porque pone el none
#no entiendo como separar en varias funciones