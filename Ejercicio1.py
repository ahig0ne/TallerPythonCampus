#Verificación de numeros pares e impares.

print('Solicita al usuario que ingrese un número y verifica si es par o impar.')
Numero = (int(input('ingrese numero2: ')))
NumeroOperacion = Numero%2 #se establece un modulo para que si el resultado es 0, signifique que el numero es par

if NumeroOperacion == 0:
    print(f'numero {Numero} es par')
else:
    print(f'numero {Numero} es impar')