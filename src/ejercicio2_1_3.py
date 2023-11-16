"""
Escribir un programa que pida al usuario dos números y muestre por pantalla su división. Si el divisor es cero el programa debe mostrar un error.
"""
def pedirNumeros():
    n1 = int(input("Dame un numero: "))
    return(n1)

def division (n1 : int, n2 : int):
    
    if n2 == 0:
        return"ERROR no puedes dividir entre cero."
    else:
        resultado = n1/n2
        return resultado


def main():
  numero1 = pedirNumeros()
  numero2 = pedirNumeros()
  
  print(division(numero1, numero2))
  



if __name__=="__main__":
    main()      
