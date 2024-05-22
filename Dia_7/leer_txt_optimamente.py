
#usando with open para abrir un archivo de manera optima
with open("Dias/Dia_7/info.txt", encoding="UTF-8") as archivo:
    #leemos el archivo
    contenido = archivo.read()
    #imprimimos el archivo
    print(contenido)

#no es necesario cerrarlo al usar with open
