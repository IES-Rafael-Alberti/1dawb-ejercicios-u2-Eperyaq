#En una determinada empresa, sus empleados son evaluados al final de cada año. Los puntos que pueden obtener en la evaluación comienzan en 0.0 y pueden ir aumentando, traduciéndose en mejores beneficios. Los puntos que pueden conseguir los empleados pueden ser 0.0, 0.4, 0.6 o más, pero no valores intermedios entre las cifras mencionadas. A continuación se muestra una tabla con los niveles correspondientes a cada puntuación. La cantidad de dinero conseguida en cada nivel es de 2.400€ multiplicada por la puntuación del nivel.

def comprobarNivel(points):
    if points == 0.0 or points == 0.4 or points >= 0.6:
        return True
    else:
        return False


def pruebaNivel(points):
    if points == 0.0:
        return "Inaceptable"
    elif points == 0.4:
        return "Aceptable"
    else:
        return "Meritorio"





def main():
   
   puntos = float(input("Dime tu nivel, 0.0, 0.4, 0.6 o más "))
   
   if comprobarNivel(puntos) == True:
           print (pruebaNivel(puntos) , (2400 * puntos))
   else:
        print("**ERROR**")

if __name__=="__main__":
    main()

#funciona