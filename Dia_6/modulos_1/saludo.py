#el as remplaza el nombre de la funcion por la que queramos
#import funcion_saludo as F_S

#valor = F_S.saludo("Stiven")
#print(valor)


#esta es otra forma de importar pero solo se importa la funcion que importemos
from funcion_saludo import saludo

valor = saludo("Stiven")
print(valor)
