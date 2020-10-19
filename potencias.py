def run():
    i = 0
    potencia = n**i
    while potencia < l:
        print(str(n) + ' elevado a ' + str(i) + ' es ' + str(potencia))
        i = i+1
        potencia = 2**i

print('Hola! te mostrare todas las potencias de un numero hasta un limite')
n = int(input('Cual es tu numero?: '))
l = int(input('Cual es el limite?: '))


if __name__ == '__main__':
    run()