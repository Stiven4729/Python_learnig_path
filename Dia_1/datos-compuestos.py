# una lista se puede modificar sus valores
lista = ["Stiven", "Oscar", 20, True, "Javier", 1.71]

#la tupla es una lista donde no se pueden modificar sus valores
tupla = ("Stiven", "Oscar", 20, True, "Javier", 1.71)


#Esto es correcto
lista[2] = "Juan"

#esto es erroneo
#tupla[2] = "Juan"

#Conjunto este no almacena datos iguales y no se puede llamar a los elementos por su indice o posicion
conjunto = {"Stiven", "Oscar", 20, True, "Javier", 1.71}
#print(conjunto[3]) -> no se peude acceder al elemento

#diccionario (dict)
diccionario = {
    'nombre' : "Stiven",
    'apellido' : "Gallego",
    'estatura' : 1.71,
    'edad' : 20
}

print(diccionario)