name = "stiven"
years = 20
height = 1.70
boolean = True
"""
concatenacion correcta para evitar fallos o descuidos a la hora de mostrar variables 
ya que en python la concatenacion cambia dependiendo el dato (si es string, int, boolean o float)
para una concatenacion global se usa los f string
"""""
print (f"Hello {name}")
print (f"you'r {years} years old")
print (f"your height is {height} m")
print (f"this information is {boolean}")


'el in funciona para budscar en la variable lo indicado tambien sirve con el not in'
print('en' in name)
print('en' not in name)