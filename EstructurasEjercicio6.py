#Suma de números pares hasta que se introduce un impar
suma = 0
while True:
    numero = int(input("Ingresa un número entero (o un número impar para detenerse): "))
    if numero % 2 != 0:
        # Si el número es impar, rompe el bucle
        break
    suma += numero
print("La suma de los números pares ingresados es:", suma)
