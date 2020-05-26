# array & strings
name = 'valgoi'
print(name)
print(name[0:2])
print(name[0:-2])
print(name[1:])
print(name[-1])
print(name[0])
print(name[1:-1])

numbers = [5, 22, 23, 34, 56]
print(numbers.index(5))
numbers.insert(len(numbers), 20)
numbers.clear()
numbers = [1, 21, 32, 41, 35, 45, 55]
numbers.pop()
print(f"Records: {numbers}. Last's Position: {numbers.index(1)}")
print(1 in numbers)
print(f'occurrences of 1: {numbers.count(1)}')
numbers.sort()
print(numbers)
numbers.reverse()
print(numbers)
letters = ['a', 'b', 'c']
a, b, c = letters
print(a)
print(b)
print(c)