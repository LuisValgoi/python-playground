# variables
# ame = 'valgoi'
# age = 23
# is_new = True

# receiving inputs
# name = input('what is your name? ')
# color = input('what is your favorite color? ')
# print(name + ' likes ' + color)

# type conversion
# birth_year = input('Birth Year: ')
# age = 2020 - int(birth_year)
# print('You are: ' + str(age))

# formatted strings
# email = '''
# carai,
# borracha
# '''
# print(email)

# array & strings
# name = 'valgoi'
# print(name) # valgoi
# print(name[0:2]) # va
# print(name[0:-2]) # valg
# print(name[1:]) # algoi
# print(name[-1]) # i
# print(name[0]) # v
# print(name[1:-1]) # algo

# string template
# name = 'Luis'
# last = 'valgoi'
# print(f'{name} is the {last}')

# string methods
# name.upper()
# name.lower()
# name.title()
# name.find()
# name.replace()
# print(name)

# operators
# print(10 // 3) # 3
# print(10 ** 3) # 1000
# print(abs(-5)) # 5
# print(round(4.3)) # 4

# import math #https://docs.python.org/3/library/math.html
# value = math.factorial(5)
# print(value)

# if statement
# is_hot = 'nao'
# if isinstance(is_hot, str) and (is_hot == 'sim'):
#     print('ta quente, porra')
# elif isinstance(is_hot, str) and (is_hot == 'nao'):
#     print('ta frio, porra')
# else:
#     print('ihh')

# house_value = 10
# user_credit = int(input('how much do you have (R$) ? '))
# put_down = 0
# if user_credit >= 10:
#     put_down = house_value * 0.1
# else:
#     put_down = house_value * 0.2
# print(f'you need to put me down R$ {round(put_down)}')

# print(not(True))
# print(1 != 2)
# for n in range(10):
#     print(n)

# name = input('nome: ')
# if len(name) < 3:
#     print('+3 caracteres')
# elif len(name) > 50:
#     print('menos de 50 caracteres')
# else:
#     print('ok')

# secret = int(input('secret key: '))
# attempts = 0
# right = False
# while attempts < 3 and not right:
#     guess = int(input(f'guess nº{attempts+1}: '))
#     if guess != secret:
#         attempts += 1
#     else:
#         right = True
#         print("It's correct")
#         break
#
# if attempts == 3 and not right:
#     print('you have failed')

# print('voce tem 3 tentativas!')
# guess = input('é Rafael doque? ')
# secret = 'Ferrari'
# attempts = 0
# while attempts < 2 and guess != secret:
#     guess = input('é do que mesmo? ')
#     if guess == secret:
#         print('fuck yeah!')
#         break
#     else:
#         attempts += 1
# if attempts == 2 and guess != secret:
#     print('looser')

# hora_inicio = input('qual horario que tu comeca a trabalhar? ')
# hora_fim = input('qual horario que tu termina de trabalhar? ')
# print(f'voce trabalha: {int(hora_fim) - int(hora_inicio)} hrs por dia')


# cor_preferida = 'verde'
# palpite = input('qual a cor preferida do lucas? ')
# quantidade_de_tentativas = 1
# while palpite != cor_preferida:
#     print('ERROU!')
#     palpite = input('qual a cor preferida do lucas? ')
#     quantidade_de_tentativas = quantidade_de_tentativas + 1
# print('Acho bom!!')
# print(f'Quantidade de tentativas: {quantidade_de_tentativas}')

# start_key = 'start'.upper()
# stop_key = 'stop'.upper()
# quit_key = 'quit'.upper()
# help_key = 'help'.upper()
# keys = [start_key, stop_key, quit_key, help_key]
#
# not_found_msg = "I don't' understand that\n"
# help_msg = '''start - to start the car
# stop - to stop the car
# quit - to exit\n'''
# start_msg = 'Car started... ready to go'
# stop_msg = 'Car stopped'
#
# cmd_user = ''
# while cmd_user != quit_key.upper():
#     cmd_user = input('>').upper()
#     if cmd_user not in keys:
#         print(not_found_msg)
#     elif cmd_user == help_key:
#         print(help_msg)
#     elif cmd_user == start_key:
#         print(start_msg)
#     elif cmd_user == stop_key:
#         print(stop_msg)

# amount = int(input('amount items: '))
# records = []
#
# i = 0
# while i < amount:
#     valor = int(input(f'value {i+1}: '))
#     records.append(valor)
#     i = i + 1
#
# bigger = 0
# for record in records:
#     if record > bigger:
#         bigger = record
#
# print(f'the bigger is: {bigger}')
