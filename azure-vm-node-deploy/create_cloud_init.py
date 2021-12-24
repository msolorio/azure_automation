import sys, os

current_path = os.getcwd()
script_path = sys.path[0]

PORT = sys.argv[1]
GITHUB_REPO = sys.argv[2]

def main():
    cloud_init_path = ''.join((script_path, '/cloud-init-github.txt'))
    cloud_init_template = open(cloud_init_path, 'r')
    cloud_init_content = cloud_init_template.read()
    new_content = cloud_init_content.replace('<local-port>', PORT).replace('<github-repo>', GITHUB_REPO)

    new_cloud_init_path = ''.join((current_path, '/cloud-init-github.txt'))
    new_cloud_init = open(new_cloud_init_path, 'w')

    new_cloud_init.write(new_content)
