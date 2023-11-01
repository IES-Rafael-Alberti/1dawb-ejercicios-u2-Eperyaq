#Escribir un programa que pida al usuario un número entero positivo y muestre por pantalla la cuenta atrás desde ese número hasta cero separados por comas.
def pedirNumero():
    numero = int(input("Dime un numero: "))
    return numero


def serie(num:int):
    while num>=0:
        print(num, end=",")
        num = num - 1
    return num


def main():
    print(pedirNumero())
    
    print(serie())
    
    
    

if __name__=="__main__":
    main()