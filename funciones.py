
def conversacion(mensaje):
    print('Hola')
    print('Que tal')
    print('Elegiste la opcion '+ mensaje)
    print('De nada, vuelva pronto 🤠')

opcion = int(input('Elige una opcion (1, 2, 3): '))

if opcion == 1:
    conversacion('1')
elif opcion == 2:
    conversacion('2')
elif opcion == 3:
    conversacion('3')
else:
    print('No escogiste nimguna, me da amsiedad 🐶')