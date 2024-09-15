#Calculadora de IMC (Índice de Masa Corporal)
peso = int(input('Por favor indique su pero en kg: '))
altura = int(input('Por favor indique su estura en centimetros: '))
metros = altura/100
#formula para calcular el IMC
IMC = peso / metros**2
if (IMC <18.5):
    print(f'dada su estatura {altura}mts y su peso {peso}kg su IMC es {IMC} es de bajo peso')
elif (IMC>=18.5 and IMC<25):
    print(f'dada su estatura {altura}mts y su peso {peso}kg su IMC es {IMC} es de peso normal')
elif (IMC>=25 and IMC<30):
    print(f'dada su estatura {altura}mts y su peso {peso}kg su IMC es {IMC} es de sobrepeso')
elif (IMC>=30):
    print(f'dada su estatura {altura}mts y su peso {peso}kg su IMC es {IMC} es de obesidad')
