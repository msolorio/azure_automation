#!/usr/bin/env python3

# run this file passing in
# 1). the local port of node app
# 2). its github repo
# 3). resource group name
# 4). vm name
# 5). circle ci api token
# ie. azure_vm_circleci_node_deploy 4000 https://github.com/msolorio/test-repo rg-test vm-test 1234

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
