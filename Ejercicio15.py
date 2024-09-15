#calculo del salario neto
co = float (0.20) 
pe = float (0.15)
br = float (0.10)
#valor del porcentaje de impuestos
salarioBruto = int(input('Por favor, ingrese su salario bruto: '))
print (f'Su salario bruto es {salarioBruto}')
paisResidencia = str(input('Por favor, ingrese su pais\nColombia : co\nPeru : pe\nBrasil : br\n que pais de residencia?: ')).lower()
match paisResidencia:
    case 'co':
        pais = 'Colombia'
        salarioNeto = salarioBruto - (salarioBruto*co)
    case 'pe':
        pais = 'Peru'
        salarioNeto = salarioBruto - (salarioBruto*pe)
    case 'br':
        pais = 'Brasil'
        salarioNeto = salarioBruto - (salarioBruto*br)
    case _:
        print('algo ocurrió mal.')
print(f'al ser su salario {salarioBruto}, y ser usted del país seleccionado {pais}(impuestos: {co}%), usted tiene un salario neto de {salarioNeto}')