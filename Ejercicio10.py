#Clasificación de notas
#Escribe un programa que asigne una calificación basada en una nota numérica.

notaCompleta = float(input('Ingrese su calificación del 0 al 100: '))
if (notaCompleta<60):
    print(f'Su nota es {notaCompleta} eso significa que es una F')
elif (notaCompleta>=60 and notaCompleta<=69):
    print(f'Su nota es {notaCompleta} eso significa que es una D')
elif (notaCompleta>=70 and notaCompleta<=79):
    print(f'Su nota es {notaCompleta} eso significa que es una C')
elif (notaCompleta>=80 and notaCompleta<=89):
    print(f'Su nota es {notaCompleta} eso significa que es una B')
elif (notaCompleta>=90 and notaCompleta<=100):
    print(f'Su nota es {notaCompleta} eso significa que es una A')