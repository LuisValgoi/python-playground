secret = int(input('integer key: '))
attempts = 0
right = False
while attempts < 3 and not right:
    guess = int(input(f'guess nº{attempts+1}: '))
    if guess != secret:
        attempts += 1
    else:
        right = True
        print("It's correct")
        break

if attempts == 3 and not right:
    print('you have failed')