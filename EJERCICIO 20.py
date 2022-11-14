'''Ejercicio 20
Mostrar en pantalla los N primero número primos. Se pide por teclado la cantidad
de números primos que queremos mostrar.'''

contador_=1
n=0
n=int(input("Dime la cantidad de numeros primos que quieres que te diga:"))
num=input("")
while contador_!=0:
        contador=0
for i in range(2,num):
    if num%i==0:
            contador=contador+1
    if contador>=1:
            print("El",num, "no es primo")
    else:
            print("El",num, "es primo")