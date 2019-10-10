"""print ("PROBLEMA NÚMERO 4:")
print (" ")
print ("hola")
print ("Aquí te ayudaré a calcular el área de un terreno que tiene la siguiente forma:")
print ("  |-")
print ("  |      -")
print ("  |           -")
print ("  |                -")
print ("A |                 | ")
print ("  |                 |  C")
print ("  |                 | ")
print ("  -------------------")
print ("           B")
print ("Tú deberás decirme las medidas de cada lado en cm. para poder sacar el área.")
print (" ")
ladoA = int (input("Dime la medida del lado A, por favor: "))
ladoB = int (input("Dime la medida del lado B, por favor: "))
ladoC = int (input("Dime la medida del lado C, por favor: "))
área1 = (ladoB * ladoC)
área2 = ((ladoA - ladoC) * ladoB) / 2
total = área1 + área2
print (f"El área de la figura mide {total} cm.")
"""
def total(ladoA, ladoB, ladoC):
  total = ((ladoA / 2) * ladoB) + ((ladoA / 2) * ladoB / 2)
  return total

ladoA = int(input("¿Cuánto mide el lado A de la figura? "))
ladoB = int(input("¿Cuánto mide el lado B de la figura? "))
ladoC = int(input("¿Cuánto mide el lado C de la figura? "))
print (total(ladoA, ladoB, ladoC))
