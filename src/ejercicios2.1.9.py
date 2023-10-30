def pedirEdad():
    edad=int(input("Dime tu edad: "))

def precio():
    if edad<4:
        print("Puedes entrar gratis!")
    elif edad>=4 and edad<18:
        print("Debes pagar 5€")
    elif edad>=18:
        print("Tienes que pagar 10€")
    
    
    
def main():
    print()


if __name__=="__main__":
    main()