#Número positivo, negativo o cero

print('programa para determinar si un numero es positivo, negativo o igual a 0')
numero = int(input('Por favor seleccione un numero entero: '))
#al seleccionar un numero, el codigo detecta si es positivo, negativo o 0
if (numero > 0):
    print(f'el numero {numero} es positivo')

if (numero < 0):
    print(f'el numero {numero} es negativo')

if (numero == 0):
    print(f'el numero {numero} es igual a 0')