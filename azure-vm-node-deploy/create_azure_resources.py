import sys, os, subprocess

current_path = os.getcwd()
script_path = sys.path[0]

RESOURCE_GROUP_NAME = sys.argv[3]
VM_NAME = sys.argv[4]

def main():
    # Create resource group
    create_rg_path = ''.join((script_path, '/create_resource_group.sh'))
    subprocess.call(['sh', create_rg_path, RESOURCE_GROUP_NAME])

    # Create VM
    create_vm_path = ''.join((script_path, '/create_vm.sh'))
    vm = subprocess.check_output(['sh', create_vm_path, RESOURCE_GROUP_NAME, VM_NAME])

    # Open HTTP port 80 on VM
    open_http_port_path = ''.join((script_path, '/open_http_port.sh'))
    subprocess.call(['sh', open_http_port_path, RESOURCE_GROUP_NAME, VM_NAME])


    print('vm ==> ', vm)
    