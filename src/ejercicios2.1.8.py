def nivel():
    if nivel==0.0:
        print("te corresponde ", 2400*0.0, "€")
    elif nivel==0.4:
        print("te corresponde ", 2400 * 0.4, "€")
    elif nivel==0.6:
        print("te corresponde ", 2400 * 0.6, "€")
    elif nivel> 0.6:
        print("te corresponde ", 2400 * nivel, "€")
    

#nivel = float(input("Que nivel tienes 0.0, 0.4, 0.6 o más? "))
#lo mismo que el anterior que hago dos funciones if y que devuelva dos true false?
def main():
    print()


if __name__=="__main__":
    main()