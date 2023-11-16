"""
Escribir un programa que pregunte al usuario una cantidad a invertir, el interés anual y el número de años, y muestre por pantalla el capital obtenido en la inversión cada año que dura la inversión.
"""
def cantidadInvertir():
    invertir = int(input("Dime la cantidad a invertir: "))
    return invertir
    
def tipoInteres():
    interes = float(input("Dime el interes anual: "))
    return interes

def añosInteres():
    años = int(input("Dime los años: "))
    return años

def calculoInversion(interes : int, años : int , invertir : int):
    
    invertir *= 1+ interes/100
    invertir= invertir*años
    resultado = invertir
    
    return resultado



def main():
  invertir = cantidadInvertir()
  interes = tipoInteres()
  años = añosInteres()
  print(calculoInversion(invertir, interes, años))
    
    

if __name__=="__main__":
    main()