"""
Escribir un programa que pida al usuario un número entero positivo y muestre por pantalla todos los números impares desde 1 hasta ese número separados por comas.
"""
def pedirNumero():
    numero = int(input("Dime un numero y te dire los impares: "))
    return numero

def seriesita(numero):
    while numero>=1:
        if numero%2==1:
            return numero
        numero = numero - 1
        
    return numero
    
def main():
    num= pedirNumero()
    serie = seriesita(num) 
    

if __name__=="__main__":
    main()
#UnboundLocalError: cannot access local variable 'serie' where it is not associated with a value