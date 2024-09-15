#Ejercicio 5 dias de la semana

numerosSemana=input(f'Por favor, seleccione día de la semana \nLunes: 1\nMartes: 2\nMiercoles: 3\nJueves: 4\nViernes: 5\nSabado: 6\nDomingo: 7\nPor favor seleccione un numero: ')
match numerosSemana:
    case '1':
        print('El día de la semana es lunes')

    case '2':
        print('El día de la semana es martes')

    case '3':
        print('El día de la semana es miercoles')

    case '4':
        print('El día de la semana es jueves')

    case '5':
        print('El día de la semana es viernes')

    case '6':
        print('El día de la semana es sabado')

    case '7':
        print('El día de la semana es domingo')
