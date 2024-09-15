#Escribe un programa que solicite al usuario dos números enteros, un valor de inicio y un valor de fin. El programa debe imprimir todos los números pares en ese rango, incluyendo los límites. Usa un ciclo for para recorrer el rango.
numerosPares= 0
print('programa para escribir los numeros enteros entre cierto rango')
valorIni= int(input('por favor ingrese el valor de inicio: '))
valorFin= int(input('por favor ingrese el valor del final: '))

for i in range (valorIni,valorFin+1):
    pares= i%2
    if pares == 0:
        numerosPares+=1
print(f'los numeros pares entre {valorIni} y {valorFin} son: {numerosPares}')
