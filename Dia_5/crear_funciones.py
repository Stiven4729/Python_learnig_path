#def saludar():
#    print("hola stiven")
    
#saludar()


#crear una cuncion con parametros
def saludar(nombre, sexo):
    sexo = sexo.lower()
    if (sexo == "hombre"):
        print(f"Hola {nombre}. como estas Señor?")
    elif (sexo == "mujer"):
        print(f"Hola {nombre}. como estas señorita?")
    else:
        print(f"Hola {nombre}. como estas pokemon?")
saludar("Stiven", "Hombre")
saludar("Sofia", "mujeR")
saludar("Daniel", "none")

#utilizando la funcion args (*args)
def suma (nombre, *numeros):
    return f"{nombre} tu suma es: {sum(numeros)}"


resultado = suma("Stiven", 2,3,4,5,6,8,86,534,2)
print(resultado)
