'''Ejercicio 8
Escribe un programa que pida el limite inferior y superior de un intervalo. Si el
límite inferior es mayor que el superior lo tiene que volver a pedir.
A continuación se van introduciendo números hasta que introduzcamos el 0.
Cuando termine el programa dará las siguientes informaciones:
-La suma de los números que están dentro del intervalo (intervalo abierto).
-Cuantos números están fuera del intervalo.
-He informa si hemos introducido algún número igual a los límites del intervalo.'''
lim_inf=0
lim_sup=0
lim_inf=int(input("Dime el limite inferior de un intervalo:"))
lim_sup=int(input("Dime el limite superior de un intervalo:"))
while (lim_inf>lim_sup) or (lim_inf!=0):
    int(input("Dime el limite inferior de un intervalo:"))
