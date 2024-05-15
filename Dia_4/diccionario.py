#creando diccionario con dict()
diccionario = dict(nombre = "Stiven", apellido = "Gallego")

#las listas no pueden ser claves y usamos fronzenser para meter conjuntos
diccionario = {frozenset(["Lopez", "lindo"]), "jajajaj"}

#creando diccionarios con fromKeys() con dos parametros
diccionario = dict.fromkeys(['nombre', 'apellido'])

#creando diccionarios con fromKeys() cambiando el valor por defecto a "no se"
diccionario = dict.fromkeys(['nombre', 'apellido'], "No se")

print(diccionario)
