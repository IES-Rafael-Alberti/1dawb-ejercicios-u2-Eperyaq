"""
Escribir un programa que pida al usuario un número entero positivo y muestre por pantalla todos los números impares desde 1 hasta ese número separados por comas.
"""
def pedirNumero():
    numero = int(input("Dime un numero y te dire los impares: "))
    
    return numero

def seriesita(numero):
    while numero>=1:
        if numero%2==1:
            numero -= 1
        else: 
            numero -= 2
    print(numero)
    return numero
    
def main():
    num= pedirNumero()
    seriesita(num) 
    

if __name__=="__main__":
    main()
#...