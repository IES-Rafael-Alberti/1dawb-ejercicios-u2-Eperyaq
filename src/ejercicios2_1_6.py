def pedirNombre():
    """
    Solicita un nombre por consolona.

    retorna
    ---------------
    str una cadena de caracteres con el nombre introducido
    """
    return input("Introduce tu nombre: ")

def pedirSexo():
    """
    Solicita un genero por consolona.

    retorna
    ---------------
    str un caractere con el tipo de sexo (M/F)

    """
    sexo = ""
    while sexo != "M" and sexo != "F":
        sexo = input("Introduce tu sexo (M/F): ").upper()

    return sexo

def asignarGrupo(sexo,nombre): 
    """
    Asigna el grupo del curso segun su nombre y sexo.

    parametros
    ---------------
    str
        el nombre del alumno
    str     
        sexo de un alumno

    retorna
    ---------------
    str 
        un caractere con el tipo de sexo (M/F)

    """
    #inicial nombre [0:1]  te mira la primera letra del nombre y la pone en mayusculas
    inicialNombre = nombre[0:1].upper()
    grupo=""
    if (sexo=="M" and inicialNombre >"N") or (sexo=="F" and inicialNombre >"M"):
        grupo = "A"
    else:
        grupo= "B"
    return (grupo)



def main():
    nombre = pedirNombre()

    sexo = pedirSexo()
    
    print(f"Estas en el grupo {asignarGrupo(nombre, sexo)}")

if __name__=="__main__":
    main()
#siempre da el grupo B