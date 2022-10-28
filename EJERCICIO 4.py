'''Ejercicio 4
Realizar un algoritmo que pida números (se pedirá por teclado la cantidad de
números a introducir). El programa debe informar de cuantos números
introducidos son mayores que 0, menores que 0 e iguales a 0.'''
num_int=0
num_int=int(input("Cuantos numeros deseas introducir:"))
num1=0
contador_num_mayores=0
contador_num_menores=0
contador_num_iguales=0
num=int
while num1!=num_int:
    num=int(input("Dime numeros:"))
    if num>0:
        contador_num_mayores+=1
    if num==0:
        contador_num_iguales+=1
    if num<0:
        contador_num_menores+=1
    num1+=1
print("Hay", contador_num_menores,"números menores que 0 \n")
print("Hay", contador_num_iguales,"números iguales que 0 \n")
print("Hay", contador_num_mayores,"números mayores que 0 \n")