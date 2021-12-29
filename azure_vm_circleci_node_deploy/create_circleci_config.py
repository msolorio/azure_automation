import subprocess, sys, os

current_path = os.getcwd()
script_path = sys.path[0]

def  main():
    cc_dir_path = f'{current_path}/.circleci'

    subprocess.run(['mkdir', cc_dir_path])

    cc_config_template_path = ''.join((script_path, '/config.yml'))
    destination_path = ''.join((current_path, '/.circleci/config.yml'))

    subprocess.run(['cp', cc_config_template_path, destination_path])
