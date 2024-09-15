#Calculadora basica

print('Calculadora simple')
NumeroUno=int(input('Seleccione primer numero: '))
NumeroDos=int(input('Seleccione segundo numero: '))
MathOp=(input(f'Ingrese que tipo de operación\nSuma: +\nResta: -\nMultiplicacion: *\nDivision: / \n Operacion a elegir: '))
#Se establecen las variables, al recibir los datos y la operación, se procede a dar resultado con match
match MathOp:
    case '+':
        NumeroResultado= NumeroUno + NumeroDos
        print(f'La suma de {NumeroUno} y {NumeroDos} es igual a {NumeroResultado}')
    case '-':
        NumeroResultado= NumeroUno - NumeroDos
        print(f'La resta de {NumeroUno} y {NumeroDos} es igual a {NumeroResultado}')
    case '*':
        NumeroResultado= NumeroUno * NumeroDos
        print(f'La multiplicacion de {NumeroUno} y {NumeroDos} es igual a {NumeroResultado}')
    case '/':
        NumeroResultado= NumeroUno / NumeroDos
        print(f'La division de {NumeroUno} y {NumeroDos} es igual a {NumeroResultado}')
    case _:
        print('Algo salió mal en la operacion')
        