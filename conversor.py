menu = """ 
Bienvenido al conversor de divisas 💰

[1] Pesos colombianos 
[2] Pesos argentinos
[3] Pesos mexicanos

Elige una opcion: """

def conversion(tipo_pesos, valor):
    pesos = float(input('Pesos ' + tipo_pesos + ' a convertir: '))
    dolar = valor
    dolares = str(round(pesos / dolar, 2))
    print('Tienes $' + dolares + ' dolares')


opcion = int(input(menu))

if opcion == 1:
    conversion('colombianos', 3785)
elif opcion == 2:
    conversion('argentinos', 65)
elif opcion == 3:
    conversion('mexicanos', 24)
else:
    print('Ingresa una opcion correcta por favor')