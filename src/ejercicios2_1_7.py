def preguntarRenta():
    renta = input("Dime cuanto es tu renta anual: ")
    return renta

def porcentaje(renta : str):

    if renta<10000:
        return "5%"
    elif renta>10000 and renta<20000:
        return "15%"
    elif renta>20000 and renta<35000:
        return "20%"
    elif renta>35000 and renta<60000:
        return "30%"
    else:
        return "45%"


def main():
    
    renta = preguntarRenta()
    
    print(f"Te corresponde un {porcentaje(renta)}")



if __name__=="__main__":
    main()

# TypeError: '<' not supported between instances of 'str' and 'int'