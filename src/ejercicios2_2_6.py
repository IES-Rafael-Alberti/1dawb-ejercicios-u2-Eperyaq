"""
Escribir un programa que pida al usuario un número entero y muestre por pantalla un triángulo rectángulo como el de más abajo, de altura el número introducido.
"""
def preguntaAltura():
    altura = int(input("Dime la altura del triangulo: "))
    return altura


def formadoPiramide(altura):
    for numero_linea in range (altura):
        espacios = altura - numero_linea -1
        asteriscos = 1 + numero_linea *2
    return " "* espacios + "*" * asteriscos

def main():
    alturas = preguntaAltura()
    print(formadoPiramide(altura))
    
    

if __name__=="__main__":
    main()

#altura is not defined