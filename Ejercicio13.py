#Comparación de 3 numeros
print('Algoritmo para comparar tres numeros y determinar cual es mayor')
primerNum = int(input('Por favor seleccione primer numero: '))
segundoNum = int(input('Por favor seleccione segundo numero: '))
tercerNum = int(input('Por favor seleccione tercer numero: '))
if (primerNum>segundoNum>=tercerNum):
    print(f'{primerNum} es el numero mayor')
elif (primerNum<segundoNum>=tercerNum):
    print(f'{segundoNum} es el numero mayor')
elif (primerNum<=segundoNum<tercerNum):
    print(f'{tercerNum} es el numero mayor')
else:
    print('los numeros son iguales')