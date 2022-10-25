'''Ejercicio 2
Crea una aplicación que permita adivinar un número. La aplicación genera un
número aleatorio del 1 al 100. A continuación va pidiendo números y va
respondiendo si el número a adivinar es mayor o menor que el introducido,a
demás de los intentos que te quedan (tienes 10 intentos para acertarlo). El
programa termina cuando se acierta el número (además te dice en cuantos
intentos lo has acertado), si se llega al limite de intentos te muestra el número
que había generado.'''
import random

intentos=1

num=random.randint(1,100)

num1=0
num1=int(input("Dime un numero:"))

if num1>num:
    print("El numero que tienes que adivinar es menor")
if num1==num:
    print("")
if num1<num:
    print("El numero que tienes que adivinar es mayor")

while num1!= num and intentos!=10:
    num1=int(input("Dime otro numero:"))
    if num1>num:
        print("El numero que tienes que adivinar es menor")
    if num1==num:
        print("")
    if num1<num:
        print("El numero que tienes que adivinar es mayor")
    intentos+=1
if intentos==10:
    print("El numero secreto era:",num)
else:
    print("Has adivinado el numero despues de",intentos,"intentos")
print("Has adivinado el numero secreto")