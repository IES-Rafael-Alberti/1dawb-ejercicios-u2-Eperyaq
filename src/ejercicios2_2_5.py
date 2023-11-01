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
    return invertir

#se podria poner float en años? 1.5 años pero 1.7 años no tiene logica


def main():
  print(calculoInversion())
    
    

if __name__=="__main__":
    main()
    #missing 3 required positional arguments