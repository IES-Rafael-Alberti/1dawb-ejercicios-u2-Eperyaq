def numeros():
    n1 = int(input("Dame un numero: "))
    n2 = int(input("Dame otro numero: "))
    return(n1,n2)

def division (n1,n2):
    if n2==0:
        print("ERROR no puedes dividir entre cero.")
    return n1/n2
print(division())

""""
n1 = int(input("Dame un numero: "))
n2 = int(input("Dame otro numero: "))
llamo a la funcion numeros dentro de division 
"""
        