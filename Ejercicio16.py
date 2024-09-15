#Calculo del tiempo de viaje

print('Programa que calcula el tiempo de viaje')
distanciaRecorrer = int(input('Por favor ingrese la distancia a recorrer en km: '))
velocidadPromedio = int(input('Por favor ingrese la velocidad promedio del vehículo: '))
#formula para calcular el tiempo de viaje = distancia del recorrido dividido por la velocidad promedio
tiempoViaje = distanciaRecorrer / velocidadPromedio
tiempoViajeMin = tiempoViaje * 60
print(f'el tiempo de viaje es de {tiempoViaje} horas, lo mismo que {tiempoViajeMin} minutos')
if (velocidadPromedio>100):
    print('por favor reduzca la velocidad')