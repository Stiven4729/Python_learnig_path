numeros = [1,2,3,4,5,6,7,8,9]

#creando una funcion que retorne numeros pares

#def es_pares(num):
#    if (num % 2 == 0 ):
#        return True
#usando filter como funcion comun
#numeros_pares = filter(es_pares, numeros)


#creando la misma funcion que retorne numeros pares pero con lambda
es_par = filter(lambda num:num%2==0, numeros)
print(list(es_par))
