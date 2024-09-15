#Determinacion del tipo de triangulo

print('Determinar si un triangulo es Isosceles, Equilatero o Escaleno')

PrimerLado = input('Por favor ingrese longitud del primer lado del triangulo: ')
SegundoLado = input('Por favor ingrese longitud del segundo lado del triangulo: ')
TercerLado = input('Por favor ingrese longitud del tercer lado del triangulo: ')

#Equilatero : tercer lados iguales , Isoceles : dos lados iguales , Escaleno : todos los lados diferentes

if (PrimerLado == SegundoLado == TercerLado):
    print('Triangulo es equilatero')

elif (PrimerLado == SegundoLado != TercerLado) or (PrimerLado != SegundoLado == TercerLado) or (TercerLado != PrimerLado == SegundoLado):
    print('Triangulo es isosceles')

else:
    print('Triangulo es escaleno')