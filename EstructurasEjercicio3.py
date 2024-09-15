#Escribe un programa que solicite al usuario un número entero positivo n y calcule el factorial de dicho número ( n! = 1 * 2 * 3 * ... * n ). Usa un ciclo for para realizar el cálculo.
factorial = 1
print('hallar factorial de un numero, ingrese numero entero positivo')
n = int(input())
if n>0:
    for i in range(1, n+1):
        factorial*=i
else:
    print('numero debe ser positivo')
print(f'el numero factorial de {n} es: {factorial}')