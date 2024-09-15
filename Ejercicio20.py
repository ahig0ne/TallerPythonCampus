#Sistema de estacionamiento con tarifas progresivas
print('Sistema de estacionamiento\nPrimera hora: $5\nSegunda a cuarta hora: $4 por hora\nMas de cuatro horas: $3 por cada hora adicional')
horaEstacionamiento = int(input('Indique cuantas horas estuvo usted con su vehiculo en el estacionamiento: '))
hora = 0
valor = 0
if horaEstacionamiento == 1:
    hora = hora +1
    valor = 5
elif horaEstacionamiento>=2 and horaEstacionamiento<=4:
    while horaEstacionamiento > hora:
        hora = hora + 1
        valor = 4
        valorTotal = valor * hora
elif horaEstacionamiento>4:
    while horaEstacionamiento > hora:
        hora = hora + 1
        valor = 3
        valorTotal = valor * hora
valorTotal = valor * hora
print(f'usted estuvo un total de {horaEstacionamiento} eso significa que la hora en el lugar vale {valor}$ y usted tiene que pagar {valorTotal}$')