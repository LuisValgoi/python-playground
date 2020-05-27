phone = input('phone: ')
numbers = {
    "1": 'One',
    "2": 'Two',
    "3": 'Three'
}
numbers_text = []
for n in phone:
    value = numbers.get(n, 'N/A')
    numbers_text.append(value)
print(', '.join(numbers_text))
