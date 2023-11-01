def pedirNumeros():
    n1 = int(input("Dame un numero: "))
    n2 = int(input("Dame otro numero: "))
    return(n1,n2)

def division (n1 : int, n2 : int):
    if n2==0:
        print("ERROR no puedes dividir entre cero.")
    return n1/n2


def main():
  print(pedirNumeros())
  
  print(division(n1, n2))
  



if __name__=="__main__":
    main()      