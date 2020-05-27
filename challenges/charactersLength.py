name = input('name: ')
if len(name) < 3:
    print('the length should be grater than 3 characters')
elif len(name) > 50:
    print('the length should be smaller than 50 characters')
else:
    print('the length is ok')