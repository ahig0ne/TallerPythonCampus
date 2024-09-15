#Sistema de calificaciones con bonificaciones

print('Programa que calcula la calificación final')
calificacion = int(input('Por favor ingrese su calificación: '))
notaAdicional = input('hizo usted tareas adionales?\nIndique si o no: ').lower()
match notaAdicional:
    #si el estudiante hizo nota adicional, se multiplica por 0.05 de nota extra para tener un 5% mas
    case 'si':
        calificacionAdicional = (calificacion * 0.05) + calificacion
        if calificacionAdicional > 100:
            calificacionAdicional = 100
print(f'Su calificacion es {calificacionAdicional}')