import http.client, sys, requests

def set_up_project(API_TOKEN, GITHUB_USERNAME, GITHUB_REPO):
    endpoint = f'https://circleci.com/api/v1.1/project/github/{GITHUB_USERNAME}/{GITHUB_REPO}/follow'

    headers = { 'Circle-Token': API_TOKEN }

    response = requests.post(endpoint, headers=headers)


def add_ssh_key(PUBLIC_IP, PRIVATE_KEY, API_TOKEN, GITHUB_USERNAME, GITHUB_REPO):
    endpoint = f'https://circleci.com/api/v1.1/project/github/{GITHUB_USERNAME}/{GITHUB_REPO}/ssh-key'
    headers = { 'Circle-Token': API_TOKEN }
    data = {
        'hostname': PUBLIC_IP,
        'private_key': PRIVATE_KEY
    }

    response = requests.post(endpoint, headers=headers, data=data)



def add_env_vars(PUBLIC_IP, API_TOKEN, GITHUB_USERNAME, GITHUB_REPO):
    endpoint = f'https://circleci.com/api/v1.1/project/github/{GITHUB_USERNAME}/{GITHUB_REPO}/envvar'

    data1 = { 'name': 'AZURE_VM_USER', 'value': 'azureuser' }
    data2 = { 'name': 'AZURE_VM_IP', 'value': PUBLIC_IP }
    headers = { 'Circle-Token': API_TOKEN }

    response1 = requests.post(endpoint, data=data1, headers=headers)
    response2 = requests.post(endpoint, data=data2, headers=headers)


def main(PUBLIC_IP, PRIVATE_KEY, API_TOKEN, GITHUB_USERNAME):
    GITHUB_REPO = sys.argv[2].split('/')[-1]

    set_up_project(API_TOKEN, GITHUB_USERNAME, GITHUB_REPO)
    add_ssh_key(PUBLIC_IP, PRIVATE_KEY, API_TOKEN, GITHUB_USERNAME, GITHUB_REPO)
    add_env_vars(PUBLIC_IP, API_TOKEN, GITHUB_USERNAME, GITHUB_REPO)