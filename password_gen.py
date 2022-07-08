import random

print('>>> Bem Vindo ao Gerador de Password <<<')

print('>>> Esolha seu idioma / Chose your language <<<')

linguagem = input('>>> P = Português / E = English:\n').lower()

if linguagem == 'p':

    caracteres = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%1234567890'

    number = int(input('Quantos passwords você quer criar?'))

    if number < 2:

        tamanho_password = int(input('Quantos caracteres o password deve ter?'))

        print('\nAqui está seu password:')

        for pw in range(number):
            password = ''
            for c in range(tamanho_password):
                password += random.choice(caracteres)
            print(password)
    else:

        tamanho_password = int(input('Quantos caracteres o password deve ter?'))

        print('\nAqui estão seus passwords:')

        for pw in range(number):
            password = ''
            for c in range(tamanho_password):
                password += random.choice(caracteres)
            print(password)
elif linguagem == 'e':

    caracteres = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%1234567890'

    number = int(input('Amount of passwords to generate:'))

    if number < 2:

        tamanho_password = int(input('Input your password length'))

        print('\nHere are your password:')

        for pw in range(number):
            password = ''
            for c in range(tamanho_password):
                password += random.choice(caracteres)
            print(password)
    else:

        tamanho_password = int(input('Quantos caracteres o password deve ter?'))

        print('\nHere is your passwords:')

        for pw in range(number):
            password = ''
            for c in range(tamanho_password):
                password += random.choice(caracteres)
            print(password)
else:
    print('Você digitou um caracter inválido / Inválid character')
