lista = ['hola', 'chao' , 2, 4, True]

#sirve para agregar un elemento a la lista
lista.append('Tardes')

#agregar un elemento a la lista en un indice especifico 
lista.insert(2, "buenas")

#agregar varios elementos a  la lista
lista.extend([False, 69])

#eliminando un elemento de la lista. -1 para eliminar el ultimo, -2 para eliminar el penultimo y asi sucesivamente 
lista.pop(0)

#elimina un elemento de la lista por su valor
lista.remove("buenas")

#ordena la lista de forma ascendente (si usamos el parametro reverse=True lo ordena en reversa) 
lista.sort()

#invirtiendo los elementos de una lista (no la ordena)
lista.reverse()


#elimina todos los elementos de la lista
lista.clear()

