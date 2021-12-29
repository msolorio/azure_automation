#!/usr/bin/env python3

"""
Steps for automated setup of continuous deployment with CircleCi to an Azure VM for a Node app.

1).
Run this file while navigated into the root of your node project, passing in the appropriate arguments.

a). the local port of node app
b). its github repo
c). resource group name
d). vm name
e). circle ci api token

ie.
azure_vm_circleci_node_deploy.py 4000 https://github.com/msolorio/test-repo rg-test vm-test 1234

2).
In your CircleCi account, Add an Environment variable with the name AZURE_VM_SSH_FINGERPRINT and a value set to the fingerprint of the newly generated alternate ssh key. This will be used to connect to the Azure VM.

3). Push a change up to your project's Github repo, triggering a build, seeing changes in your vm.
"""

import sys

import create_cloud_init
import create_circleci_config
import write_package_scripts
import create_azure_resources
import generate_ssh_on_vm
import set_privileges
import connect_circleci

CIRCLECI_API_TOKEN = sys.argv[5]

create_cloud_init.main()
create_circleci_config.main()
write_package_scripts.main()
PUBLIC_IP = create_azure_resources.main()
CIRCLECI_PRIVATE_KEY = generate_ssh_on_vm.main(PUBLIC_IP)
set_privileges.main(PUBLIC_IP)
connect_circleci.main(PUBLIC_IP, CIRCLECI_PRIVATE_KEY, CIRCLECI_API_TOKEN, 'msolorio')
