'''Ejercicio 3
Algoritmo que pida números hasta que se introduzca un cero. Debe imprimir la
suma y la media de todos los números introducidos.'''
num=0
num=int(input("Dime un numero:"))
suma=0
contador=0
while num!=0:
    num1=int(input("Dime un numero:"))
    suma=num1+suma

print("La suma de tus numeros es:", suma)
print("La media de tus numeros es:", suma/contador)