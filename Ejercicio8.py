#Calcular si un año es bisiesto

print('Programa para calcular si un año es bisiesto.')
año = int(input('Por favor ingrese un año para determinar si es bisiesto: '))
if (año %4 != 0):
    print(f'{año} no es un año bisiesto')
elif (año %4 == 0) and (año %100 != 0):
    print(f'{año} es un año bisiesto')
elif (año %4 == 0) and (año %100 == 0) and (año %400 != 0):
    print(f'{año} no es un año bisiesto')
elif (año %4 == 0) and (año %100 == 0) and (año %400 == 0):
    print(f'{año} es un año bisiesto')

