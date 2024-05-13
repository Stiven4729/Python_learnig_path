diccionario = {
    "nombre" : "Stiven",
    "apellido" : "Gallego",
    "subs" : 20
}

#nos devuelve un objeto dict_item
claves = diccionario.keys()

#obtiene un elemento con get(). (si no esta el programa continua)
valor = diccionario.get("apellido")

#eliminando un elemento del diccionario
diccionario.pop('nombre')

#elimina todo el diccionario 
diccionario.clear()

#obteniendo un elemento dict_items iterables
diccionario_iterables = diccionario.items()


