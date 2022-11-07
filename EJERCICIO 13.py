'''Ejercicio 13
Una empresa tiene el registro de las horas que trabaja diariamente un empleado
durante la semana (seis días) y requiere determinar el total de éstas, así como el
sueldo que recibirá por las horas trabajadas.'''
total=0
contador=1
sueldo=0
sueldo=int(input("Dime cuanto cobra por hora:"))
for i in range(1,7):
    num=0
    num=int(input(f"Dime cuantas horas ha trabajado el dia {contador}:"))
    contador=contador+1
    total= total+num
print("La cantidad de horas que ha trabajado en la semana es de:", total)
print("El sueldo semanal es de:",total*sueldo,"€")