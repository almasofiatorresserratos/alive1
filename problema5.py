print ("PROBLEMA NÚMERO 5")
print ("Este programa es para saber tu pago anual.")
print ("¿Cuánto dinero ganas en quince días?")
quincena = int (input(""))
quin = quincena * .15
diario = quin / 15
print (f"Entonces ganas $ {diario} diarios.")
anual = diario * 365
print (f"Y entonces ganas $ {anual} al año.")
