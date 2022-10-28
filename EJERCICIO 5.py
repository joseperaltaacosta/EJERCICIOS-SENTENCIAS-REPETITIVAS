'''Ejercicio 5
Algoritmo que pida caracteres e imprima ‘VOCAL’ si son vocales y ‘NO VOCAL’
en caso contrario, el programa termina cuando se introduce un espacio.'''
caracter=str
while caracter!=" ":
    caracter=str(input("Dime un caracter en minuscula"))
    if (caracter=="a")or (caracter=="e") or (caracter=="i") or (caracter=="o") or (caracter=="u"):
        print("Vocal")
    else:
        print("No Vocal")