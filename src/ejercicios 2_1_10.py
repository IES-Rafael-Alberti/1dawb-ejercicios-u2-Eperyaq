def respuesta():
    veg= input("Quieres la pizza de tipo vegetariano? si/no ")
    return (veg)

def choice():
    ing = input("ingredientes: tomate, mozarella y debes escoger si quieres pimiento o tofu. ")
    return(ing)

def carnivoro():
    ing = input("ingredientes: tomate, mozarella y debes escoger si quieres peperoni, jamon, salmon. ")
    return(ing)




vegetariano = (respuesta())
if vegetariano=="si":
    ingrediente = (choice())
    if ingrediente=="pimiento":
        print("Tu pizza va a llevar tomate, mozarella y pimiento")
    else:
        print("Tu pizza va a llevar tomate, mozarella y tofu")
elif vegetariano=="no":
        ingrediente = (carnivoro())
        if ingrediente=="peperoni":
            print("Tu pizza va a llevar tomate, mozarella y peperoni.")
        elif ingrediente=="jamon":
            print("Tu pizza va a llevar tomate, mozarella y jamon.")
        else: 
            print("Tu pizza va a llevar tomate, mozarella y salmon.")
#Funciona