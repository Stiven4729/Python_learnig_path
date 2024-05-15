animales = ['perros', 'gatos', 'cocodrilo', 'pajaro']
numeros = [1,2,3,4]

for animal in animales:
    print(animal)

#se intera dos listas en un mismo for usando el zip. tener encuenta que tienen que tener el mismo tamño
for numero,animal in zip(numeros,animales):
    print(f"estos son los numeros multiplicados por dos {numero * 2}")
    print(f"estos son los animales que hay en la lista {animal}")

#interar con el range para especificar un rango
for num in range(5):
    print(num)

for num in enumerate(numeros):
    indice = num[0]
    valor = num[1]
    print(f"el indice es: {indice} y el valor es: {valor}")

#usando el else en for
for numero in numeros:
    print(f"ejecutando el ultimo bucle, valor actual: {numero}")
else:
    print("el bucle termino")


#recorreer una lista sin cocodrilo con continue. si se coloca el brack rompe el bucle
for animal in animales:
    if animal == "cocodrilo":
        continue
    print(f" este animal me gusta {animal}")

#for en una sola linea
numeros_duplicados = [x*2 for x in numeros]
print(numeros_duplicados)