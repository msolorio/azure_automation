# Azure Automation

A collection of automation scripts for interacting with Azure cloud provider.

---

## Goals
- Solidify cloud computing and CI/CD concepts.
- Write python / shell scripts
- Interact with necessary CLIs and APIs
- Document steps for carrying out important cloud computing tasks
- Setup and tear down projects efficiently, host projects only when needed, and save on cloud computing costs.

---
## Projects

###  [Deploy Node Project to an Azure VM](./azure_vm_node_deploy)
- Creates a cloud init file
- Updates `package.json` with process management scripts and installs
- Creates Azure resources

<br>

### [Continuous Deployment with CircleCI to Azure VM](./azure_vm_circleci_node_deploy)
- Creates a cloud init file
- Creates CircleCI config file
- Updates `package.json` with process management scripts and installs
- Creates Azure resources
- Configures Azure VM with SSH for CircleCI
- Sets Privileges in VM
- Configures CircleCI with SSH and environment vars

<br>

### [Delete an Azure Resource Group](./azure_delete_resource_group)
- Removes an Azure resource group by name
