'''Ejercicio 19
Realizar un ejemplo de menú, donde podemos escoger las distintas opciones
hasta que seleccionamos la opción de “Salir”.'''
salir=0
salir=int(input("Que quieres hacer:"))
print("Pulsa un numero distinto de 0 si quieres continuar")
print("Pulsa 0 si quieres salir")
while salir!=0:
    salir=int(input("Que quieres hacer:"))
    print("Pulsa 0 si quieres salir")
print("Has salido")