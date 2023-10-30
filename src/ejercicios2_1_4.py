def pregunta():
    n1 = int(input("Dime un numero: "))
    return (n1)

def par(num1 : int):
    if num1%2==1:
        return True
    else:
        return False




def main():
  numero = pregunta()
  
  if par(numero)==True:
    print("Es impar")
  else:
    print("Es PAR!!")



if __name__=="__main__":
    main()