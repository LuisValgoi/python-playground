favorite_color = 'verde'
guess = input("What's your favorite colour?")
attempts = 1
while guess != favorite_color:
    print('Wrong!')
    guess = input("What's your favorite colour?")
    attempts = attempts + 1
print('Correct!')
print(f'Attempts Tried: {attempts}')
