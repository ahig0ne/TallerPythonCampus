#Sistema de evaluacion de creditos universitarios
contadorMaterias=0
credito=0
materiaAprobada=0
print('programa que determina cantidad de creditos en total en base a materias cursadas y su puntaje')
materiasCursadas = int(input('Por favor ingrese numero de materias cursadas: '))
while contadorMaterias < materiasCursadas:
    contadorMaterias=contadorMaterias+1
    print('ingrese la nota de la materia')
    materiaNota=int(input())
    if materiaNota <60:
        print('Materia no aprobada')
    elif materiaNota >=60:
        print('Materia aprobada')
        credito=credito+3
        materiaAprobada = materiaAprobada +1
print(f'De acuerdo a las materias cursadas que son {materiasCursadas} usted aprobó {materiaAprobada} eso significa que tiene un total de {credito} creditos')

    