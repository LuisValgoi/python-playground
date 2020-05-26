start_key = 'start'.upper()
stop_key = 'stop'.upper()
quit_key = 'quit'.upper()
help_key = 'help'.upper()
keys = [start_key, stop_key, quit_key, help_key]

not_found_msg = "I don't' understand that\n"
help_msg = '''start - to start the car
stop - to stop the car
quit - to exit\n'''
start_msg = 'Car started... ready to go'
stop_msg = 'Car stopped'

cmd_user = ''
while cmd_user != quit_key.upper():
    cmd_user = input('>').upper()
    if cmd_user not in keys:
        print(not_found_msg)
    elif cmd_user == help_key:
        print(help_msg)
    elif cmd_user == start_key:
        print(start_msg)
    elif cmd_user == stop_key:
        print(stop_msg)
