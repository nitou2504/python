menu = """ 
Bienvenido al conversor de divisas 💰

[1] Pesos colombianos
[2] Pesos argentinos
[3] Pesos mexicanos

Elige una opcion: """

opcion = int(input(menu))

if opcion == 1:
    pesos = float(input('Pesos colombianos a convertir: '))
    dolar = 3785
    dolares = str(round(pesos / dolar, 2))
    print('Tienes $' + dolares + ' dolares')
elif opcion == 2:
    pesos = float(input('Pesos argentinos a convertir: '))
    dolar = 65
    dolares = str(round(pesos / dolar, 2))
    print('Tienes $' + dolares + ' dolares')
elif opcion == 3:
    pesos = float(input('Pesos mexicanos a convertir: '))
    dolar = 24
    dolares = str(round(pesos / dolar, 2))
    print('Tienes $' + dolares + ' dolares')
else:
    print('Ingresa una opcion correcta por favor')

