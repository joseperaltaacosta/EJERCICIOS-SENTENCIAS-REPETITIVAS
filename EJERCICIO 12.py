'''Ejercicio 12
Realizar un algoritmo para determinar cuánto ahorrará una persona en un año, si
al final de cada mes deposita cantidades variables de dinero; además, se quiere
saber cuánto lleva ahorrado cada mes.'''
total=0
contador=0
for i in range(1,13):
    num=int(input("Cuanto dinero has ahorrado este mes:"))
    total= total+num
    contador=contador+1
    print("El dinero ahorrado en el mes", contador,"es de:",total)
print("La cantidad que has ahorrado este año es de:", total)