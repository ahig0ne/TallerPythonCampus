#Escribe un programa que solicite al usuario un número entero positivo n y calcule la suma de los primeros n números enteros. Utiliza un ciclo for para realizar la suma.

print('seleccione un numero entero positivo')
n = int(input())
suma = 0
if n > 0:
    for numeros in range (0, n+1):#esto hace que el numero entero positivo agregado, sea la cantidad hasta la que llegue el contador como tope, mas uno para que cuente esa cantidad exacta.
        suma = suma + numeros
elif n <= 0:
    print('numero no es entero positivo')
print(f'La suma de los primeros numeros enteros positivos de {n} es igual a {suma}')