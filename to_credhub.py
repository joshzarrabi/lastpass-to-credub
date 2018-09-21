import yaml
import sys
import os

def convert_password_to_credhub(password_input):
    credhub_passwords = []
    for key, value in password_input.items():
        credhub_password = {"type": "password", "name": "/concourse/main/" + key, "value": value}
        credhub_passwords.append(credhub_password)
    return credhub_passwords

# fixes weird python multiline string issue
# https://stackoverflow.com/questions/8640959/how-can-i-control-what-scalar-form-pyyaml-uses-for-my-data
def str_presenter(dumper, data):
  if len(data.splitlines()) > 1:  # check for multiline string
    return dumper.represent_scalar('tag:yaml.org,2002:str', data, style='|')
  return dumper.represent_scalar('tag:yaml.org,2002:str', data)


def main():
    yaml.add_representer(str, str_presenter)
    creds_folder = sys.argv[1]
    all_creds = []
    for cred_file in os.listdir(creds_folder):
        if cred_file.endswith('.yml'):
            creds = os.path.join(creds_folder, cred_file)
            creds = open(creds).read()
            creds = yaml.load(creds)
            passwords = convert_password_to_credhub(creds)
            all_creds.extend(passwords)
    print(yaml.dump(all_creds))

main()
