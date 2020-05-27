# normal arguments
def callMe():
    print('my name')
print('start')
callMe()

# position arguments
def get_name(first, last):
    return f'{last}, {first}'
full_name = get_name(first='luis', last='valgoi')
print(full_name)

# none return
def return_none():
    return None
print(return_none())