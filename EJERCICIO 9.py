'''Ejercicio 9
Escribe un programa que dados dos números, uno real (base) y un entero
positivo (exponente), saque por pantalla el resultado de la potencia. No se puede
utilizar el operador de potencia.'''
base=int(input("Dime la base de la potencia:"))
potencia=base
exponente=int(input("Dime el exponente de la potencia:"))
for i in range(exponente-1):
    potencia*=base
print("El resultado de la potencia es:",potencia)