az vm create \
--resource-group $1 \
--name $2 \
--location eastus \
--image UbuntuLTS \
--admin-username azureuser \
--generate-ssh-keys \
--custom-data cloud-init-github.txt