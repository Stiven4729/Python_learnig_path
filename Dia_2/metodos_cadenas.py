cadena_1 = "hola soy stiven hola s1"
cadena_2 = "Bienvenido,crack"

#El .upper convierte a mayusculas
mayusculas = cadena_1.upper()


#el .lower convierte a minusculas
minuscula = cadena_1.lower()

# el .capitalize convierte todo a minuscula y luego convierte la primera litra en mayuscula
primera_letra_mayuscula = cadena_1.capitalize()

#busquedad de una cadena en otra cadena. si no encuentra ningun caracter parecido devulve un -1
busquedad_find = cadena_1.find("4")

#busquedad de una cadena en otra cadena. si no encuentra ningun caracter parecido devulve una excepcion
busquedad_index = cadena_1.index("hola")
print(busquedad_index)

#si es numerico nos devuelve true
es_numerico =  cadena_1.isnumeric()


#si es alfanumerico (de la A hasta la Z )devolvemos true
es_alfanumerico = cadena_1.isalpha()

#busquedad de una cadena en otra cadena. devuelve la cantidad de veces que se repite un caracter
contar_coincidencias = cadena_1.count("4")
print(contar_coincidencias)
if cadena_1.count("4") != 0 | cadena_1.count("9") | cadena_1.count("2"):
    print("hola")
else:
    print("chao")

#contar cuantos caracteres hay en cadena de texto
contar_caracteres = len(cadena_1)# --funcion

#veriicamos si una cadena empieza con otra cadena dada, si es asi devuelve true
empieza_con = cadena_1.startswith("H")

#veriicamos si una cadena termina con otra cadena dada, si es asi devuelve true
termina_con = cadena_1.endswith("ven")

#si el valor 1, se encuentra en la cadena original, remplaza el valor 1 de la misma, por el valor 2
cadena_nueva = cadena_1.replace("Hola", "Chao")

#separar cadenas con la cadena que le pasemos 
cadena_separada = cadena_2.split(",") 