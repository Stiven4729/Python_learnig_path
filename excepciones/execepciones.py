#creando funcion con manejo de except
def sumar():
    #creando un bucle
    while True:
        #pidiendo 2 numeros
        a = input("Digita un numero ")
        b = input("Digita otro numero ")
        #intentando realizar la suma
        try:
            resultado = int(a) + int(b)
        #si no realiza la suma imprimir informacion. llamamos el padre Exception y lo renombramos
        #except Exception as r:
        #    print("Te pedi un numero")
            #capturando el error de la excepcion
        #    print(f"Error: {r}")
            #capturando el nombre del error para darle manejo
        #    print(f"Error: {type(r).__name__}")
        except ValueError as e:
            print("Se ejecuta cuando el error es un ValueError para actuar de forma distinta")
            print(f"Este es el error: {e}")
        #rompiendo el ciclo cuando se realice la suma
        else:
            break
    return resultado

print(sumar())
