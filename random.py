import random

for i in range(3):
    print(random.random())
    print(random.randint(10, 20))

people = ['luis', 'diego', 'lucas']
print(random.choice(people))