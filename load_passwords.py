from constants import *

def load_passwords():
    pass_list = {}
    with open(PASSWORD_FILE, 'r') as pass_file:
        for line in pass_file:
            username, password = line.split()
            if username not in pass_list:
                pass_list[username] = password 
    return pass_list