def palindromo(palabra):
    palabra = palabra.strip()
    palabra = palabra.replace(' ', '')
    palabra = palabra.lower()
    inversa = palabra[::-1]
    if palabra == inversa:
        return True
    else:
        return False


def run():
    palabra = input('Escribe una palabra: ')
    es_palindromo = palindromo(palabra)
    if es_palindromo == True:
        print('Es palindromo')
    else:
        print('No es palindromo')


if __name__ == '__main__':
    run()