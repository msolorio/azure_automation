#!/usr/bin/env python3

# run this file passing in
# - resource group name to delete

import sys, subprocess

script_path = sys.path[0]
RESOURCE_GROUP_NAME = sys.argv[1]

delete_rg_path = ''.join((script_path, '/delete_rg.sh'))
subprocess.call(['sh', delete_rg_path, RESOURCE_GROUP_NAME])