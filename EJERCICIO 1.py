'''Ejercicio 1
Crea una aplicación que pida un número y calcule su factorial (El factorial de un
número es el producto de todos los enteros entre 1 y el propio número y se
representa por el número seguido de un signo de exclamación. Por ejemplo 5! =
1x2x3x4x5=120),'''
factorial=1
num=0
num=int(input("Dime un numero:"))
for numero in range(1,num):
    factorial=factorial*(numero+1)
print("El resultado del factorial de", num,"es:",factorial)