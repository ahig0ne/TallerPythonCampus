#Calificación de una nota.

print('Solicita al usuario una calificación y determina si la nota es aprobatoria (>= 60) o reprobatoria (<60).')
calificacion = int(input('Ingrese calificación:  '))

#Si la nota es <60, la nota es reprobatoria, de lo contraio, será aprobatoria.
if calificacion < 60:
    print('La nota es reprobatoria')
else:
    print('La nota es aprobatoria')