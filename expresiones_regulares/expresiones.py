import re

texto = """hola 2 como estas crack, esta es la primera linea
crack como 23 estas viendo la. 23 segunda 33 linea?
esta es la ultima 233 lienea Esta.?
"""

#el findall muestra todas las coincidencias
#el ignorecase es para ignorar las mayusculas
#resultado = re.findall('esta', texto, flags=re.IGNORECASE)

#\d -> busca digitos entre 0 y 9
#el r es para indicar el uso de expresiones regulares
#resultado = re.findall(r"\d", texto)

#\D -> busca TODO menos 0 y 9
#resultado = re.findall(r"\D", texto)

#\w -> busca caracteres alfanumericos [a-z, A-Z, 0-9, _]
#resultado = re.findall(r"\w", texto)

#\W -> busca TODO MENOS caracteres alfanumericos [a-z, A-Z, 0-9, _]
#resultado = re.findall(r"\W", texto)

#\s -> busca espacios en blanco -> espacios, tabs, saltos de linea
#resultado = re.findall(r"\s", texto)

#\S -> busca TODO MENOS espacios en blanco -> espacios, tabs, saltos de linea
#resultado = re.findall(r"\S", texto)

#. -> busca TODO MENOS saltos de linea
#resultado = re.findall(r'.', texto)

#\n busca saltos de linea
#resultado = re.findall(r'\n', texto)

#\ -> cancela caracteres especiales, cancelamos la funcion del punto y buscamos un punto
#resultado = re.findall(r'\.', texto)

#^ -> busca el comienzo de una linea (se coloca flags para activar multi linea)
#resultado = re.findall(r'^hola', texto, flags=re.M)

#$ -> busca final de la linea
#resultado = re.findall(r'linea$', texto, flags=re.M)

#{n} -> busca n cantidad de veces el valor de la izquierda (dos numeros juntos en este caso)
#resultado = re.findall(r"\d{2}", texto)

#{n,m} -> al menos n, como maximo m
resultado = re.findall(r"\d{2,3}", texto)

# | -> busca una cosa o otra cosa
resultado = re.findall(r"\d{2,3}|hola", texto)
print(resultado)
