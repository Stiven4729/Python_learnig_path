diccionario = {
    "nombre": "Stiven",
    "apellido": "Gallego",
    "suscriptores": 100000
}

#recorriendo diccionario con items() para obtener la clave y valor
for datos in diccionario.items():
    key = datos[0]
    value = datos[1]
    print(f"la clave es: {key} y el valor es: {value}")