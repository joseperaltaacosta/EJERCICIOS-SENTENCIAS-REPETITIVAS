'''Ejercicio 7
Realizar una algoritmo que muestre la tabla de multiplicar de un número
introducido por teclado.'''
num1=0
num1=int(input("Dime el numero del que quieres la tabla de multiplicar:"))
print("La tabla de multipiclar es:")
for num in range(1,11):
    print(num1,"*",num,"es:",num1*num)