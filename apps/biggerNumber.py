amount = int(input('amount items: '))
records = []
i = 0
while i < amount:
    valor = int(input(f'value {i+1}: '))
    records.append(valor)
    i = i + 1
bigger = 0
for record in records:
    if record > bigger:
        bigger = record
print(f'the bigger is: {bigger}')
