'''Ejercicio 11
Escribe un programa que diga si un número introducido por teclado es o no
primo. Un número primo es aquel que sólo es divisible entre él mismo y la
unidad. Nota: Es suficiente probar hasta la raíz cuadrada del número para ver si
es divisible por algún otro número.'''
num=int(input("Dime un numero:"))
contador=0
for i in range(2,num):
    if num%i==0:
        contador=contador+1
if contador>=1:
    print("El",num, "no es primo")
else:
    print("El",num, "es primo")