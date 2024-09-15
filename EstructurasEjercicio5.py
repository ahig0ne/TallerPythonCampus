#(random.randint(1, 100))
import random
print('Programa para adivinar un numero del 1 al 100')
randomNumero = (random.randint(1,100))#genera un numero al azar entre 1 y 100 y lo ingresa en la variable
numero=''
while numero != randomNumero:#Si el numero es diferente al numero al azar, repite el ciclo hasta que sea igual al numero al azar
    numero = int(input('ingrese un numero: '))
    if numero<randomNumero:
        numero = 0
        print('el numero ingresado es menor al numero al azar')
    elif numero > randomNumero:
        numero = 0
        print('el numero ingresado es mayor al numero al azar')
    elif numero == randomNumero:
        print('felicidades, acertaste el numero!')
        
