"""
Escribir un programa que pida al usuario una palabra y luego muestre por pantalla una a una las letras de la palabra introducida empezando por la última.
"""
def pedirPalabra():
    palabra  =  input("Dime una palabra: ")
    print(palabra[::-1])
    
    return palabra

def main():
  
  pedirPalabra()
  
    
    

if __name__=="__main__":
    main()