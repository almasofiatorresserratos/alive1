from math import sqrt

"""print ("PROBLEMA 6")
print (" ")
print ("En este programa le ayudaré a saber el área de la siguiente figura")
radio = int(input("Dime la medida del radio del círculo en cm: "))
hipotenusa = int(input("Dime cuál es la medida de la hipotenusa del triángulo en cm."))
base = radio * 2
areaCirculo = 3.1416 * (radio**2) / 2
altura = (sqrt (hipotenusa**2 - radio**2) * base) /2
total = areaCirculo + altura
print (f"El área de la figura es {total} cm.")
"""
def total (radio, hipotenusa):
  total = (3.1416 * (radio**2) / 2) + (sqrt (hipotenusa**2 - radio**2) * (radio * 2)) / 2
  return total
radio = int(input("¿Cuánto mide en cm el radio del círculo? "))
hipotenusa = int(input("¿Cuánto mide en cm la hipotenusa del triángulo? "))
print ("El área total de la figura es igual a: ")
print (total(radio, hipotenusa))
