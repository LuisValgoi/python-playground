# Strings
string_double_quotes = "Luis"
string_single_quotes = 'Valgoi'
string_combined_quotes = "User's Name"
string_multiple_lines = """
You gotta be careful, man!
"""
print(f'{string_combined_quotes}: {string_double_quotes}, {string_single_quotes}. {string_multiple_lines}')

# Numbers
int_age = 23
float_height = 1.80
print(f"My Height is: {float_height} and my Age is: {int_age}")

# Boolean
is_developer = True
is_backender = False
is_frontender = not is_backender
print(f'Is a frontender: {is_frontender}')

# List
array_integer = [0, 1, 2, 3]
array_string = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'o', '...']
print(array_integer)
print(array_string)

# Tuple
# Tuples are a group of values like a list and are manipulated in similar ways. But, tuples are fixed in size once they are assigned.
myGroup = ('Rhino', 'Grasshopper', 'Flamingo', 'Bongo')
print(myGroup)

# Dictionary
dictionary_names = {'john': 425, 'tom': 212}
print(dictionary_names['tom'])
print(dictionary_names.get('john'))