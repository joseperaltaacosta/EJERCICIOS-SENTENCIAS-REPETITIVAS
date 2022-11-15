'''Ejercicio 20
Mostrar en pantalla los N primero número primos. Se pide por teclado la cantidad
de números primos que queremos mostrar.'''

vNum=[]
num_primo=0
numero_primo=(int(input("Dime la cantidad de numeros primos que quieres que te muestre:")))
i=2
contador=numero_primo
def num_primo(num):
        num_primo=0
        for i in range(2,num):
                if num%i==0:
                        num_primo+=1
                if num_primo>=1:
                        return False
                else:
                        return True
while contador!=0:
        if num_primo(i)==True:
                vNum.append(i)
                contador-=1
        i+=1
print(vNum)