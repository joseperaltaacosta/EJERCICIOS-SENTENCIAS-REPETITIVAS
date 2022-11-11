'''Ejercicio 16
Una empresa les paga a sus empleados con base en las horas trabajadas en la
semana. Realice un algoritmo para determinar el sueldo semanal de N
trabajadores y, además, calcule cuánto pagó la empresa por los N empleados.'''
total=0
total_pagado=0
trabajadores=0
trabajadores=int(input("Dime cuantos trabajadores hay:"))
contador_trabajador=1
sueldo=0
sueldo=int(input("Dime cuanto cobra por hora:"))
for i in range(trabajadores):
    num=0
    num=int(input(f"Dime cuantas horas ha trabajado en esta semana el trabajador {contador_trabajador}:"))
    contador_trabajador=contador_trabajador+1
    total=sueldo*num
    total_pagado+=total
    print(f"El sueldo semanal del trabajador {contador_trabajador} es de: {total}")
print("El sueldo semanal total es de:",total_pagado,"€")