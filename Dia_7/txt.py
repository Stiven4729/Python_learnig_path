archivo_sin_leer = open("Dias/Dia_7/info.txt", encoding="UTF-8") #open(para abrir un archivo)

#leer archivo completo
# archivo = archivo_sin_leer.read() #se usa el encoding="UTF-8 para caracteres especiales

#leer una sola linea
linea = archivo_sin_leer.readline()

#leer linea por linea
#lineas = archivo_sin_leer.readlines() #UN ARCHIVO SOLO SE PUEDE LEER UNA SOLA VEZ POR SEGURIDAD

#cerramos el archivo
archivo_sin_leer.close()

print(linea) #lo leemos con el .read() para mostrar el texto y lo imprimimos en consola
