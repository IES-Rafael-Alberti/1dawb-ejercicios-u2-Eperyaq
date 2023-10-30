def preguntarRenta():
    renta = input("Dime cuanto es tu renta anual: ")
    return renta

def renta1(renta):
    if renta<10000:
        return True
    else:
        if renta>10000 and renta<20000:
            return False

def renta2():
    if renta>20000 and renta<35000:
        Return
    else:
        if renta>35000 and renta<60000:
            print("Te corresponde un 30% de impositivo.")
    

# he definido varias funciones para que dependiendo del porcentaje se meta en una funcion u otra, pero despues en el main tendre que hacer varios if dependiendo del dinero para que entre en una funcion u otra pero entonces no tendria sentido tener varias funciones

""""
def renta ():
    if renta<10000:
        print("Te corresponde un 5% de impositivo.")
    elif renta>10000 and renta<20000:
        print("Te corresponde un 15% de impositivo.")
    elif renta>20000 and renta<35000:
        print("Te corresponde un 20% de impositivo.")
    elif renta>35000 and renta<60000:
        print("Te corresponde un 30% de impositivo.")
    elif renta>60000:
        print("Te corresponde un 45% de impositivo.")
"""


def main():
    print()


if __name__=="__main__":
    main()
