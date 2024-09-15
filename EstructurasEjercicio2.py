#Contador de vocales en una cadena
numeroVocales = 0
vocales ='aeiou'
print('Por favor ingrese una cadena de texto para determinar su numero de vocales')
cadenaTexto = str(input())
for v in cadenaTexto:#este for hace que el codigo se sume letra por letra en la variable v
    if v in vocales:#esta parte hace que el codigo sume un valor cada que esa suma de variables cuente una vocal
        numeroVocales+=1
print(f'el numero de vocales es {numeroVocales}')