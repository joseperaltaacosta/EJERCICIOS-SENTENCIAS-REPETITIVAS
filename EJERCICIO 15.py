'''Ejercicio 15
Una persona adquirió un producto para pagar en 20 meses. El primer mes pagó
10 €, el segundo 20 €, el tercero 40 € y así sucesivamente. Realizar un algoritmo
para determinar cuánto debe pagar mensualmente y el total de
lo que pagó después de los 20 meses.'''
contador=1
m1=10
for i in range(1,21):
    contador=contador+1
    print("El mes",contador,"pagó",m*2)