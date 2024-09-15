#Escribe un programa que clasifique un triángulo en agudo, obtuso o rectángulo según sus ángulos internos usando if .

print('Solicitar al usuario tres angulo de un triangulo')
anguloUno = int(input('por favor ingrese primer angulo'))
anguloDos = int(input('por favor ingrese segundo angulo'))
anguloTres = int(input('por favor ingrese tercer angulo'))

if  anguloUno!=anguloDos!=anguloTres<90:
    triangulo = 'agudo'
elif anguloUno==90 or anguloDos==90 or anguloTres==90:
    triangulo = 'rectangulo'
elif anguloUno>90 or anguloDos>90 or anguloTres>90:
    triangulo = 'obtuso'
print (f'de acuerdo al los 3 angulos ingresados, el triangulo es {triangulo}')