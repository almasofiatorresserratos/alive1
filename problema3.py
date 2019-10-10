"""print ("PROBLEMA NÚMERO 3:")
print ("hola")
print ("Aquí te ayudaré a calcular el área de un círculo")
print ("Dime cuánto mide el radio del círculo en cm, por favor.")
radio = int (input (""))
area = (radio * radio) * 3.1416
print (f"El área del círculo es igual a {área} cm.")
"""
def area(radio):
  area = (radio * radio) * 3.1416
  return area

radio = int(input("¿Cuánto mide el radio del círculo en cm? "))
print ("El área del círculo es:")
print (area(radio))
