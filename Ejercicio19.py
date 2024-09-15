#Conversión de calificaciones numéricas a letras
print('Algoritmo que solicita una calificación numérica (0-100) y convierte esa calificación a una letra usando el siguiente esquema:')
calificacion = int(input('por favor ingrese su nota: '))
match calificacion:
    case calificacion if 90 <= calificacion <= 100:
        letra = 'A'
    case calificacion if 80 <= calificacion < 90:
        letra = 'B'
    case calificacion if 70 <= calificacion < 80:
        letra = 'C'
    case calificacion if 60 <= calificacion < 70:
        letra = 'D'
    case calificacion if 0 <= calificacion < 60:
        letra = 'F'

print(f'usted sacó una {letra}')