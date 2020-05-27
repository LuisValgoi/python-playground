from pathlib import Path
from spacer import give_space

path = Path('emails')
print(f'Do we have a folder called "emails"? {path.exists()}')
path.mkdir() # creates new folder called email
path.rmdir() # removes new folder called email

give_space()

current_path = Path()

print('[existing .py files] ')
for file in current_path.glob('*.py'):
    print(file)
give_space()
print('[existing files] ')
for resource in current_path.glob('*'):
    print(resource)
