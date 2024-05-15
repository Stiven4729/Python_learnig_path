#creando un  conjunto con set()
conjunto = set(["dato1"])

#metiendo un conjunto dentro de otro conjunto utilizando el frozenset
conjunto1 = frozenset("dato1", "dato2")
conjunto2 = {conjunto1, "dato3"}
print(conjunto2)

#teoria de conjuntos

conjunto1 = {1,2,3,4,5}
conjunto2 = {1,3,5}
#se usa la funcion issuperset para preguntar si conjunto 2 es un sub conjunto de conjunto1 este nos devolvera un bool
resultado = conjunto2.issubset(conjunto1)
#tambien es asi 
#resultado = conjunto2 <= conjunto1 

#verificando si es un super conjunto
resultado = conjunto2.issuperset(conjunto1)
resultado = conjunto2 > conjunto1

#verificar si solo hay un numero en comun. si existe un numero en comun arroja false. la unica forma de que arroje true es que no tenga nada en comun
resultado = conjunto2.isdisjoint(conjunto1)

print(resultado)