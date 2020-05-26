users_list = []
users_list_amount = int(input('how many items you want to add?'))
iterations = 0
while iterations < users_list_amount:
    value = int(input(f'{iterations}ª value: '))
    users_list.append(value)
    iterations += 1

i = 0
users_list_uniques = []
while i < users_list_amount:
    value = users_list[i]
    if value not in users_list_uniques:
        users_list_uniques.append(value)
    i += 1

print(f'Initial List: {users_list}')
print(f'W/a duplicateds: {users_list_uniques}')