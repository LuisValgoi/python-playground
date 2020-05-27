def calculateIMC(weight, height):
    try:
        return int(weight) / int(height)
    except ZeroDivisionError:
        return 'Cannot divide by 0'
    except TypeError:
        return 'N/A'


weight = input('your weight? ')
height = input('your height? ')
imc = calculateIMC(weight, height)
print(imc)
