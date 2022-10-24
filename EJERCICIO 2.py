'''Ejercicio 2
Crea una aplicación que permita adivinar un número. La aplicación genera un
número aleatorio del 1 al 100. A continuación va pidiendo números y va
respondiendo si el número a adivinar es mayor o menor que el introducido,a
demás de los intentos que te quedan (tienes 10 intentos para acertarlo). El
programa termina cuando se acierta el número (además te dice en cuantos
intentos lo has acertado), si se llega al limite de intentos te muestra el número
que había generado.'''
import random
num=random.randint(1,100)
num1=0
num1=int(input("Dime un numero:"))
while num1!= num:
    int(input("Dime otro numero:"))
print("Has adivinado el numero secreto")