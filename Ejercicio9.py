#Solicita la edad de la persona e indica si es niño (0-12 años), adolescente (13-17 años), adulto (18-64 años) o anciano (65 años o más).

edad = int(input('Escriba su edad: '))
#el codigo interpreta si su edad está entre el intervalo establecido para su edad, para así, decir si es niño, adolescente, adulto, o anciano.
if (edad >=0 and edad <=12):
    print(f'su edad es igual a {edad} eso significa que usted es un niño')

elif (edad >=13 and edad <=17):
    print(f'su edad es igual a {edad} eso significa que usted es un adolescente')

elif (edad >=18 and edad <=64):
    print(f'su edad es igual a {edad} eso significa que usted es un adulto')

elif (edad>=65):
    print(f'su edad es igual a {edad} eso significa que usted es un anciano')