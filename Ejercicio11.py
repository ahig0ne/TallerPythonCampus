#Conversión de temperaturas
print('Programa que convierte un tipo de grado a otro, Celsius a Fahrenheit y viceversa')
grado = float(input('Escribe la temperatura: '))
tipoGrado = (input('Escribe la escala de temperatura\nGrados Celsius: C\nGrados Fahrenheit: F\nTemperatura: '))
match tipoGrado:
    case 'C':
        #Formula para convertir Celsius a Fahrenheit
        conversion = (grado*9/5)+32
        print(f'{grado}{tipoGrado} es igual a {conversion}F')
    case 'F':
        #Formula para convertir Fahrenheit a Celsius
        conversion = (grado-32)*5/9
        print(f'{grado}{tipoGrado} es igual a {conversion}C')