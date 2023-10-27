def pregunta():
    n1 = int(input("Dime un numero: "))
    return (n1)

def par(n1 : int):
    if n1%2==1:
        print("Es impar")
    else:
        print("Es par")
    return(n1)


print(par())
#otro mas que sale none
#par() missing 1 required positional argument: 'n1'