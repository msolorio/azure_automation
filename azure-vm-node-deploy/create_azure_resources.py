import sys, os, subprocess

current_path = os.getcwd()
script_path = sys.path[0]

RESOURCE_GROUP = sys.argv[3]

def main():
    # print(RESOURCE_GROUP)
    create_rg_path = ''.join((script_path, '/create_resource_group.sh'))

    subprocess.call(['sh', create_rg_path, RESOURCE_GROUP])