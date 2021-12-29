#!/usr/bin/env python3

# run this file passing in
# - the local port of node app
# - its github repo
# - resource group name
# - vm name
# ie. ./deploy_to_vm.py 4000 https://github.com/msolorio/test-repo rg-test vm-test

import create_cloud_init
import write_package_scripts
import create_azure_resources

create_cloud_init.main()
write_package_scripts.main()
create_azure_resources.main()
