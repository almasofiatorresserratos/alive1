"""print ("PROBLEMA NÚMERO 5")
print (" ")
print ("Este programa es para saber tu pago anual.")
quincena = int (input("¿Cuánto dinero ganas en quince dias"))
quin = quincena * .15
diario = quin / 15
print (f"Entonces ganas $ {diario} diarios.")
anual = diario * 365
print (f"Y entonces ganas $ {anual} al año.")
"""
def anual(quincena):
  anual = (quincena * .15) * 365
  return anual

quincena = int(input("¿Cuánto dinero ganas en quince días? $ "))
print ("Ahorras en total:$ ")
print (anual(quincena))
