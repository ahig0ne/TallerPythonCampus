#Juego de adivinanza de numeros

import random
#libreria para generar numeros al azar
randomNumber = (random.randrange(1, 11))
#este comando genera numeros al azar entre 1 y 11-1(10)
print('Programa genera numero aleatorio entre 1 y 10.\nescriba un numero y el programa indica si el numero ingresado es mayor, menor o igual al numero generado')
NumeroEsc = int(input('Ingrese numero entre 1 y 10: '))

if (NumeroEsc > randomNumber):
    print(f'el numero que seleccionaste es {NumeroEsc} que es mayor que el numero al azar equivalente a {randomNumber}')

if (NumeroEsc == randomNumber):
    print(f'el numero que seleccionaste es {NumeroEsc} que es igual que el numero al azar equivalente a {randomNumber}')

if (NumeroEsc < randomNumber):
    print(f'el numero que seleccionaste es {NumeroEsc} que es menor que el numero al azar equivalente a {randomNumber}')