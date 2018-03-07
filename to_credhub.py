import yaml
import json

def convert_password_to_credhub(password_input):
    credhub_passwords = []
    for key, value in password_input.items():
        credhub_password = {"type": "password", "name": key, "value": value}
        credhub_passwords.append(credhub_password)
    return credhub_passwords
