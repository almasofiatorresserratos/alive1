"""print ("PROBLEMA NÚMERO 2:")
print ("hola")
print ("En esta tienda damos un 15% de descuento en TODAS TUS COMPRAS")
print ("Dime cuánto dinero es el precio de tu compra, por favor.")
precio = int (input(""))
total = precio - (precio * .15)
print (f"En total vas a pagar $ {total} pesos.")
"""


def total(precio):
  total = precio - (precio * .15)
  return total

precio = int(input("¿Cuánto es el precio de tu compra? $"))
print ("En esta tienda te damos un 15% de descuento en todas tus compras. Así que pagas:")
print (total(precio))
