def pedirEdad():
    edad = int(input("Dime la edad: "))
    return (edad)

def edad(edad):
    if edad>18:
        return True
    else:
        return False
    

def main():
  edad = pedirEdad()

if edad(edad) == True:
    print("Eres mayor de edad")
else:
    print("Eres menor :(")

  

if __name__=="__main__":
    main()