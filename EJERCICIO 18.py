'''Ejercicio 18
Hacer un programa que muestre un cronometro, indicando las horas, minutos y
segundos.'''
h=0
min=0
seg=0
decimas=0
while h!=24:
    h+=1
    print(h,"horas")
    while min!=60:
        min+=1
        print(min,"minutos")
        while seg!=60:
            seg+=0.0002
            print(seg,"segundos")