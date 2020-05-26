house_value = 10
user_credit = int(input('how much do you have (R$) ? '))
put_down = 0
if user_credit >= 10:
    put_down = house_value * 0.1
else:
    put_down = house_value * 0.2
print(f'you need to put me down R$ {round(put_down)}')