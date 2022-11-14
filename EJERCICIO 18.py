'''Ejercicio 18
Hacer un programa que muestre un cronometro, indicando las horas, minutos y
segundos.'''
h=0
min=0
seg=0
for h in range(24):
    h+=1
    print("**********")
    print(h,"HORAS")
    print("**********")
    for min in range(60):
        min+=1
        print("**********")
        print(min,"MINUTOS")
        print("**********")
        for seg in range(60):
            seg+=1
            print(seg,"segundos")