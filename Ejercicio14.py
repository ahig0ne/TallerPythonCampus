# Adivinanza de letras
secretaletra = 'x'

# Solicitar al usuario que elija una letra
elegida = input('Por favor, selecciona una letra entre a y z: ')

# Evaluar la adivinanza usando match
match elegida:
    case elegida:
        if elegida == secretaletra:
            print('¡Acertaste, felicidades!')
        else:
            print(f'no acertaste, tu numero es {elegida} y la letra secreta es {secretaletra}')

