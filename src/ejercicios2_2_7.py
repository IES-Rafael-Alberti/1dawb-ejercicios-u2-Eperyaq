"""
Escribir un programa que muestre por pantalla la tabla de multiplicar del 1 al 10.
"""
def preguntarTabla():
    numero_tabla = int(input("Que tabla quieres que haga?: "))
    
    return numero_tabla

def crearTabla(numero_tabla):
    
    for i in range(1,11):
        resultado = i * numero_tabla
        print(f" {numero_tabla} x {i} = {resultado}")
       
        
    return resultado

def main():
    numero_tabla = preguntarTabla()
    crearTabla(numero_tabla)
    
    
    

if __name__=="__main__":
    main()